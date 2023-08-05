import numpy as np

def pauli(qubo):
	"""
	Convert to pauli operators of universal gate model.
	Requires blueqat.
	"""
	from blueqat.pauli import qubo_bit
	h = 0.0
	assert all(len(q) == len(qubo) for q in qubo)
	for i in range(len(qubo)):
		h += qubo_bit(i) * qubo[i][i]
		for j in range(i + 1, len(qubo)):
			h += qubo_bit(i)*qubo_bit(j) * (qubo[i][j] + qubo[j][i])
	return h

def optx(quboh): 
	try:
		import sympy
	except ImportError:
		raise ImportError("optx() requires sympy. Please install before call this function.")

	optx_E = sympy.expand(quboh)
	symbol_list = list(optx_E.free_symbols)
	sympy.var(' '.join(map(str,symbol_list)),positive=True)
	for i in range(len(symbol_list)):
		optx_E = optx_E.subs(symbol_list[i]*symbol_list[i],symbol_list[i])
	return optx_E

def optm(quboh,numM):
	try:
		import sympy
	except ImportError:
		raise ImportError("optm() requires sympy. Please install before call this function.") 
	optm_E = sympy.expand(quboh) 
	symbol_list = ["q"+str(i) for i in range(numM)] 
	sympy.var(' '.join(symbol_list),positive=True) 

	symbol_list_proto = list(optm_E.free_symbols) 
	for i in range(len(symbol_list_proto)): 
		optm_E = optm_E.subs(symbol_list_proto[i]*symbol_list_proto[i],symbol_list_proto[i]) 

	optm_M = np.zeros((numM,numM)) 

	for i in range(numM): 
		for j in range(i+1,numM): 
			optm_M[i][j] = optm_E.coeff(symbol_list[i]+"*"+symbol_list[j]) 

		temp1 = sympy.poly(optm_E.coeff(symbol_list[i])) 
		optm_M[i][i] = sympy.poly(optm_E.coeff(symbol_list[i])).coeff_monomial(1) 

	return optm_M

def Ei(q3,j3):
	EE = 0
	for i in range(len(q3)):
		EE += q3[i]*j3[i][i]
		EE += sum(q3[i]*q3[i+1:]*j3[i][i+1:])
	return EE

def Ei_sqa(q, J, T, P, G):
	E = 0
	for p in range(P):
		E += Ei(q[p], J) / P
		E += T / 2 * np.log(1 / np.tanh(G / T / P)) * np.sum(q[p,:] * q[(p+1+P) % P, :])
	return E

def sel(selN,selK,selarr=[]):
	"""
	Automatically create QUBO which select K qubits from N qubits
	.. code-block:: python
		print(wq.sel(5,2))
		#=>
		[[-3  2  2  2  2]
		[ 0 -3  2  2  2]
		[ 0  0 -3  2  2]
		[ 0  0  0 -3  2]
		[ 0  0  0  0 -3]]
		
	if you set array on the 3rd params, the result likely to choose the nth qubit in the array
	.. code-block:: python
		print(wq.sel(5,2,[0,2]))
		#=>
		[[-3.5  2.   2.   2.   2. ]
		[ 0.  -3.   2.   2.   2. ]
		[ 0.   0.  -3.5  2.   2. ]
		[ 0.   0.   0.  -3.   2. ]
		[ 0.   0.   0.   0.  -3. ]]
	"""
	selres = np.diag([1-2*selK]*selN)+np.triu([[2] * selN for i in range(selN)],k=1)
	selmat = np.zeros(selN)
	for i in range(len(selarr)):
		selmat[selarr[i]] += 1
	selres = np.asarray(selres) - 0.5*np.diag(selmat)
	return selres

def mul(mulA,mulB):
	return np.triu(np.outer(mulA,mulB))+np.triu(np.outer(mulA,mulB),k=1)

def sqr(sqrA):
	return np.triu(np.outer(sqrA,sqrA))+np.triu(np.outer(sqrA,sqrA),k=1)

