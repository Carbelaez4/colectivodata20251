import pandas as pd

dataFrameAsistencia = pd.read_csv("./data/asistencia_estudiantes_completo.csv")

# Antes de filtrar como analistas de datos debes explorar la fuente de datos
# print(dataFrameAsistencia['estado'].unique())
# print(dataFrameAsistencia['estrato'].unique())
# print(dataFrameAsistencia['medio_transporte'].unique())

# Filtros y condiciones para transformar datos
# 1. Reportar todos los estudiantes que asistieron
# estudiantesQueAsistieron= dataFrameAsistencia.query('estado=="asistio"')
# print(estudiantesQueAsistieron)

# 2. Reportar todos los estudiantes que faltaron
# estudiantesQueFaltaron= dataFrameAsistencia.query('estado=="inasistencia"')
# print(estudiantesQueFaltaron)

# 3. Reportar todos los estudiantes que llegaron tarde(Justificado)
# estudiantesTarde= dataFrameAsistencia.query('estado=="justificado"')
# print(estudiantesTarde)

# 4. Reportar todos los estudiantes de estrato 1
# estudiantesEstratoUno= dataFrameAsistencia.query('estrato==1')
# print (estudiantesEstratoUno)

# 5. Reportar todos los estudiantes de estratos altos
# estuidiantesEstratoAlto= dataFrameAsistencia[dataFrameAsistencia['estrato'].isin([5, 6])]
# print (estuidiantesEstratoAlto)

# 6. Reportar todos los estudiantes que llegan en metro
# estudiantesQueUsanMetro= dataFrameAsistencia.query('medio_transporte=="metro"')
# print (estudiantesEstratoUno)

# 7. Reportar todos los estudiantes que llegan en bicicleta
# estudiantesQueUsanBicicleta= dataFrameAsistencia.query('medio_transporte=="bicicleta"')
# print (estudiantesQueUsanBicicleta)

# 8. Reportar todos los estudiantes que no caminan para llegar a la U
# estudiantesQueNoCaminan=dataFrameAsistencia.query('medio_transporte!="a pie"')
# print(estudiantesQueNoCaminan)


# Preguntar
# 9. Reportar todos los registros de asistencia del mes de junio
# dataFrameAsistencia['fecha'] = pd.to_datetime(dataFrameAsistencia['fecha'])
# dataFrameAsistencia['mes']= dataFrameAsistencia['fecha'].dt.month
# estudiantesAsistenciaJunio= dataFrameAsistencia.query('estado=="asistio" and mes==3')
# print(estudiantesAsistenciaJunio)


# 10. Reportar los estudiantes que faltaron y usan bus para llegar a la U
# estudiantesQueFaltaronYUsanBus=dataFrameAsistencia.query('medio_transporte=="bus"and estado=="inasistencia"')
# print (estudiantesQueFaltaronYUsanBus.info())


# 11. Reportar estudiantes que usan bus y son de estratos altos
# estudiantesQueUsanBusYEstratoAlto = dataFrameAsistencia[
#    (dataFrameAsistencia['estrato'].isin([5, 6])) &
#    (dataFrameAsistencia['medio_transporte'] == "bus")]
# print(estudiantesQueUsanBusYEstratoAlto)

# 12. Reportar estudiantes que usan bus y son de estratos bajos
# estudiantesQueUsanBusYEstratoBajo= dataFrameAsistencia[(dataFrameAsistencia['estrato'].isin([1,2]))& (dataFrameAsistencia['medio_transporte']=="bus")]
# print(estudiantesQueUsanBusYEstratoBajo)

# 13. Reportar estudiantes que llegan tarde y son de estratos 3,4,5 y 6
# estudiantesQueLLeganTardeYEstratoTresSeis= dataFrameAsistencia[(dataFrameAsistencia['estrato'].isin([3,4,5,6]))&(dataFrameAsistencia['estado']=="justificado")]
# print(estudiantesQueLLeganTardeYEstratoTresSeis)

# 14.Reportar estudiantes que usan transporte ecologicos
# estudiantesTransporteEcologico = dataFrameAsistencia[(dataFrameAsistencia['medio_transporte']=="a pie") | (dataFrameAsistencia['medio_transporte']=="metro")]
# print(estudiantesTransporteEcologico)

# 15. Reportar estudiantes que faltan y usan carro para transportarse
# estudiantesQueFaltanYUsanCarro =dataFrameAsistencia[(dataFrameAsistencia['estado']=="inasistencia")&(dataFrameAsistencia['medio_transporte']=="carro")]
# print(estudiantesQueFaltanYUsanCarro)


# 16. Reportar estudiantes que asisten son estratos altos y caminan
# estudiantesEstratosAltosYCaminan= dataFrameAsistencia[(dataFrameAsistencia['estrato'].isin([5,6]))&(dataFrameAsistencia['medio_transporte']=="a pie")]
# print(estudiantesEstratosAltosYCaminan)


