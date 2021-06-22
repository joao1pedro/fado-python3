from FAdo.fa import *
from FAdo.fio import *

ndfa = NFA()
ndfa.setSigma(['0','1'])
ndfa.addState('q0')
ndfa.addState('q1')
ndfa.addState('q2')

ndfa.addInitial(0)
ndfa.addFinal(2)

ndfa.addTransition(0, '0', 0)
ndfa.addTransition(0, '0', 1)
ndfa.addTransition(1, '1', 0)
ndfa.addTransition(1, '0', 2)
ndfa.addTransition(2, '0', 2)

ndfa.evalWordP('010')
ndfa.evalWordP('0100')
ndfa.evalWordP('11')

ndfa.display('nfa2')

min = ndfa.minimal()

min.display('minimal')
