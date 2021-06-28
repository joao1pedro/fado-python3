from FAdo.reex import *
from FAdo.fio import *
from FAdo.fa import *

# construir uma expressão regular como classe Python
r = star(disj(regexp("a"),concat(regexp("b"),regexp("a"))))

print(r)

# converter uma string para expressão regular
r = str2regexp("(a+ba)*")
print(r)

#converter DFA para regex
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

automata_new = automata.regexp()
print(automata_new)

