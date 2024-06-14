from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

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

df.hist(bins=30, figsize=(20, 15))
plt.show()

plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()

sns.pairplot(df[['Taxa_Crim', 'Z_Residencial', 'Propor_Comercial', 'Proxi_Rio', 
              'Concentracao_NOX', 'Media_Quartos', 'Propor_UN_Antigas', 'Distancia_Centros', 
              'Acessi_Rodovias', 'Taxa_Imposto', 'Propor_Aluno_Professor', 'Propor_Negros', 
              'Propor_Status_Baixo', 'Valor_Medio']])
plt.show()
                                    # ------------------------------------------------------------------------------------------------------------------------------
X = df.drop('Valor_Medio', axis=1)  # ------------------------------- Substituir o 'Valor_Medio' pela variável alvo :D ---------------------------------------------
y = df['Valor_Medio']               # ------------------------------------------------------------------------------------------------------------------------------

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
