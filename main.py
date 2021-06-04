from verificador import isDui

# Ejemplo de uso, la función está en verificador.py
dui = input("Ingrese el número de DUI: ")
if isDui(dui):
    print("El DUI ingresado es válido.")
else:
    print("El DUI ingresado no es válido.")