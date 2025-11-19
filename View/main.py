#%% #importamos las librerias
from Model.functions import Qo
import numpy as np
from scipy.stats import norm, lognorm, expon, triang, uniform
import matplotlib.pyplot as plt

#%% Probamos la función
Qm = 250  #stb/d
Pr = 2400  #psi
Pwf = [2400, 2000, 1500, 500, 0]

Caudal_Petro = Qo(Qm, Pr, Pwf)
print(Caudal_Petro)
