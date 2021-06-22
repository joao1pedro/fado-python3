from FAdo.fa import *
#from FAdo.reex import *
from FAdo.fio import *

automata = readFromFile("nfa_entry.fa")[0] #arquivo para ler as entradas, indice do estado inicial

print(automata)
#automata.evalWordP("01010")
automata.display('NFA')

