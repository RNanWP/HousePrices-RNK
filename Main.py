import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('boston.csv')

print(df.head())

print(df.info())

print(df.describe())

print(df.isnull().sum())

# Tratar valores ausentes (Exemplo: Remover colunas com muitos valores ausentes)
# df = df.drop(columns=['coluna_com_muitos_na'])  # Descomente e substitua pela coluna real

# Preencher valores ausentes com a média (Exemplo: Preencher uma coluna específica)
# df['coluna_com_na'] = df['coluna_com_na'].fillna(df['coluna_com_na'].mean())  # Descomente e substitua pela coluna real

df = pd.get_dummies(df, drop_first=True)

df.hist(bins=30, figsize=(20, 15))
plt.show()

# Gráfico de correlação
plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()

# Gráficos de dispersão para algumas variáveis-chave (Substitua 'var1', 'var2', etc. pelas variáveis relevantes)
# sns.pairplot(df[['var1', 'var2', 'var3', 'price']])  # Descomente e substitua pelas variáveis reais
# plt.show()

# Separar variáveis previsoras (X) e alvo (y)
X = df.drop('price', axis=1)  # Substitua 'price' pela sua variável alvo
y = df['price']

# Dividir o conjunto de dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo de regressão linear
model = LinearRegression()
model.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = model.predict(X_test)

# Avaliar o desempenho do modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
print(f'R² Score: {r2}')

# Interpretação dos coeficientes do modelo
coefficients = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
print(coefficients)