def net(narr,nnet):
	"""
	Automatically create QUBO which has value 1 for all connectivity defined by array of edges and graph size N
	.. code-block:: python
		print(wq.net([[0,1],[1,2]],4))
		#=>
		[[0. 1. 0. 0.]
		[0. 0. 1. 0.]
		[0. 0. 0. 0.]
		[0. 0. 0. 0.]]
	this create 4*4 QUBO and put value 1 on connection between 0th and 1st qubit, 1st and 2nd qubit
	"""
	mat = np.zeros((nnet,nnet))
	for i in range(len(narr)):
		narr[i] = np.sort(narr[i])
		mat[narr[i][0]][narr[i][1]] = 1
	return mat

def counter(narr):
	import collections
	dis = []
	for i in range(len(narr)):
		dis.append(''.join([str(x) for x in narr[i]]))
	return collections.Counter(dis)

def diag(diag_ele):
	"""
	Create QUBO with diag from list
	.. code-block:: python
		print(wq.diag([1,2,1]))
		#=>
		[[1 0 0]
		[0 2 0]
		[0 0 1]]
	"""
	return np.diag(diag_ele)

def zeros(zeros_ele):
	"""
	Create QUBO with all element value as 0
	.. code-block:: python
		print(wq.zeros(3))
		#=>
		[[0. 0. 0.]
		[0. 0. 0.]
		[0. 0. 0.]]
	"""
	return np.zeros((zeros_ele,zeros_ele))

def rands(rands_ele):
	"""
	Create random QUBO
	"""
	return np.triu(np.random.rand(rands_ele,rands_ele))

def dbms(dbms_arr,weight_init=0):
	dbmN = np.sum(dbms_arr)
	if weight_init == 0:
		dbms_mat = np.diag(np.random.rand(dbmN))	
	else:
		dbms_mat = np.diag([0.5 for i in range(dbmN)])
	cc = 0
	for k in range(len(dbms_arr)-1):
		for i in range(cc,cc+dbms_arr[k]):
			for j in range(cc+dbms_arr[k],cc+dbms_arr[k]+dbms_arr[k+1]):
				if weight_init == 0:
					dbms_mat[i][j] = np.random.rand()
				else:
					dbms_mat[i][j] = weight_init
		cc = cc + dbms_arr[k]
	return dbms_mat

