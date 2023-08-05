import warnings
import numpy as np
from . import gate
from .backends.numpy_backend import NumPyBackend
from .backends.qasm_output_backend import QasmOutputBackend
from .backends.mqc_backend import MQCBackend

GATE_SET = {
    "i": gate.IGate,
    "x": gate.XGate,
    "y": gate.YGate,
    "z": gate.ZGate,
    "h": gate.HGate,
    "t": gate.TGate,
    "s": gate.SGate,
    "cz": gate.CZGate,
    "cx": gate.CXGate,
    "cnot": gate.CXGate,
    "rx": gate.RXGate,
    "ry": gate.RYGate,
    "rz": gate.RZGate,
    "phase": gate.RZGate,
    "u1": gate.RZGate,
    "ccx": gate.ToffoliGate,
    "toffoli": gate.ToffoliGate,
    "t": gate.TGate,
    "tdg": gate.TDagGate,
    "s": gate.SGate,
    "sdg": gate.SDagGate,
    "measure": gate.Measurement,
    "m": gate.Measurement,
}

BACKENDS = {
    "numpy": NumPyBackend,
    "mqc": MQCBackend,
    "qasm_output": QasmOutputBackend,
}
DEFAULT_BACKEND_NAME = "numpy"

class Circuit:
    def __init__(self, n_qubits=0, ops=None):
        self.ops = ops or []
        self._backends = {}
        self._default_backend = None
        # ad-hoc
        self.n_qubits = n_qubits
        if n_qubits > 0:
            self.i[n_qubits - 1]

    def __get_backend(self, backend_name):
        try:
            return self._backends[backend_name]
        except KeyError:
            backend = BACKENDS.get(backend_name)
            if backend is None:
                raise ValueError(f"Backend {backend_name} doesn't exist.")
        self._backends[backend_name] = backend()
        return self._backends[backend_name]

    def __backend_runner_wrapper(self, backend_name):
        backend = self.__get_backend(backend_name)
        def runner(*args, **kwargs):
            return backend.run(self.ops, self.n_qubits, *args, **kwargs)
        return runner

    def __getattr__(self, name):
        if name in GATE_SET:
            return _GateWrapper(self, name, GATE_SET[name])
        if name.startswith("run_with_"):
            backend_name = name[9:]
            if backend_name in BACKENDS:
                return self.__backend_runner_wrapper(backend_name)
            raise AttributeError(f"Backend '{backend_name}' is not exists.")
        raise AttributeError(f"'circuit' object has no attribute or gate '{name}'")

    def __add__(self, other):
        if not isinstance(other, Circuit):
            return NotImplemented
        c = self.copy()
        c += other
        return c

    def __iadd__(self, other):
        if not isinstance(other, Circuit):
            return NotImplemented
        self.ops += other.ops
        self.n_qubits = max(self.n_qubits, other.n_qubits)
        return self

    def copy(self, copy_backends=True, copy_default_backend=True, copy_cache=None, copy_history=None):
        """Copy the circuit.

        :params
        copy_backends :bool copy backends if True.
        copy_default_backend :bool copy default_backend if True
        """
        copied = Circuit(self.n_qubits, self.ops.copy())
        if copy_backends:
            copied._backends = {k: v.copy() for k, v in self._backends.items()}
        if copy_default_backend:
            copied._default_backend = self._default_backend

        # Warn for deprecated options
        if copy_cache is not None:
            warnings.warn("copy_cache is deprecated. Use copy_backends instead.", DeprecationWarning)
        if copy_history is not None:
            warnings.warn("copy_history is deprecated.", DeprecationWarning)

        return copied

    def run(self, *args, backend=None, **kwargs):
        if backend is None:
            if self._default_backend is None:
                backend = self.__get_backend(DEFAULT_BACKEND_NAME)
            else:
                backend = self.__get_backend(self._default_backend)
        elif isinstance(backend, str):
            backend = self.__get_backend(backend)
        return backend.run(self.ops, self.n_qubits, *args, **kwargs)

    def make_cache(self, backend=None):
        """Make a cache to reduce the time of run. Some backends may implemented it.

        This is temporary API. It may changed or deprecated."""
        if backend is None:
            if self._default_backend is None:
                backend = DEFAULT_BACKEND_NAME
            else:
                backend = self._default_backend
        return self.__get_backend(backend).make_cache(self.ops, self.n_qubits)

    def to_qasm(self, *args, **kwargs):
        return self.run_with_qasm_output(*args, **kwargs)

    def set_default_backend(self, backend_name):
        """Set the default backend of this circuit.

        This setting is only applied for this circuit.
        If you want to change the default backend of all gates,
        use `BlueqatGlobalSetting.set_default_backend()`.

        After set the default backend by this method,
        global setting is ignored even if `BlueqatGlobalSetting.set_default_backend()` is called.
        If you want to use global default setting, call this method with backend_name=None.

        :params
        backend_name: str or None: new default backend name. if None is given, global setting is applied.
        """
        if backend_name not in BACKENDS:
            raise ValueError(f"Unknown backend '{backend_name}'.")
        self._default_backend = backend_name

    def get_default_backend_name(self):
        return DEFAULT_BACKEND_NAME if self._default_backend is None else self._default_backend

