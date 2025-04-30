import pandas as pd

dataFrameAsistencia=pd.read_csv("./data/asistencia_estudiantes_completo.csv")

#Antes de filtrar como analistas de datos debes explorar la fuente de datos
#print(dataFrameAsistencia['estado'].unique())
#print(dataFrameAsistencia['estrato'].unique())
#print(dataFrameAsistencia['medio_transporte'].unique())

#Filtros y condiciones para transformar datos
#1. Reportar todos los estudiantes que asistieron
#estudiantesQueAsistieron= dataFrameAsistencia.query('estado=="asistio"')
#print(estudiantesQueAsistieron)

#2. Reportar todos los estudiantes que faltaron
#3. Reportar todos los estudiantes que llegaron tarde(Justificado)
#4. Reportar todos los estudiantes de estrato 1
#estudiantesEstratoUno= dataFrameAsistencia.query('estrato==1')
#print (estudiantesEstratoUno)

#5. Reportar todos los estudiantes de estratos altos
#6. Reportar todos los estudiantes que llegan en metro
#estudiantesQueUsanMetro= dataFrameAsistencia.query('medio_transporte=="metro"')
#print (estudiantesEstratoUno)
#7. Reportar todos los estudiantes que llegan en bicicleta
#8. Reportar todos los estudiantes que no caminan para llegar a la U
#estudiantesQueNoCaminan=dataFrameAsistencia.query('medio_transporte!="a pie"')
#print(estudiantesQueNoCaminan)
#9. Reportar todos los registros de asistencia del mes de junio
#10. Reportar los estudiantes que faltaron y usan bus para llegar a la U
#estudiantesQueFaltaronYUsanBus=dataFrameAsistencia.query('medio_transporte=="bus"and estado=="inasistencia"')
#print (estudiantesQueFaltaronYUsanBus.info())
#11. Reportar estudiantes que usan bus y son de estratos altos
#12. Reportar estudiantes que usan bus y son de estratos bajos
#13. Reportar estudiantes que llegan tarde y son de estratos 3,4,5 y 6
#14.Reportar estudiantes que usan transporte ecologicos
#15. Reportar estudiantes que faltan y usan carro para transportarse
#16. Reportar estudiantes que asisten son estratos altos y caminan
#17. Reportar estudiantes que son estratos bajos y justifican su inasistencia
#18. Reportar estudiantes que son estratos altos y justifican su inasistencia
#19. Reportar estudiantes que usan carro y justifican su inasistencia
#20. Reportar estudiantes que faltan y usan metro y son estratos medios



#Agrupaciones y conteos sobre los datos
#1. Contar cada registro de aistencia por cada estado
#conteoRegistrosPorEstado=dataFrameAsistencia.groupby('estado').size()
#print(conteoRegistrosPorEstado)
#2. Numero de registros por estrato
#conteoRegistroPorEstrato=dataFrameAsistencia.groupby('estrato').size()
#print (conteoRegistroPorEstrato)
#3. Cantidad de estudiantes por medio de transporte
#4. Cantidad de registro por grupo
#5. Cruce entre estado y medio de transporte
#cruceEstadoMedioTransporte=dataFrameAsistencia.groupby(['estado','medio_transporte']).size()
#print(cruceEstadoMedioTransporte)
#6. Promedio de estrato por estado de asistencia
promedioEstratoAsistencia=dataFrameAsistencia.groupby('estado')['estrato'].mean()
print(promedioEstratoAsistencia)
#7. Estrato promedio por medio de transporte
#8. Maximo estrato por estado de asistencia
#9. Minimo estrato por estado de asistencia
#10. Conteo de asistencias por grupo y por estado
#11. Transporte usado por cada grupo
#12. Cuantos grupos distintos registraron asistencia por fecha
#13. Promedio de estrato por fecha
#14. Numero de tipos de estado por transporte
#15. Primer registro de cada grupo