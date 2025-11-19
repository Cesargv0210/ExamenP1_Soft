def Qo (Qm, Pr, Pwf):
    """
    Función para calcular el Caudal de petróleo en stb/d

    Qm: Caudal máximo, stb/d
    Pr: Presión de reservorio, psi
    Pwf: Presión de fondo fluyente, psi

    Return
    Qo: Caudal de petróleo, stb/d
    """
    caudal=(1-(0.2*Pwf/Pr)-(0.8*((Pwf/Pr)**2)))
    return caudal
