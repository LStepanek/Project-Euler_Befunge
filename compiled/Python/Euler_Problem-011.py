# compiled with BefunCompile v1.0.1 (c) 2015
# execute with at least Python3
from random import randint
g=[[118,32,32,32,32,32,32,32,32,32,32,32,32,32,118,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,60,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[62,34,52,34,50,47,58,42,49,45,48,48,112,32,62,32,48,48,48,103,58,32,34,52,34,50,47,32,37,34,63,34,43,92,32,34,52,34,50,47,32,47,49,43,32,112,32,32,48,48,103,58,49,45,48,48,112,32,32,35,94,95,118,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[32,48,56,32,48,50,32,50,50,32,57,55,32,51,56,32,49,53,32,48,48,32,52,48,32,48,48,32,55,53,32,48,52,32,48,53,32,48,55,32,55,56,32,53,50,32,49,50,32,53,48,32,55,55,32,57,49,32,48,56,32,124,32,43,43,43,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,43,43,43,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[32,52,57,32,52,57,32,57,57,32,52,48,32,49,55,32,56,49,32,49,56,32,53,55,32,54,48,32,56,55,32,49,55,32,52,48,32,57,56,32,52,51,32,54,57,32,52,56,32,48,52,32,53,54,32,54,50,32,48,48,32,124,32,43,43,43,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,43,43,43,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[32,56,49,32,52,57,32,51,49,32,55,51,32,53,53,32,55,57,32,49,52,32,50,57,32,57,51,32,55,49,32,52,48,32,54,55,32,53,51,32,56,56,32,51,48,32,48,51,32,52,57,32,49,51,32,51,54,32,54,53,32,124,32,43,43,43,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,43,43,43,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[32,53,50,32,55,48,32,57,53,32,50,51,32,48,52,32,54,48,32,49,49,32,52,50,32,54,57,32,50,52,32,54,56,32,53,54,32,48,49,32,51,50,32,53,54,32,55,49,32,51,55,32,48,50,32,51,54,32,57,49,32,124,32,43,43,43,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,43,43,43,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[32,50,50,32,51,49,32,49,54,32,55,49,32,53,49,32,54,55,32,54,51,32,56,57,32,52,49,32,57,50,32,51,54,32,53,52,32,50,50,32,52,48,32,52,48,32,50,56,32,54,54,32,51,51,32,49,51,32,56,48,32,124,32,43,43,43,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,43,43,43,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[32,50,52,32,52,55,32,51,50,32,54,48,32,57,57,32,48,51,32,52,53,32,48,50,32,52,52,32,55,53,32,51,51,32,53,51,32,55,56,32,51,54,32,56,52,32,50,48,32,51,53,32,49,55,32,49,50,32,53,48,32,124,32,43,43,43,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,43,43,43,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[32,51,50,32,57,56,32,56,49,32,50,56,32,54,52,32,50,51,32,54,55,32,49,48,32,50,54,32,51,56,32,52,48,32,54,55,32,53,57,32,53,52,32,55,48,32,54,54,32,49,56,32,51,56,32,54,52,32,55,48,32,124,32,43,43,43,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,43,43,43,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[32,54,55,32,50,54,32,50,48,32,54,56,32,48,50,32,54,50,32,49,50,32,50,48,32,57,53,32,54,51,32,57,52,32,51,57,32,54,51,32,48,56,32,52,48,32,57,49,32,54,54,32,52,57,32,57,52,32,50,49,32,124,32,43,43,43,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,43,43,43,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[32,50,52,32,53,53,32,53,56,32,48,53,32,54,54,32,55,51,32,57,57,32,50,54,32,57,55,32,49,55,32,55,56,32,55,56,32,57,54,32,56,51,32,49,52,32,56,56,32,51,52,32,56,57,32,54,51,32,55,50,32,124,32,43,43,43,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,43,43,43,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[32,50,49,32,51,54,32,50,51,32,48,57,32,55,53,32,48,48,32,55,54,32,52,52,32,50,48,32,52,53,32,51,53,32,49,52,32,48,48,32,54,49,32,51,51,32,57,55,32,51,52,32,51,49,32,51,51,32,57,53,32,124,32,43,43,43,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,43,43,43,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[32,55,56,32,49,55,32,53,51,32,50,56,32,50,50,32,55,53,32,51,49,32,54,55,32,49,53,32,57,52,32,48,51,32,56,48,32,48,52,32,54,50,32,49,54,32,49,52,32,48,57,32,53,51,32,53,54,32,57,50,32,124,32,43,43,43,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,43,43,43,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[32,49,54,32,51,57,32,48,53,32,52,50,32,57,54,32,51,53,32,51,49,32,52,55,32,53,53,32,53,56,32,56,56,32,50,52,32,48,48,32,49,55,32,53,52,32,50,52,32,51,54,32,50,57,32,56,53,32,53,55,32,124,32,43,43,43,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,43,43,43,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[32,56,54,32,53,54,32,48,48,32,52,56,32,51,53,32,55,49,32,56,57,32,48,55,32,48,53,32,52,52,32,52,52,32,51,55,32,52,52,32,54,48,32,50,49,32,53,56,32,53,49,32,53,52,32,49,55,32,53,56,32,124,32,43,43,43,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,43,43,43,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[32,49,57,32,56,48,32,56,49,32,54,56,32,48,53,32,57,52,32,52,55,32,54,57,32,50,56,32,55,51,32,57,50,32,49,51,32,56,54,32,53,50,32,49,55,32,55,55,32,48,52,32,56,57,32,53,53,32,52,48,32,124,32,43,43,43,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,43,43,43,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[32,48,52,32,53,50,32,48,56,32,56,51,32,57,55,32,51,53,32,57,57,32,49,54,32,48,55,32,57,55,32,53,55,32,51,50,32,49,54,32,50,54,32,50,54,32,55,57,32,51,51,32,50,55,32,57,56,32,54,54,32,124,32,43,43,43,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,43,43,43,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[32,56,56,32,51,54,32,54,56,32,56,55,32,53,55,32,54,50,32,50,48,32,55,50,32,48,51,32,52,54,32,51,51,32,54,55,32,52,54,32,53,53,32,49,50,32,51,50,32,54,51,32,57,51,32,53,51,32,54,57,32,124,32,43,43,43,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,43,43,43,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[32,48,52,32,52,50,32,49,54,32,55,51,32,51,56,32,50,53,32,51,57,32,49,49,32,50,52,32,57,52,32,55,50,32,49,56,32,48,56,32,52,54,32,50,57,32,51,50,32,52,48,32,54,50,32,55,54,32,51,54,32,124,32,43,43,43,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,43,43,43,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[32,50,48,32,54,57,32,51,54,32,52,49,32,55,50,32,51,48,32,50,51,32,56,56,32,51,52,32,54,50,32,57,57,32,54,57,32,56,50,32,54,55,32,53,57,32,56,53,32,55,52,32,48,52,32,51,54,32,49,54,32,124,32,43,43,43,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,43,43,43,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[32,50,48,32,55,51,32,51,53,32,50,57,32,55,56,32,51,49,32,57,48,32,48,49,32,55,52,32,51,49,32,52,57,32,55,49,32,52,56,32,56,54,32,56,49,32,49,54,32,50,51,32,53,55,32,48,53,32,53,52,32,124,32,43,43,43,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,43,43,43,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[32,48,49,32,55,48,32,53,52,32,55,49,32,56,51,32,53,49,32,53,52,32,54,57,32,49,54,32,57,50,32,51,51,32,52,56,32,54,49,32,52,51,32,53,50,32,48,49,32,56,57,32,49,57,32,54,55,32,52,56,32,124,32,43,43,43,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,43,43,43,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[118,112,48,48,45,49,42,58,42,52,53,32,32,32,32,112,49,43,43,49,53,53,48,112,48,43,43,49,53,53,49,112,49,43,53,53,45,49,48,112,48,43,53,53,49,112,49,57,45,49,48,112,48,57,48,32,32,32,112,48,49,48,60,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,62,49,48,112,118,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[62,48,48,103,58,53,52,42,37,51,42,49,43,92,53,52,42,47,52,43,103,34,48,34,45,53,50,42,42,48,48,103,58,53,52,42,37,51,42,50,43,92,53,52,42,47,52,43,103,34,48,34,45,43,48,48,103,58,53,52,42,37,118,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,62,36,62,32,32,32,32,32,118,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[124,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,112,48,48,45,49,58,103,48,48,112,43,52,47,42,52,53,92,43,34,66,34,60,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,94,95,94,35,96,103,48,49,58,60,32,32,32,32,32,118,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,60,32,32,32,32,32,32,32],[62,53,52,42,58,42,49,45,48,48,112,62,50,50,48,112,62,50,48,103,57,43,58,48,103,51,48,112,49,103,52,48,112,48,48,103,58,53,52,42,37,53,48,112,53,52,42,47,54,48,112,53,48,103,34,66,34,43,54,48,103,52,43,103,53,48,103,51,48,103,43,53,48,112,54,48,103,52,48,103,43,54,48,112,62,53,48,103,34,66,34,43,54,48,103,52,43,103,53,48,103,51,48,103,43,53,48,112,54,48,103,52,48,103,43,54,48,112,118,32,62,50,48,103,58,49,45,50,48,112,35,118,95,48,48,103,58,49,45,48,48,112,35,94,95,49,48,103,46,32,64],[32,32,32,32,32,32,32,32,32,32,32,94,32,32,32,95,94,35,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,60,118,112,48,54,43,103,48,52,103,48,54,112,48,53,43,103,48,51,103,48,53,103,43,52,103,48,54,43,34,66,34,103,48,53,60,94,32,60,32,32,118,32,32,32,32,32,48,60,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,62,53,48,103,34,66,34,43,54,48,103,52,43,103,53,48,103,51,48,103,43,53,48,112,54,48,103,52,48,103,43,54,48,112,42,42,42,94,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,94,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,60,60,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32]];
def gr(x,y):
    if(x>=0 and y>=0 and x<151 and y<31):
        return g[y][x];
    return 0;
def gw(x,y,v):
    if(x>=0 and y>=0 and x<151 and y<31):
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
    return (7)if(sp()!=0)else(8)
def _1():
    return (9)if(sp()!=0)else(10)
def _2():
    return (13)if(sp()!=0)else(19)
def _3():
    return (18)if(sp()!=0)else(15)
def _4():
    return (11)if(sp()!=0)else(12)
def _5():
    return (17)if(sp()!=0)else(16)
def _6():
    gw(0,0,675)
    return 7
def _7():
    gw((tm(gr(0,0),26))+(63),(td(gr(0,0),26))+(1),0)
    sa(gr(0,0))
    gw(0,0,(gr(0,0))-(1))
    return 0
def _8():
    gw(1,0,0)
    gw(9,0,0)
    gw(9,1,-1)
    gw(10,0,1)
    gw(10,1,-1)
    gw(11,0,1)
    gw(11,1,0)
    gw(0,0,399)
    return 9
def _9():
    gw((tm(gr(0,0),20))+(66),(td(gr(0,0),20))+(4),(((gr(((tm(gr(0,0),20))*(3))+(1),(td(gr(0,0),20))+(4)))-(48))*(10))+((gr(((tm(gr(0,0),20))*(3))+(2),(td(gr(0,0),20))+(4)))-(48)))
    sa(gr(0,0))
    gw(0,0,(gr(0,0))-(1))
    return 1
def _10():
    gw(0,0,399)
    return 11
def _11():
    gw(2,0,2)
    return 12
def _12():
    sa((gr(2,0))+(9))
    gw(3,0,gr((gr(2,0))+(9),0))
    sa(1)
    v0=sp()
    sa(gr(sp(),v0))
    gw(4,0,sp())
    sa(gr(0,0))
    gw(5,0,tm(gr(0,0),20))
    sa(20)
    v0=sp()
    sa(td(sp(),v0))
    gw(6,0,sp())
    sa(gr((gr(5,0))+(66),(gr(6,0))+(4)))
    gw(5,0,(gr(5,0))+(gr(3,0)))
    gw(6,0,(gr(6,0))+(gr(4,0)))
    sa(gr((gr(5,0))+(66),(gr(6,0))+(4)))
    gw(5,0,(gr(5,0))+(gr(3,0)))
    gw(6,0,(gr(6,0))+(gr(4,0)))
    sa(gr((gr(5,0))+(66),(gr(6,0))+(4)))
    gw(5,0,(gr(5,0))+(gr(3,0)))
    gw(6,0,(gr(6,0))+(gr(4,0)))
    sa(gr((gr(5,0))+(66),(gr(6,0))+(4)))
    gw(5,0,(gr(5,0))+(gr(3,0)))
    gw(6,0,(gr(6,0))+(gr(4,0)))
    sa(sp()*sp());
    sa(sp()*sp());
    sa(sp()*sp());
    sa(sr())
    sa(gr(1,0))
    v0=sp()
    sa((1)if(sp()>v0)else(0))
    return 2
def _13():
    gw(1,0,sp())
    return 14
def _14():
    sa(gr(2,0))
    gw(2,0,(gr(2,0))-(1))
    return 3
def _15():
    sa(gr(0,0))
    gw(0,0,(gr(0,0))-(1))
    return 5
def _16():
    print(gr(1,0),end="",flush=True)
    return 20
def _17():
    sa(1)
    return 4
def _18():
    sa(0)
    return 4
def _19():
    sp()
    return 14
m=[_0,_1,_2,_3,_4,_5,_6,_7,_8,_9,_10,_11,_12,_13,_14,_15,_16,_17,_18,_19]
c=6
while c<20:
    c=m[c]()