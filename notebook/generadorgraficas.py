import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


dataframeAsistencia=pd.read_csv("./data/asistencia_estudiantes_completo.csv")

#Graficando

#Grafica de barras
colors=["#c25e68","#a7587b","#835783","#5e557e","#3f506e","#2f4858"]

plt.figure(figsize=(8,5))
sns.countplot(x='estado',data=dataframeAsistencia,palette=colors)
plt.title("Cantidad de registros por estado de asistencia")
plt.xlabel("Esatdo de asistencia")
plt.ylabel("Cantidad de registros")
plt.tight_layout()
plt.show()



#Grafica de torta
#Mostrar proporciones entre dos columnas del dataframe (proporcion de estudiantes  x medio de transporte)
conteoMedioTransporte=dataframeAsistencia['medio_transporte'].value_counts()

plt.figure(figsize=(5,5))
plt.pie(
    conteoMedioTransporte,
    labels=conteoMedioTransporte.index,
    autopct='%1.1f%%',
    colors=sns.color_palette("Blues")
)
plt.title("Distribucion de estudiantes por medio de transporte")
plt.tight_layout()
plt.show()


#Grafica de barras agrupadas
#Se aplica cuando hice cruces en el dataframe

#convierte la matriz en una lista para poderla graficar
conteoEstadoMedioTransporte=dataframeAsistencia.groupby(['estado','medio_transporte']).size().unstack(fill_value=0)

conteoEstadoMedioTransporte.plot(
    kind='bar',
    figsize=(10,6),
    color=colors
)
plt.title("Registros por estado de asistencia y medios de transporte")
plt.xlabel("Esatdo de asistencia")
plt.ylabel("Cantidad de registros")
plt.legend(title="Medio de transporte")
plt.tight_layout()
plt.show()