class opt:
	"""
	Optimizer for SA/SQA.
	"""

	def __init__(self):
		#: Initial temperature [SA]
		self.Ts = 5
		#: Final temperature [SA]. Temperature [SQA]
		self.Tf = 0.02

		#: Initial strength of transverse magnetic field. [SQA]
		self.Gs = 10
		#: Final strength of transverse magnetic field. [SQA]
		self.Gf = 0.02
		#: Trotter slices [SQA]
		self.tro = 8

		#: Descreasing rate of temperature [SA]
		self.R = 0.95
		#: Iterations [SA]
		self.ite = 1000
		#: QUBO
		self.qubo = []
		self.J = []

		self.ep = 0
		#: List of energies
		self.E = []

		self.dwaveendpoint = 'https://cloud.dwavesys.com/sapi'
		self.dwavetoken = ''
		self.dwavesolver = 'DW_2000Q_2_1'

		#: RBM Models
		self.RBMvisible = 0
		self.RBMhidden = 0

	def reJ(self):
        	return np.triu(self.J) + np.triu(self.J, k=1).T

	def qi(self):
		nn = len(self.qubo)
		self.J = [np.random.choice([1.,1.],nn) for j in range(nn)]
		for i in range(nn):
			for j in range(i+1,nn):
				self.J[i][j] = self.qubo[i][j]/4

		self.J = np.triu(self.J)+np.triu(self.J,k=1).T

		for i in range(nn):
			sum = 0
			for j in range(nn):
				if i == j:
					sum += self.qubo[i][i]*0.5
				else:
					sum += self.J[i][j]
			self.J[i][i] = sum

		self.ep = 0

		for i in range(nn):
			self.ep += self.J[i][i]
			for j in range(i+1,nn):
				self.ep -= self.J[i][j]

		self.J = np.triu(self.J)

	def plot(self):
		"""
		Draws energy chart using matplotlib.
		"""
		import matplotlib.pyplot as plt
		plt.plot(self.E)
		plt.show()

	def sa(self,shots=1,sampler="normal",targetT=0.02,verbose=False):
		"""
		Run SA with provided QUBO. 
		Set qubo attribute in advance of calling this method.
		"""
		if self.qubo != []:
			self.qi()
		J = self.reJ()
		N = len(J)

		if sampler == "fast":
			itetemp = 100
			Rtemp = 0.75
		else:
			itetemp = self.ite
			Rtemp = self.R

		self.E = []
		qq = []
		for i in range(shots):
			T = self.Ts
			q = np.random.choice([-1,1],N)
			EE = []
			EE.append(Ei(q,self.J)+self.ep)
			while T>targetT:
				x_list = np.random.randint(0, N, itetemp)
				for x in x_list:
					q2 = np.ones(N)*q[x]
					q2[x] = 1
					dE = -2*sum(q*q2*J[:,x])

					if dE < 0 or np.exp(-dE/T) > np.random.random_sample():
						q[x] *= -1
				EE.append(Ei(q,self.J)+self.ep)
				T *= Rtemp
			self.E.append(EE)
			qtemp = (np.asarray(q,int)+1)/2
			qq.append([int(s) for s in qtemp])
			if verbose == True:
				print(i,':',[int(s) for s in qtemp])
			if shots == 1:
				qq = qq[0]
		if shots == 1:
			self.E = self.E[0]
		return qq

	def sqa(self):
		"""
		Run SQA with provided QUBO.
		Set qubo attribute in advance of calling this method.
		"""
		G = self.Gs
		if self.qubo != []:
			self.qi()
		J = self.reJ()
		N = len(J)
		q = np.random.choice([-1,1], self.tro*N).reshape(self.tro, N)
		self.E.append(Ei_sqa(q, J, self.Tf, self.tro, G) + self.ep)
		while G>self.Gf:
			for _ in range(self.ite):
				x = np.random.randint(N)
				y = np.random.randint(self.tro)
				dE = 0

				for j in range(N):
					if j == x:
						dE += -2*q[y][x]*J[x][x] / self.tro
					else:
						dE += -2*q[y][j]*q[y][x]*J[j][x] / self.tro

				dE += q[y][x]*(q[(self.tro+y-1)%self.tro][x]+q[(y+1)%self.tro][x])*np.log(1/np.tanh(G/self.Tf/self.tro))*self.Tf

				if dE < 0 or np.exp(-dE/self.Tf) > np.random.random_sample():
					q[y][x] *= -1
			self.E.append(Ei_sqa(q, J, self.Tf, self.tro, G)+self.ep)
			G *= self.R
		#qq = [int((i+1)/2) for i in q]
		return q

	def dw(self):
		try:
			from dwave.cloud import Client
		except ImportError:
			raise ImportError("dw() requires dwave-cloud-client. Please install before call this function.")
		solver = Client.from_config(endpoint= self.dwaveendpoint, token=self.dwavetoken, solver=self.dwavesolver).get_solver()

		if self.qubo != []:
			self.qi()

		# for hi
		harr = np.diag(self.J)
		larr = []
		for i in solver.nodes:
			if i < len(harr):
				larr.append(harr[i])
		linear = {index: larr[index] for index in range(len(larr))}

		# for jij
		qarr = []
		qarrv = []
		for i in solver.undirected_edges:
			if i[0] < len(harr) and i[1] < len(harr):
				qarr.append(i)
				qarrv.append(self.J[i[0]][i[1]])

		quad = {key: j for key,j in zip(qarr,qarrv)}
		computation = solver.sample_ising(linear, quad, num_reads=1)

		return computation.samples[0][:len(harr)]

