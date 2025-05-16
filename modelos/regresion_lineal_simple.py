from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
 
 df = pd.DataFrame({}) # <---- datos

X = df[[]] # <---- nombre de columna
y = df[[]] # <---- nombre de columna

# Definimos datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Configurar modelo
modelo = LinearRegression()

# Entrenar
modelo.fit(X_train, y_train)

# Predicciones
y_pred = modelo.predict(X_test)