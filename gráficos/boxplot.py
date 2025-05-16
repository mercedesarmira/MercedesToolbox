""" Boxplot con Seaborn

Boxplot: gráfico que presenta un resumen estadístico, mínimo, Q1, mediana, Q3 y máximo; detecta valores atípicos"""

from dataframe import df
import seaborn as sns
import matplotlib.pyplot as plt

# Crear gráfico
sns.boxplot(data=df, x="Producto", y="Cantidad_vendida")

# Personalizar
plt.title("Cantidad vendida por producto")

# Mostrar
plt.show