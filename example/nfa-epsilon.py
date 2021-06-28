from FAdo.fa import *
from FAdo.fio import *


automata = readFromFile("epsilon-nfa.fa")[0]

print(automata)

automata.display('NFA-epsilon')

automata2 = automata.elimEpsilon()

automata2.display('nfa-elim-epsilon')
