# compiled with BefunCompile v1.0.1 (c) 2015
# execute with at least Python3
from random import randint
g=[[118,32,32,32,32,32,47,47,32,80,114,111,106,101,99,116,32,69,117,108,101,114,32,45,32,80,114,111,98,108,101,109,32,49,51,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[32,32,32,32,32,32,51,55,49,48,55,50,56,55,53,51,51,57,48,50,49,48,50,55,57,56,55,57,55,57,57,56,50,50,48,56,51,55,53,57,48,50,52,54,53,49,48,49,51,53,55,52,48,50,53,48,32,32,32],[32,32,32,32,32,32,52,54,51,55,54,57,51,55,54,55,55,52,57,48,48,48,57,55,49,50,54,52,56,49,50,52,56,57,54,57,55,48,48,55,56,48,53,48,52,49,55,48,49,56,50,54,48,53,51,56,32,32,32],[32,32,32,32,32,32,55,52,51,50,52,57,56,54,49,57,57,53,50,52,55,52,49,48,53,57,52,55,52,50,51,51,51,48,57,53,49,51,48,53,56,49,50,51,55,50,54,54,49,55,51,48,57,54,50,57,32,32,32],[32,32,32,32,32,32,57,49,57,52,50,50,49,51,51,54,51,53,55,52,49,54,49,53,55,50,53,50,50,52,51,48,53,54,51,51,48,49,56,49,49,48,55,50,52,48,54,49,53,52,57,48,56,50,53,48,32,32,32],[32,32,32,32,32,32,50,51,48,54,55,53,56,56,50,48,55,53,51,57,51,52,54,49,55,49,49,55,49,57,56,48,51,49,48,52,50,49,48,52,55,53,49,51,55,55,56,48,54,51,50,52,54,54,55,54,32,32,32],[32,32,32,32,32,32,56,57,50,54,49,54,55,48,54,57,54,54,50,51,54,51,51,56,50,48,49,51,54,51,55,56,52,49,56,51,56,51,54,56,52,49,55,56,55,51,52,51,54,49,55,50,54,55,53,55,32,32,32],[32,32,32,32,32,32,50,56,49,49,50,56,55,57,56,49,50,56,52,57,57,55,57,52,48,56,48,54,53,52,56,49,57,51,49,53,57,50,54,50,49,54,57,49,50,55,53,56,56,57,56,51,50,55,51,56,32,32,32],[32,32,32,32,32,32,52,52,50,55,52,50,50,56,57,49,55,52,51,50,53,50,48,51,50,49,57,50,51,53,56,57,52,50,50,56,55,54,55,57,54,52,56,55,54,55,48,50,55,50,49,56,57,51,49,56,32,32,32],[32,32,32,32,32,32,52,55,52,53,49,52,52,53,55,51,54,48,48,49,51,48,54,52,51,57,48,57,49,49,54,55,50,49,54,56,53,54,56,52,52,53,56,56,55,49,49,54,48,51,49,53,51,50,55,54,32,32,32],[32,32,32,32,32,32,55,48,51,56,54,52,56,54,49,48,53,56,52,51,48,50,53,52,51,57,57,51,57,54,49,57,56,50,56,57,49,55,53,57,51,54,54,53,54,56,54,55,53,55,57,51,52,57,53,49,32,32,32],[32,32,32,32,32,32,54,50,49,55,54,52,53,55,49,52,49,56,53,54,53,54,48,54,50,57,53,48,50,49,53,55,50,50,51,49,57,54,53,56,54,55,53,53,48,55,57,51,50,52,49,57,51,51,51,49,32,32,32],[32,32,32,32,32,32,54,52,57,48,54,51,53,50,52,54,50,55,52,49,57,48,52,57,50,57,49,48,49,52,51,50,52,52,53,56,49,51,56,50,50,54,54,51,51,52,55,57,52,52,55,53,56,49,55,56,32,32,32],[32,32,32,32,32,32,57,50,53,55,53,56,54,55,55,49,56,51,51,55,50,49,55,54,54,49,57,54,51,55,53,49,53,57,48,53,55,57,50,51,57,55,50,56,50,52,53,53,57,56,56,51,56,52,48,55,32,32,32],[32,32,32,32,32,32,53,56,50,48,51,53,54,53,51,50,53,51,53,57,51,57,57,48,48,56,52,48,50,54,51,51,53,54,56,57,52,56,56,51,48,49,56,57,52,53,56,54,50,56,50,50,55,56,50,56,32,32,32],[32,32,32,32,32,32,56,48,49,56,49,49,57,57,51,56,52,56,50,54,50,56,50,48,49,52,50,55,56,49,57,52,49,51,57,57,52,48,53,54,55,53,56,55,49,53,49,49,55,48,48,57,52,51,57,48,32,32,32],[32,32,32,32,32,32,51,53,51,57,56,54,54,52,51,55,50,56,50,55,49,49,50,54,53,51,56,50,57,57,56,55,50,52,48,55,56,52,52,55,51,48,53,51,49,57,48,49,48,52,50,57,51,53,56,54,32,32,32],[32,32,32,32,32,32,56,54,53,49,53,53,48,54,48,48,54,50,57,53,56,54,52,56,54,49,53,51,50,48,55,53,50,55,51,51,55,49,57,53,57,49,57,49,52,50,48,53,49,55,50,53,53,56,50,57,32,32,32],[32,32,32,32,32,32,55,49,54,57,51,56,56,56,55,48,55,55,49,53,52,54,54,52,57,57,49,49,53,53,57,51,52,56,55,54,48,51,53,51,50,57,50,49,55,49,52,57,55,48,48,53,54,57,51,56,32,32,32],[32,32,32,32,32,32,53,52,51,55,48,48,55,48,53,55,54,56,50,54,54,56,52,54,50,52,54,50,49,52,57,53,54,53,48,48,55,54,52,55,49,55,56,55,50,57,52,52,51,56,51,55,55,54,48,52,32,32,32],[32,32,32,32,32,32,53,51,50,56,50,54,53,52,49,48,56,55,53,54,56,50,56,52,52,51,49,57,49,49,57,48,54,51,52,54,57,52,48,51,55,56,53,53,50,49,55,55,55,57,50,57,53,49,52,53,32,32,32],[32,32,32,32,32,32,51,54,49,50,51,50,55,50,53,50,53,48,48,48,50,57,54,48,55,49,48,55,53,48,56,50,53,54,51,56,49,53,54,53,54,55,49,48,56,56,53,50,53,56,51,53,48,55,50,49,32,32,32],[32,32,32,32,32,32,52,53,56,55,54,53,55,54,49,55,50,52,49,48,57,55,54,52,52,55,51,51,57,49,49,48,54,48,55,50,49,56,50,54,53,50,51,54,56,55,55,50,50,51,54,51,54,48,52,53,32,32,32],[32,32,32,32,32,32,49,55,52,50,51,55,48,54,57,48,53,56,53,49,56,54,48,54,54,48,52,52,56,50,48,55,54,50,49,50,48,57,56,49,51,50,56,55,56,54,48,55,51,51,57,54,57,52,49,50,32,32,32],[32,32,32,32,32,32,56,49,49,52,50,54,54,48,52,49,56,48,56,54,56,51,48,54,49,57,51,50,56,52,54,48,56,49,49,49,57,49,48,54,49,53,53,54,57,52,48,53,49,50,54,56,57,54,57,50,32,32,32],[32,32,32,32,32,32,53,49,57,51,52,51,50,53,52,53,49,55,50,56,51,56,56,54,52,49,57,49,56,48,52,55,48,52,57,50,57,51,50,49,53,48,53,56,54,52,50,53,54,51,48,52,57,52,56,51,32,32,32],[32,32,32,32,32,32,54,50,52,54,55,50,50,49,54,52,56,52,51,53,48,55,54,50,48,49,55,50,55,57,49,56,48,51,57,57,52,52,54,57,51,48,48,52,55,51,50,57,53,54,51,52,48,54,57,49,32,32,32],[32,32,32,32,32,32,49,53,55,51,50,52,52,52,51,56,54,57,48,56,49,50,53,55,57,52,53,49,52,48,56,57,48,53,55,55,48,54,50,50,57,52,50,57,49,57,55,49,48,55,57,50,56,50,48,57,32,32,32],[32,32,32,32,32,32,53,53,48,51,55,54,56,55,53,50,53,54,55,56,55,55,51,48,57,49,56,54,50,53,52,48,55,52,52,57,54,57,56,52,52,53,48,56,51,51,48,51,57,51,54,56,50,49,50,54,32,32,32],[32,32,32,32,32,32,49,56,51,51,54,51,56,52,56,50,53,51,51,48,49,53,52,54,56,54,49,57,54,49,50,52,51,52,56,55,54,55,54,56,49,50,57,55,53,51,52,51,55,53,57,52,54,53,49,53,32,32,32],[32,32,32,32,32,32,56,48,51,56,54,50,56,55,53,57,50,56,55,56,52,57,48,50,48,49,53,50,49,54,56,53,53,53,52,56,50,56,55,49,55,50,48,49,50,49,57,50,53,55,55,54,54,57,53,52,32,32,32],[32,32,32,32,32,32,55,56,49,56,50,56,51,51,55,53,55,57,57,51,49,48,51,54,49,52,55,52,48,51,53,54,56,53,54,52,52,57,48,57,53,53,50,55,48,57,55,56,54,52,55,57,55,53,56,49,32,32,32],[32,32,32,32,32,32,49,54,55,50,54,51,50,48,49,48,48,52,51,54,56,57,55,56,52,50,53,53,51,53,51,57,57,50,48,57,51,49,56,51,55,52,52,49,52,57,55,56,48,54,56,54,48,57,56,52,32,32,32],[32,32,32,32,32,32,52,56,52,48,51,48,57,56,49,50,57,48,55,55,55,57,49,55,57,57,48,56,56,50,49,56,55,57,53,51,50,55,51,54,52,52,55,53,54,55,53,53,57,48,56,52,56,48,51,48,32,32,32],[32,32,32,32,32,32,56,55,48,56,54,57,56,55,53,53,49,51,57,50,55,49,49,56,53,52,53,49,55,48,55,56,53,52,52,49,54,49,56,53,50,52,50,52,51,50,48,54,57,51,49,53,48,51,51,50,32,32,32],[32,32,32,32,32,32,53,57,57,53,57,52,48,54,56,57,53,55,53,54,53,51,54,55,56,50,49,48,55,48,55,52,57,50,54,57,54,54,53,51,55,54,55,54,51,50,54,50,51,53,52,52,55,50,49,48,32,32,32],[32,32,32,32,32,32,54,57,55,57,51,57,53,48,54,55,57,54,53,50,54,57,52,55,52,50,53,57,55,55,48,57,55,51,57,49,54,54,54,57,51,55,54,51,48,52,50,54,51,51,57,56,55,48,56,53,32,32,32],[32,32,32,32,32,32,52,49,48,53,50,54,56,52,55,48,56,50,57,57,48,56,53,50,49,49,51,57,57,52,50,55,51,54,53,55,51,52,49,49,54,49,56,50,55,54,48,51,49,53,48,48,49,50,55,49,32,32,32],[32,32,32,32,32,32,54,53,51,55,56,54,48,55,51,54,49,53,48,49,48,56,48,56,53,55,48,48,57,49,52,57,57,51,57,53,49,50,53,53,55,48,50,56,49,57,56,55,52,54,48,48,52,51,55,53,32,32,32],[32,32,32,32,32,32,51,53,56,50,57,48,51,53,51,49,55,52,51,52,55,49,55,51,50,54,57,51,50,49,50,51,53,55,56,49,53,52,57,56,50,54,50,57,55,52,50,53,53,50,55,51,55,51,48,55,32,32,32],[32,32,32,32,32,32,57,52,57,53,51,55,53,57,55,54,53,49,48,53,51,48,53,57,52,54,57,54,54,48,54,55,54,56,51,49,53,54,53,55,52,51,55,55,49,54,55,52,48,49,56,55,53,50,55,53,32,32,32],[32,32,32,32,32,32,56,56,57,48,50,56,48,50,53,55,49,55,51,51,50,50,57,54,49,57,49,55,54,54,54,56,55,49,51,56,49,57,57,51,49,56,49,49,48,52,56,55,55,48,49,57,48,50,55,49,32,32,32],[32,32,32,32,32,32,50,53,50,54,55,54,56,48,50,55,54,48,55,56,48,48,51,48,49,51,54,55,56,54,56,48,57,57,50,53,50,53,52,54,51,52,48,49,48,54,49,54,51,50,56,54,54,53,50,54,32,32,32],[32,32,32,32,32,32,51,54,50,55,48,50,49,56,53,52,48,52,57,55,55,48,53,53,56,53,54,50,57,57,52,54,53,56,48,54,51,54,50,51,55,57,57,51,49,52,48,55,52,54,50,53,53,57,54,50,32,32,32],[32,32,32,32,32,32,50,52,48,55,52,52,56,54,57,48,56,50,51,49,49,55,52,57,55,55,55,57,50,51,54,53,52,54,54,50,53,55,50,52,54,57,50,51,51,50,50,56,49,48,57,49,55,49,52,49,32,32,32],[32,32,32,32,32,32,57,49,52,51,48,50,56,56,49,57,55,49,48,51,50,56,56,53,57,55,56,48,54,54,54,57,55,54,48,56,57,50,57,51,56,54,51,56,50,56,53,48,50,53,51,51,51,52,48,51,32,32,32],[32,32,32,32,32,32,51,52,52,49,51,48,54,53,53,55,56,48,49,54,49,50,55,56,49,53,57,50,49,56,49,53,48,48,53,53,54,49,56,54,56,56,51,54,52,54,56,52,50,48,48,57,48,52,55,48,32,32,32],[32,32,32,32,32,32,50,51,48,53,51,48,56,49,49,55,50,56,49,54,52,51,48,52,56,55,54,50,51,55,57,49,57,54,57,56,52,50,52,56,55,50,53,53,48,51,54,54,51,56,55,56,52,53,56,51,32,32,32],[32,32,32,32,32,32,49,49,52,56,55,54,57,54,57,51,50,49,53,52,57,48,50,56,49,48,52,50,52,48,50,48,49,51,56,51,51,53,49,50,52,52,54,50,49,56,49,52,52,49,55,55,51,52,55,48,32,32,32],[32,32,32,32,32,32,54,51,55,56,51,50,57,57,52,57,48,54,51,54,50,53,57,54,54,54,52,57,56,53,56,55,54,49,56,50,50,49,50,50,53,50,50,53,53,49,50,52,56,54,55,54,52,53,51,51,32,32,32],[32,32,32,32,32,32,54,55,55,50,48,49,56,54,57,55,49,54,57,56,53,52,52,51,49,50,52,49,57,53,55,50,52,48,57,57,49,51,57,53,57,48,48,56,57,53,50,51,49,48,48,53,56,56,50,50,32,32,32],[32,32,32,32,32,32,57,53,53,52,56,50,53,53,51,48,48,50,54,51,53,50,48,55,56,49,53,51,50,50,57,54,55,57,54,50,52,57,52,56,49,54,52,49,57,53,51,56,54,56,50,49,56,55,55,52,32,32,32],[32,32,32,32,32,32,55,54,48,56,53,51,50,55,49,51,50,50,56,53,55,50,51,49,49,48,52,50,52,56,48,51,52,53,54,49,50,52,56,54,55,54,57,55,48,54,52,53,48,55,57,57,53,50,51,54,32,32,32],[32,32,32,32,32,32,51,55,55,55,52,50,52,50,53,51,53,52,49,49,50,57,49,54,56,52,50,55,54,56,54,53,53,51,56,57,50,54,50,48,53,48,50,52,57,49,48,51,50,54,53,55,50,57,54,55,32,32,32],[32,32,32,32,32,32,50,51,55,48,49,57,49,51,50,55,53,55,50,53,54,55,53,50,56,53,54,53,51,50,52,56,50,53,56,50,54,53,52,54,51,48,57,50,50,48,55,48,53,56,53,57,54,53,50,50,32,32,32],[32,32,32,32,32,32,50,57,55,57,56,56,54,48,50,55,50,50,53,56,51,51,49,57,49,51,49,50,54,51,55,53,49,52,55,51,52,49,57,57,52,56,56,57,53,51,52,55,54,53,55,52,53,53,48,49,32,32,32],[32,32,32,32,32,32,49,56,52,57,53,55,48,49,52,53,52,56,55,57,50,56,56,57,56,52,56,53,54,56,50,55,55,50,54,48,55,55,55,49,51,55,50,49,52,48,51,55,57,56,56,55,57,55,49,53,32,32,32],[32,32,32,32,32,32,51,56,50,57,56,50,48,51,55,56,51,48,51,49,52,55,51,53,50,55,55,50,49,53,56,48,51,52,56,49,52,52,53,49,51,52,57,49,51,55,51,50,50,54,54,53,49,51,56,49,32,32,32],[32,32,32,32,32,32,51,52,56,50,57,53,52,51,56,50,57,49,57,57,57,49,56,49,56,48,50,55,56,57,49,54,53,50,50,52,51,49,48,50,55,51,57,50,50,53,49,49,50,50,56,54,57,53,51,57,32,32,32],[32,32,32,32,32,32,52,48,57,53,55,57,53,51,48,54,54,52,48,53,50,51,50,54,51,50,53,51,56,48,52,52,49,48,48,48,53,57,54,53,52,57,51,57,49,53,57,56,55,57,53,57,51,54,51,53,32,32,32],[32,32,32,32,32,32,50,57,55,52,54,49,53,50,49,56,53,53,48,50,51,55,49,51,48,55,54,52,50,50,53,53,49,50,49,49,56,51,54,57,51,56,48,51,53,56,48,51,56,56,53,56,52,57,48,51,32,32,32],[32,32,32,32,32,32,52,49,54,57,56,49,49,54,50,50,50,48,55,50,57,55,55,49,56,54,49,53,56,50,51,54,54,55,56,52,50,52,54,56,57,49,53,55,57,57,51,53,51,50,57,54,49,57,50,50,32,32,32],[32,32,32,32,32,32,54,50,52,54,55,57,53,55,49,57,52,52,48,49,50,54,57,48,52,51,56,55,55,49,48,55,50,55,53,48,52,56,49,48,50,51,57,48,56,57,53,53,50,51,53,57,55,52,53,55,32,32,32],[32,32,32,32,32,32,50,51,49,56,57,55,48,54,55,55,50,53,52,55,57,49,53,48,54,49,53,48,53,53,48,52,57,53,51,57,50,50,57,55,57,53,51,48,57,48,49,49,50,57,57,54,55,53,49,57,32,32,32],[32,32,32,32,32,32,56,54,49,56,56,48,56,56,50,50,53,56,55,53,51,49,52,53,50,57,53,56,52,48,57,57,50,53,49,50,48,51,56,50,57,48,48,57,52,48,55,55,55,48,55,55,53,54,55,50,32,32,32],[32,32,32,32,32,32,49,49,51,48,54,55,51,57,55,48,56,51,48,52,55,50,52,52,56,51,56,49,54,53,51,51,56,55,51,53,48,50,51,52,48,56,52,53,54,52,55,48,53,56,48,55,55,51,48,56,32,32,32],[32,32,32,32,32,32,56,50,57,53,57,49,55,52,55,54,55,49,52,48,51,54,51,49,57,56,48,48,56,49,56,55,49,50,57,48,49,49,56,55,53,52,57,49,51,49,48,53,52,55,49,50,54,53,56,49,32,32,32],[32,32,32,32,32,32,57,55,54,50,51,51,51,49,48,52,52,56,49,56,51,56,54,50,54,57,53,49,53,52,53,54,51,51,52,57,50,54,51,54,54,53,55,50,56,57,55,53,54,51,52,48,48,53,48,48,32,32,32],[32,32,32,32,32,32,52,50,56,52,54,50,56,48,49,56,51,53,49,55,48,55,48,53,50,55,56,51,49,56,51,57,52,50,53,56,56,50,49,52,53,53,50,49,50,50,55,50,53,49,50,53,48,51,50,55,32,32,32],[32,32,32,32,32,32,53,53,49,50,49,54,48,51,53,52,54,57,56,49,50,48,48,53,56,49,55,54,50,49,54,53,50,49,50,56,50,55,54,53,50,55,53,49,54,57,49,50,57,54,56,57,55,55,56,57,32,32,32],[32,32,32,32,32,32,51,50,50,51,56,49,57,53,55,51,52,51,50,57,51,51,57,57,52,54,52,51,55,53,48,49,57,48,55,56,51,54,57,52,53,55,54,53,56,56,51,51,53,50,51,57,57,56,56,54,32,32,32],[32,32,32,32,32,32,55,53,53,48,54,49,54,52,57,54,53,49,56,52,55,55,53,49,56,48,55,51,56,49,54,56,56,51,55,56,54,49,48,57,49,53,50,55,51,53,55,57,50,57,55,48,49,51,51,55,32,32,32],[32,32,32,32,32,32,54,50,49,55,55,56,52,50,55,53,50,49,57,50,54,50,51,52,48,49,57,52,50,51,57,57,54,51,57,49,54,56,48,52,52,57,56,51,57,57,51,49,55,51,51,49,50,55,51,49,32,32,32],[32,32,32,32,32,32,51,50,57,50,52,49,56,53,55,48,55,49,52,55,51,52,57,53,54,54,57,49,54,54,55,52,54,56,55,54,51,52,54,54,48,57,49,53,48,51,53,57,49,52,54,55,55,53,48,52,32,32,32],[32,32,32,32,32,32,57,57,53,49,56,54,55,49,52,51,48,50,51,53,50,49,57,54,50,56,56,57,52,56,57,48,49,48,50,52,50,51,51,50,53,49,49,54,57,49,51,54,49,57,54,50,54,54,50,50,32,32,32],[32,32,32,32,32,32,55,51,50,54,55,52,54,48,56,48,48,53,57,49,53,52,55,52,55,49,56,51,48,55,57,56,51,57,50,56,54,56,53,51,53,50,48,54,57,52,54,57,52,52,53,52,48,55,50,52,32,32,32],[32,32,32,32,32,32,55,54,56,52,49,56,50,50,53,50,52,54,55,52,52,49,55,49,54,49,53,49,52,48,51,54,52,50,55,57,56,50,50,55,51,51,52,56,48,53,53,53,53,54,50,49,52,56,49,56,32,32,32],[32,32,32,32,32,32,57,55,49,52,50,54,49,55,57,49,48,51,52,50,53,57,56,54,52,55,50,48,52,53,49,54,56,57,51,57,56,57,52,50,50,49,55,57,56,50,54,48,56,56,48,55,54,56,53,50,32,32,32],[32,32,32,32,32,32,56,55,55,56,51,54,52,54,49,56,50,55,57,57,51,52,54,51,49,51,55,54,55,55,53,52,51,48,55,56,48,57,51,54,51,51,51,51,48,49,56,57,56,50,54,52,50,48,57,48,32,32,32],[32,32,32,32,32,32,49,48,56,52,56,56,48,50,53,50,49,54,55,52,54,55,48,56,56,51,50,49,53,49,50,48,49,56,53,56,56,51,53,52,51,50,50,51,56,49,50,56,55,54,57,53,50,55,56,54,32,32,32],[32,32,32,32,32,32,55,49,51,50,57,54,49,50,52,55,52,55,56,50,52,54,52,53,51,56,54,51,54,57,57,51,48,48,57,48,52,57,51,49,48,51,54,51,54,49,57,55,54,51,56,55,56,48,51,57,32,32,32],[32,32,32,32,32,32,54,50,49,56,52,48,55,51,53,55,50,51,57,57,55,57,52,50,50,51,52,48,54,50,51,53,51,57,51,56,48,56,51,51,57,54,53,49,51,50,55,52,48,56,48,49,49,49,49,54,32,32,32],[32,32,32,32,32,32,54,54,54,50,55,56,57,49,57,56,49,52,56,56,48,56,55,55,57,55,57,52,49,56,55,54,56,55,54,49,52,52,50,51,48,48,51,48,57,56,52,52,57,48,56,53,49,52,49,49,32,32,32],[32,32,32,32,32,32,54,48,54,54,49,56,50,54,50,57,51,54,56,50,56,51,54,55,54,52,55,52,52,55,55,57,50,51,57,49,56,48,51,51,53,49,49,48,57,56,57,48,54,57,55,57,48,55,49,52,32,32,32],[32,32,32,32,32,32,56,53,55,56,54,57,52,52,48,56,57,53,53,50,57,57,48,54,53,51,54,52,48,52,52,55,52,50,53,53,55,54,48,56,51,54,53,57,57,55,54,54,52,53,55,57,53,48,57,54,32,32,32],[32,32,32,32,32,32,54,54,48,50,52,51,57,54,52,48,57,57,48,53,51,56,57,54,48,55,49,50,48,49,57,56,50,49,57,57,55,54,48,52,55,53,57,57,52,57,48,49,57,55,50,51,48,50,57,55,32,32,32],[32,32,32,32,32,32,54,52,57,49,51,57,56,50,54,56,48,48,51,50,57,55,51,49,53,54,48,51,55,49,50,48,48,52,49,51,55,55,57,48,51,55,56,53,53,54,54,48,56,53,48,56,57,50,53,50,32,32,32],[32,32,32,32,32,32,49,54,55,51,48,57,51,57,51,49,57,56,55,50,55,53,48,50,55,53,52,54,56,57,48,54,57,48,51,55,48,55,53,51,57,52,49,51,48,52,50,54,53,50,51,49,53,48,49,49,32,32,32],[32,32,32,32,32,32,57,52,56,48,57,51,55,55,50,52,53,48,52,56,55,57,53,49,53,48,57,53,52,49,48,48,57,50,49,54,52,53,56,54,51,55,53,52,55,49,48,53,57,56,52,51,54,55,57,49,32,32,32],[32,32,32,32,32,32,55,56,54,51,57,49,54,55,48,50,49,49,56,55,52,57,50,52,51,49,57,57,53,55,48,48,54,52,49,57,49,55,57,54,57,55,55,55,53,57,57,48,50,56,51,48,48,54,57,57,32,32,32],[32,32,32,32,32,32,49,53,51,54,56,55,49,51,55,49,49,57,51,54,54,49,52,57,53,50,56,49,49,51,48,53,56,55,54,51,56,48,50,55,56,52,49,48,55,53,52,52,52,57,55,51,51,48,55,56,32,32,32],[32,32,32,32,32,32,52,48,55,56,57,57,50,51,49,49,53,53,51,53,53,54,50,53,54,49,49,52,50,51,50,50,52,50,51,50,53,53,48,51,51,54,56,53,52,52,50,52,56,56,57,49,55,51,53,51,32,32,32],[32,32,32,32,32,32,52,52,56,56,57,57,49,49,53,48,49,52,52,48,54,52,56,48,50,48,51,54,57,48,54,56,48,54,51,57,54,48,54,55,50,51,50,50,49,57,51,50,48,52,49,52,57,53,51,53,32,32,32],[32,32,32,32,32,32,52,49,53,48,51,49,50,56,56,56,48,51,51,57,53,51,54,48,53,51,50,57,57,51,52,48,51,54,56,48,48,54,57,55,55,55,49,48,54,53,48,53,54,54,54,51,49,57,53,52,32,32,32],[32,32,32,32,32,32,56,49,50,51,52,56,56,48,54,55,51,50,49,48,49,52,54,55,51,57,48,53,56,53,54,56,53,53,55,57,51,52,53,56,49,52,48,51,54,50,55,56,50,50,55,48,51,50,56,48,32,32,32],[32,32,32,32,32,32,56,50,54,49,54,53,55,48,55,55,51,57,52,56,51,50,55,53,57,50,50,51,50,56,52,53,57,52,49,55,48,54,53,50,53,48,57,52,53,49,50,51,50,53,50,51,48,54,48,56,32,32,32],[32,32,32,32,32,32,50,50,57,49,56,56,48,50,48,53,56,55,55,55,51,49,57,55,49,57,56,51,57,52,53,48,49,56,48,56,56,56,48,55,50,52,50,57,54,54,49,57,56,48,56,49,49,49,57,55,32,32,32],[32,32,32,32,32,32,55,55,49,53,56,53,52,50,53,48,50,48,49,54,53,52,53,48,57,48,52,49,51,50,52,53,56,48,57,55,56,54,56,56,50,55,55,56,57,52,56,55,50,49,56,53,57,54,49,55,32,32,32],[32,32,32,32,32,32,55,50,49,48,55,56,51,56,52,51,53,48,54,57,49,56,54,49,53,53,52,51,53,54,54,50,56,56,52,48,54,50,50,53,55,52,55,51,54,57,50,50,56,52,53,48,57,53,49,54,32,32,32],[32,32,32,32,32,32,50,48,56,52,57,54,48,51,57,56,48,49,51,52,48,48,49,55,50,51,57,51,48,54,55,49,54,54,54,56,50,51,53,53,53,50,52,53,50,53,50,56,48,52,54,48,57,55,50,50,32,32,32],[35,32,32,32,32,32,53,51,53,48,51,53,51,52,50,50,54,52,55,50,53,50,52,50,53,48,56,55,52,48,53,52,48,55,53,53,57,49,55,56,57,55,56,49,50,54,52,51,51,48,51,51,49,54,57,48,32,32,32],[61,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[32,32,32,32,32,32,32,32,32,118,95,118,35,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,60,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,60,49,60,32,32,32,32,32,32,32,32],[62,53,49,48,112,34,100,34,50,48,112,62,34,48,34,49,48,103,50,48,103,112,49,48,103,49,45,58,49,48,112,35,94,95,53,49,48,112,50,48,103,49,45,58,50,48,112,35,94,95,94,32,32,32,32,32,32,32,32],[118,32,32,32,32,32,32,32,36,60,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[62,34,55,34,49,48,112,118,62,49,48,103,50,48,103,103,34,32,34,45,33,35,118,95,32,32,32,32,32,32,32,62,49,48,103,50,48,103,103,34,48,34,45,48,48,103,43,48,48,112,32,118,32,32,32,32,32,32,32],[118,51,48,112,48,50,49,60,32,62,49,48,103,49,45,49,48,112,53,53,43,47,48,48,112,32,32,32,118,32,32,124,45,34,32,34,103,103,48,50,103,48,49,112,48,50,43,49,103,48,50,60,32,32,32,32,32,32,32],[62,48,112,48,58,58,112,32,94,94,112,48,50,49,112,103,48,50,103,48,49,43,34,48,34,37,43,53,53,58,60,62,48,118,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[32,32,32,32,32,32,32,32,94,32,32,32,32,32,32,32,32,32,32,32,32,32,34,35,32,32,32,36,60,32,94,103,48,60,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[118,32,32,32,32,32,32,32,32,32,32,112,48,50,34,101,34,112,48,49,48,36,60,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[62,49,48,103,49,43,58,49,48,112,50,48,103,103,34,48,34,45,33,35,118,95,53,53,43,48,48,112,62,48,48,103,58,49,45,48,48,112,33,35,64,95,53,52,43,48,48,103,45,49,48,103,43,50,48,103,103,44,118],[94,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,60,32,32,32,32,32,32,32,94,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,60]];
def gr(x,y):
    if(x>=0 and y>=0 and x<59 and y<113):
        return g[y][x];
    return 0;
def gw(x,y,v):
    if(x>=0 and y>=0 and x<59 and y<113):
        g[y][x]=v;
def rd():
    return bool(random.getrandbits(1))
def td(a,b):
    return bool(random.getrandbits(1))
def td(a,b):
    return ((0)if(b==0)else(a//b))
def tm(a,b):
    return ((0)if(b==0)else(a%b))
s=[]
def sp():
    global s
    if (len(s) == 0):
        return 0
    return s.pop()
def sa(v):
    global s
    s.append(v)
def sr():
    global s
    if (len(s) == 0):
        return 0
    return s[-1]
def _0():
    return (1)if(sp()!=0)else(9)
def _1():
    return (11)if(sp()!=0)else(8)
def _2():
    return (13)if(sp()!=0)else(14)
def _3():
    return (17)if(sp()!=0)else(16)
def _4():
    return (18)if(sp()!=0)else(19)
def _5():
    return (1)if(sp()!=0)else(10)
def _6():
    return (12)if((0)if(((gr(gr(1,0),gr(2,0)))-(32))!=0)else(1))else(18)
def _7():
    gw(1,0,5)
    gw(2,0,100)
    return 8
def _8():
    gw(gr(1,0),gr(2,0),48)
    sa((gr(1,0))-(1))
    gw(1,0,(gr(1,0))-(1))
    return 0
def _9():
    gw(1,0,5)
    sa((gr(2,0))-(1))
    gw(2,0,(gr(2,0))-(1))
    return 5
def _10():
    sa(1)
    return 1
def _11():
    gw(1,0,55)
    gw(2,0,1)
    gw(3,0,0)
    gw(0,0,0)
    return 6
def _12():
    gw(1,0,0)
    gw(2,0,101)
    return 13
def _13():
    sa((gr(1,0))+(1))
    gw(1,0,(gr(1,0))+(1))
    sa(gr(2,0))
    v0=sp()
    sa(gr(sp(),v0))
    sa(48)
    v0=sp()
    sa(sp()-v0)
    sa((0)if(sp()!=0)else(1))
    return 2
def _14():
    gw(0,0,10)
    return 15
def _15():
    sa(gr(0,0))
    gw(0,0,(gr(0,0))-(1))
    sa((0)if(sp()!=0)else(1))
    return 3
def _16():
    print(chr(gr(((9)-(gr(0,0)))+(gr(1,0)),gr(2,0))),end="",flush=True)
    return 15
def _17():
    return 20
def _18():
    gw(0,0,((gr(gr(1,0),gr(2,0)))-(48))+(gr(0,0)))
    gw(2,0,(gr(2,0))+(1))
    sa((gr(gr(1,0),gr(2,0)))-(32))
    return 4
def _19():
    sa(gr(0,0))
    gw(gr(1,0),gr(2,0),(tm(gr(0,0),10))+(48))
    gw(2,0,1)
    gw(1,0,(gr(1,0))-(1))
    sa(10)
    v0=sp()
    sa(td(sp(),v0))
    gw(0,0,sp())
    return 6
m=[_0,_1,_2,_3,_4,_5,_6,_7,_8,_9,_10,_11,_12,_13,_14,_15,_16,_17,_18,_19]
c=7
while c<20:
    c=m[c]()