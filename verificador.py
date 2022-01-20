import re

def isDui(input):
    # Acepta entrada tanto con guión como sin guión
    if re.match("^\d{8}-\d$", input) or re.match("^\d{9}$", input):
        # El primer número a la izquierda está en la posición 9; el segundo, 8, el tercero, 7; etc...
        posicion = 9
        sumaMultiplicaciones = 0
        # Se multiplican los primeros 8 números por su posición y se suman los resultados
        for i in range(0, 8):
            sumaMultiplicaciones += int(input[i]) * posicion
            posicion-= 1
        # Se calcula el MOD 10 de la suma de las multiplicaciones (el remanante)
        remanente = sumaMultiplicaciones % 10
        # El digito verificador es 10 menos el remanente
        digitoVerificador = 10-remanente
        # Si el digito verificador obtenido es igual que el del DUI ingresado, el DUI es válido
        if int(input[len(input)-1]) == digitoVerificador:
            # DUI válido
            return True
        else:
            # DUI inválido
            return False
    else:
        # Formato de DUI inválido
        return False
