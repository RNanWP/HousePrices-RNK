import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import tkinter as tk
from tkinter import ttk

df = pd.read_csv('boston.csv')

df.columns = ['Taxa_Crim', 'Z_Residencial', 'Propor_Comercial', 'Proxi_Rio', 
              'Concentracao_NOX', 'Media_Quartos', 'Propor_UN_Antigas', 'Distancia_Centros', 
              'Acessi_Rodovias', 'Taxa_Imposto', 'Propor_Aluno_Professor', 'Propor_Negros', 
              'Propor_Status_Baixo', 'Valor_Medio']

print(df.head())

print(df.info())

print(df.describe())

print(df.isnull().sum())

df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.fillna(df.mean(), inplace=True)

df.hist(bins=30, figsize=(18, 12))
plt.show()

plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()
                                    #-----------------------------------------------------------------------------------
X = df.drop('Valor_Medio', axis=1)  #-------------------Substituir o 'Valor_Medio' pela variável alvo-------------------
y = df['Valor_Medio']               #-----------------------------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Erro Quadrático Médio: {mse}')
print(f'Coeficiente de Determinação R²: {r2}')

coeficientes = pd.DataFrame(modelo.coef_, X.columns, columns=['Coeficiente'])
print(coeficientes)

#-------------------------------------GRÁFICO INTERATIVO----------------------------------------------#

def plot_scatter():
    x_var = combo_x.get()
    y_var = combo_y.get()
    
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=df[x_var], y=df[y_var])
    plt.xlabel(x_var)
    plt.ylabel(y_var)
    plt.title(f'Gráfico de Dispersão de {x_var} e {y_var}')
    plt.show()

root = tk.Tk()
root.title('Gráfico de Dispersão Interativo')

label_x = ttk.Label(root, text='Selecione a Variável X:')
label_y = ttk.Label(root, text='Selecione a Variável Y:')
combo_x = ttk.Combobox(root, values=df.columns.tolist())
combo_y = ttk.Combobox(root, values=df.columns.tolist())

button_plot = ttk.Button(root, text='Ver Gráfico', command=plot_scatter)

label_x.grid(row=0, column=0, padx=10, pady=5, sticky='w')
combo_x.grid(row=0, column=1, padx=10, pady=5)
label_y.grid(row=1, column=0, padx=10, pady=5, sticky='w')
combo_y.grid(row=1, column=1, padx=10, pady=5)
button_plot.grid(row=2, columnspan=2, padx=10, pady=10)

root.mainloop()