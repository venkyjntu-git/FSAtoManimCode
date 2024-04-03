class FSA:
	def __init__(self,st,inpu,tr,ins,f):
		self.states = st
		self.sigma  = inpu
		self.delta  = tr
		self.initialstate = ins
		self.finalstates = f	
	def accepted_or_not(self,x):
		cs = self.initialstate
		for i in x:
			if (cs,i) in self.delta:
				cs = self.delta[(cs,i)]
			else:
				cs = 'rejected'
				break
		if cs in self.finalstates:
			return True
		else:
			return False
	def print_to_manim(self):
		out = open('ex.py','w')
		print(f'from manim import *',file=out)
		for s in self.states:
			print(f'c{s} = Circle(radius=0.8)',file=out)

s1 = ['q0','q1']
i1 = ['0']
d1 = {('q0','0'):'q1',('q1','0'):'q0'}
st1 = 'q0'
f1  = ['q1']
M1 = FSA(s1,i1,d1,st1,f1)
M1.print_to_manim()

# s1 = ['q0','q1','q2']
# i1 = ['0','1']
# d1 = {('q0','0'):'q1',('q0','1'):'q1',
#       ('q1','0'):'q2',('q1','1'):'q2',
#       ('q2','0'):'q0',('q2','1'):'q0'
# }
# st1 = 'q0'
# f1  = ['q0']
# M1 = FSA(s1,i1,d1,st1,f1)


# s1 = ['q0','q1','q2','q3']
# i1 = ['0','1']
# d1 = {('q0','0'):'q1',('q0','1'):'q1',
#       ('q1','0'):'q2',('q1','1'):'q2',
#       ('q2','0'):'q3',('q2','1'):'q3',
#       ('q3','0'):'q0',('q3','1'):'q0'
# }
# st1 = 'q0'
# f1  = ['q0']
# M2 = FSA(s1,i1,d1,st1,f1)
# M = M1.fsa_union(M2)
# x = input('enter string')
# print(M.accepted_or_not(x))