# ESCAREÑO COVARRUBIAS EMANUEL INNI 
import pandas as pd
from scipy.stats import chi2_contingency

# Leer el archivo CSV
df = pd.read_csv('tallas.csv')

# Pedir al usuario que ingrese el nombre de las columnas a comparar
print("Test de Chi-cuadrada")
print("|weight | age | height | size |")
print("")
col1 = input("Ingresa el nombre de la primera columna: ")
col2 = input("Ingresa el nombre de la segunda columna: ")

# Obtener las frecuencias de los valores en ambas columnas
tabla_cruzada = pd.crosstab(df[col1], df[col2])

# Realizar el test de chi-cuadrada
chi2, p, dof, expected = chi2_contingency(tabla_cruzada)

# Imprimir los resultados
print("Test de Chi-cuadrada")
print("Chi2: ", chi2)
print("p-value: ", p)
print("Grados de libertad: ", dof)
print("Expected: ", expected)

