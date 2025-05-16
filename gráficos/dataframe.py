import pandas as pd

# En este documentos está contenido el dataframe sobre el cual están desarrollados los gráficos

# Datos
data = {
    'Producto' : ['borrador', 'cuaderno', 'goma', 'lápiz'],
    'Costo_de_producción' : [1, 5, 3, 1],
    'Precio_de_venta' : [1.5, 7, 5, 2],
    'Cantidad_vendida' : [50, 100, 30, 75]
}

# Crear dataframe a partir de data
df = pd.DataFrame(data)

# Visualizar
print(df)