class _GateWrapper:
    def __init__(self, circuit, name, gate):
        self.circuit = circuit
        self.target = None
        self.name = name
        self.gate = gate
        self.args = ()
        self.kwargs = {}

    def __call__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        return self

    def __getitem__(self, args):
        self.target = args
        self.circuit.ops.append(self.gate(self.target, *self.args, **self.kwargs))
        # ad-hoc
        self.circuit.n_qubits = max(gate.get_maximum_index(args) + 1, self.circuit.n_qubits)
        return self.circuit

    def __str__(self):
        if self.args:
            args_str = str(self.args)
            if self.kwargs:
                args_str = args_str[:-1] + ", kwargs=" + str(self.kwargs) + ")"
        elif self.kwargs:
            args_str = "(kwargs=" + str(self.kwargs) + ")"
        else:
            args_str = ""
        return self.name + args_str + " " + str(self.target)

class BlueqatGlobalSetting:
    """Setting for Blueqat."""
    @staticmethod
    def register_gate(name, gateclass, allow_overwrite=False):
        """Register new gate to gate set."""
        if hasattr(Circuit, name):
            if allow_overwrite:
                warnings.warn(f"Circuit has attribute `{name}`.")
            else:
                raise ValueError(f"Circuit has attribute `{name}`.")
        if name.startswith("run_with_"):
            if allow_overwrite:
                warnings.warn(f"Gate name `{name}` may conflict with run of backend.")
            else:
                raise ValueError(f"Gate name `{name}` shall not start with 'run_with_'.")
        if not allow_overwrite:
            if name in GATE_SET:
                raise ValueError(f"Gate '{name}' is already exists in gate set.")
        GATE_SET[name] = gateclass

    @staticmethod
    def unregister_gate(name):
        """Unregister a gate from gate set"""
        if name not in GATE_SET:
            raise ValueError(f"Gate '{name}' is not registered.")
        del GATE_SET[name]

    @staticmethod
    def register_backend(name, backend, allow_overwrite=False):
        """Register new backend."""
        if hasattr(Circuit, "run_with_" + name):
            if allow_overwrite:
                warnings.warn(f"Circuit has attribute `run_with_{name}`.")
            else:
                raise ValueError(f"Circuit has attribute `run_with_{name}`.")
        if not allow_overwrite:
            if name in BACKENDS:
                raise ValueError(f"Backend '{name}' is already registered as backend.")
        BACKENDS[name] = backend

    @staticmethod
    def remove_backend(name):
        """Unregister a backend."""
        if name not in GATE_SET:
            raise ValueError(f"Backend '{name}' is not registered.")
        del BACKENDS[name]

    @staticmethod
    def set_default_backend(name):
        if name not in BACKENDS:
            raise ValueError(f"Backend '{name}' is not registered.")
        global DEFAULT_BACKEND_NAME
        DEFAULT_BACKEND_NAME = name

    @staticmethod
    def get_default_backend_name():
        return DEFAULT_BACKEND_NAME
