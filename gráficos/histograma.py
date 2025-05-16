""" Histograma con Matplotlib

Histograma: gráfico que representa la distribución de una variable dividiéndola en intervalos"""

from dataframe import df
import matplotlib.pyplot as plt

# Crear gráfico
df["Cantidad_vendida"].hist(bins=20)

# Personalizar
plt.title("Distribución de Cantidad Vendida por producto")
plt.xlabel("Cantidad Vendida")
plt.ylabel("Frecuencia")
plt.show()