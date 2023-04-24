import pandas as pd
from scipy.stats import chi2_contingency

# Leer el archivo csv
df = pd.read_csv('tallas.csv')

# Pedir al usuario que ingrese el nombre de las columnas a comparar
print("Test de Chi-cuadrada")
print("|weight | age | height | size |")
print("")
col1 = input("Ingresa el nombre de la primera columna: ")
col2 = input("Ingresa el nombre de la segunda columna: ")

# Crear la tabla de contingencia
contingency_table = pd.crosstab(df[col1], df[col2])

# Calcular el coeficiente de Tschuprow
chi2, p_value, dof, expected = chi2_contingency(contingency_table)
tschuprow = (chi2 / (chi2 + len(df))) ** 0.5

# Imprimir el resultado
print("El coeficiente de Tschuprow entre las columnas {} y {} es: {}".format(col1, col2, tschuprow))