# 17. Reportar estudiantes que son estratos bajos y justifican su inasistencia
# estudiantesEstratoBajoYJustifica =dataFrameAsistencia[(dataFrameAsistencia['estrato'].isin([1,2]))&(dataFrameAsistencia['estado']=="justificado")]
# print(estudiantesEstratoBajoYJustifica)

# 18. Reportar estudiantes que son estratos altos y justifican su inasistencia
# estudiantesEstratoAltoYJustifica =dataFrameAsistencia[(dataFrameAsistencia['estrato'].isin([5,6]))&(dataFrameAsistencia['estado']=="justificado")]
# print(estudiantesEstratoAltoYJustifica)


# 19. Reportar estudiantes que usan carro y justifican su inasistencia
# estudiantesQueUsanCarroYJustifican =dataFrameAsistencia[(dataFrameAsistencia['medio_transporte']=="carro")&(dataFrameAsistencia['estado']=="justificado")]
# print(estudiantesQueUsanCarroYJustifican)


# 20. Reportar estudiantes que faltan y usan metro y son estratos medios
# estudiantesQueFaltanMetroYEstratomedio =dataFrameAsistencia[(dataFrameAsistencia['estado']=="inasistencia")&(dataFrameAsistencia['medio_transporte']=="metro")&(dataFrameAsistencia['estrato'].isin([3,4]))]
# print(estudiantesQueFaltanMetroYEstratomedio)


# Agrupaciones y conteos sobre los datos


# 1. Contar cada registro de aistencia por cada estado
# conteoRegistrosPorEstado=dataFrameAsistencia.groupby('estado').size()
# print(conteoRegistrosPorEstado)


# 2. Numero de registros por estrato
# conteoRegistroPorEstrato=dataFrameAsistencia.groupby('estrato').size()
# print (conteoRegistroPorEstrato)


# 3. Cantidad de estudiantes por medio de transporte
# cantidadEstudiantesPorMedioTransporte= dataFrameAsistencia.groupby('medio_transporte').size()
# print (cantidadEstudiantesPorMedioTransporte)

# 4. Cantidad de registro por grupo
# cantidadRegistrosPorGrupo = dataFrameAsistencia.groupby('id_grupo').size()
# print(cantidadRegistrosPorGrupo)


# 5. Cruce entre estado y medio de transporte
# cruceEstadoMedioTransporte=dataFrameAsistencia.groupby(['estado','medio_transporte']).size()
# print(cruceEstadoMedioTransporte)


# 6. Estrato promedio  por estado de asistencia
# promedioEstratoAsistencia=dataFrameAsistencia.groupby('estado')['estrato'].mean()
# print(promedioEstratoAsistencia)


# 7. Estrato promedio por medio de transporte
# estratoPromedioPorMedioTransporte = dataFrameAsistencia.groupby('medio_transporte')['estrato'].mean()
# print(estratoPromedioPorMedioTransporte)

# 8. Maximo estrato por estado de asistencia
# estadoAsistieron = dataFrameAsistencia[dataFrameAsistencia['estado'] == 'asistio']
# maximoEstrato = estadoAsistieron['estrato'].max()
# print(maximoEstrato)

# 9. Minimo estrato por estado de asistencia
# estadoAsistencia = dataFrameAsistencia[dataFrameAsistencia['estado'] == 'asistio']
# inimoEstrato = estadoAsistencia['estrato'].min()
# print(minimoEstrato)

# 10. Conteo de asistencias por grupo y por estado
# asistencias = dataFrameAsistencia[dataFrameAsistencia['estado'] == 'asistio']
# conteoAsistenciaPorGrupo = asistencias.groupby('id_grupo').size()
# print(conteoAsistenciaPorGrupo)


# 11. Transporte usado por cada grupo
# transportePorCadaGrupo =dataFrameAsistencia.groupby(['id_grupo','medio_transporte']).size()
# print(transportePorCadaGrupo)


# 12. Cuantos grupos distintos registraron asistencia por fecha
#asistencias = dataFrameAsistencia[dataFrameAsistencia['estado'] == 'asistio']
#gruposDistintosPorFecha = asistencias.groupby('fecha')['id_grupo'].nunique()
#print(gruposDistintosPorFecha)


# 13. Promedio de estrato por fecha
#asistencias = dataFrameAsistencia[dataFrameAsistencia['estado'] == 'asistio']
#promedioEstratoPorFecha = asistencias.groupby('fecha')['estrato'].mean()
#print(promedioEstratoPorFecha)

# 14. Numero de tipos de estado por transporte
#tiposEstadoPorTransporte = dataFrameAsistencia.groupby('medio_transporte')['estado'].nunique()
#print(tiposEstadoPorTransporte)



# 15. Primer registro de cada grupo
#primerRegistroGrupo = dataFrameAsistencia.groupby('id_grupo').first()
#print(primerRegistroGrupo)

