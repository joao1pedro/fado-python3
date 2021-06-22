from FAdo.fa import *
from FAdo.reex import *
from FAdo.fio import *

automata = DFA()
automata.setSigma(['0','1'])
automata.addState('q0')
automata.addState('q1')
automata.addState('q2')

automata.setInitial(0) ## indice do estado inicial
automata.addFinal(2) ## indice do estado final

automata.addTransition(0, '1', 0)
automata.addTransition(0, '0', 1)
automata.addTransition(1, '0', 1)
automata.addTransition(1, '1', 2)
automata.addTransition(2, '0', 2)
automata.addTransition(2, '1', 2)

print('print automata:')
print(automata)
print('\n')
print('verify word w = 10001')
print(automata.evalWordP('10001'))
print('\n')
print('verify word w = 0001')
print(automata.evalWordP('0001'))
print('\n')
print('verify word w = 11111')
print(automata.evalWordP('11111'))

automata.display('dfa')
