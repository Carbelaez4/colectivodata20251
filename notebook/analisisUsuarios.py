import pandas as pd

dataFrameUsuarios = pd.read_excel("./data/usuarios_sistema_completo.xlsx")

# 1. Solo estudiantes
# estudiantes = dataFrameUsuarios[dataFrameUsuarios["tipo_usuario"] == "estudiante"]
# print (estudiantes)


# 2. Solo profesores
# profesores = dataFrameUsuarios[dataFrameUsuarios['tipo_usuario'].str.lower() == 'docente']
# print(profesores)

# 3. Todos excepto estudiantes
# noEstudiantes = dataFrameUsuarios[dataFrameUsuarios['tipo_usuario'].str.lower() != 'estudiante']
# print(noEstudiantes)

# 4. Filtrar por especialidad
# especialidad_buscada="Ingenieria civil"
# resultado=dataFrameUsuarios[dataFrameUsuarios['especialidad']==especialidad_buscada]
# print (especialidad_buscada)

# 5. Excluir una especialidad
# especialidad_excluida="inginieria mecanica"
# resultado=dataFrameUsuarios[dataFrameUsuarios['especialidad']==especialidad_excluida]
# print (resultado)


# 6. Excluir administrativos
# resultado=dataFrameUsuarios[dataFrameUsuarios['tipo_usuario'] != 'administrativo']
# print(resultado)


# 7. Direcciones en medellin
# resultado = dataFrameUsuarios[dataFrameUsuarios['direccion'].str.contains('medellin', case=False, na=False)]
# print(resultado)


# 8. Direcciones terminadas en sur
# resultado = dataFrameUsuarios[dataFrameUsuarios['direccion'].str.contains(r'sur\s*$', case=False, na=False)]
# print(resultado)


# 9. Direcciones que inician con calle
# resultado = dataFrameUsuarios[dataFrameUsuarios['direccion'].str.contains(r'^calle', case=False, na=False)]
# print(resultado)


# 10.Especialidades que contienen la palabra datos
# resultado = dataFrameUsuarios[dataFrameUsuarios['especialidad'].str.contains('datos', case=False, na=False)]
# print(resultado)


# 11. instructores en itagui
# resultado = dataFrameUsuarios[
#    (dataFrameUsuarios['tipo_usuario'].str.lower() == 'instructor') &
#    (dataFrameUsuarios['direccion'].str.contains('itagui', case=False, na=False))
# ]
# print(resultado)


# 12. nacidos despues de 2000
# dataFrameUsuarios['fecha_nacimiento'] = pd.to_datetime(dataFrameUsuarios['fecha_nacimiento'], errors='coerce')
# resultado = dataFrameUsuarios[dataFrameUsuarios['fecha_nacimiento'] > '2000-12-31']
# print(resultado)


# 13. nacidos en los 90
# dataFrameUsuarios['fecha_nacimiento'] = pd.to_datetime(dataFrameUsuarios['fecha_nacimiento'], errors='coerce')
# resultado = dataFrameUsuarios[
#    (dataFrameUsuarios['fecha_nacimiento'] > '1989-12-31') &
#    (dataFrameUsuarios['fecha_nacimiento'] < '2000-01-01')
# ]
# print(resultado)


# 14. direcciones en envigado
# resultado = dataFrameUsuarios[dataFrameUsuarios['direccion'].str.contains('envigado', case=False, na=False)]
# print(resultado)


# 15. especialdiades que empizan por I
# resultado = dataFrameUsuarios[dataFrameUsuarios['especialidad'].str.contains(r'^i', case=False, na=False)]
# print(resultado)


# 16. usuarios sin direccion
# resultado = dataFrameUsuarios[dataFrameUsuarios['direccion'].isnull()]
# print(resultado)


# 17. usuarios sin especialidad
# resultado = dataFrameUsuarios[dataFrameUsuarios['especialidad'].isnull()]
# print(resultado)


# 18. profesores que viven en sabaneta
# resultado = dataFrameUsuarios[
#    (dataFrameUsuarios['tipo_usuario'].str.lower() == 'profesor') &
#    (dataFrameUsuarios['direccion'].str.contains('sabaneta', case=False, na=False))
# ]
# print(resultado)


# 19. aprendices que viven en bello
# resultado = dataFrameUsuarios[
#    (dataFrameUsuarios['tipo_usuario'].str.lower() == 'aprendiz') &
#    (dataFrameUsuarios['direccion'].str.contains('bello', case=False, na=False))
# ]
# print(resultado)


# 20. nacidos en el nuevo milenio
# dataFrameUsuarios['fecha_nacimiento'] = pd.to_datetime(dataFrameUsuarios['fecha_nacimiento'], errors='coerce')
# resultado = dataFrameUsuarios[dataFrameUsuarios['fecha_nacimiento'] >= '2000-01-01']
# print(resultado)


# 1. total por tipo
# totalPorTipo= dataFrameUsuarios["tipo_usuario"].value_counts()
# print(totalPorTipo)

# 2. total por especialidad
# total_por_especialidad = dataFrameUsuarios['especialidad'].value_counts(dropna=False)
# print(total_por_especialidad)

# 3. cantidad de especialidades distintas
# cantidad_especialidades = dataFrameUsuarios['especialidad'].nunique(dropna=True)
# print (cantidad_especialidades)


# 4. tipos de usuario por especialidad
# usuarios_por_tipo_y_especialidad = dataFrameUsuarios.groupby(['especialidad', 'tipo_usuario']).size().reset_index(name='total')
# print(usuarios_por_tipo_y_especialidad)

# 5. usuario mas antiguo por tipo
# dataFrameUsuarios["fecha_nacimiento"] = pd.to_datetime(dataFrameUsuarios["fecha_nacimiento"], errors="coerce")
# dataFrameUsuarios_filtrado = dataFrameUsuarios[dataFrameUsuarios["fecha_nacimiento"].notna()]
# indices_mas_antiguos = dataFrameUsuarios_filtrado.groupby("tipo_usuario")["fecha_nacimiento"].idxmin()
# usuario_mas_antiguo_por_tipo = dataFrameUsuarios_filtrado.loc[indices_mas_antiguos]
# print(usuario_mas_antiguo_por_tipo)


# 6. usuario mas joven por tipo
# dataFrameUsuarios['fecha_nacimiento'] = pd.to_datetime(dataFrameUsuarios['fecha_nacimiento'], errors='coerce')
# df_validos = dataFrameUsuarios[dataFrameUsuarios['fecha_nacimiento'].notna()]
# indices_mas_jovenes = df_validos.groupby("tipo_usuario")["fecha_nacimiento"].idxmax()
# usuario_mas_joven_por_tipo = df_validos.loc[indices_mas_jovenes]
# print(usuario_mas_joven_por_tipo)


# 7. primer registro por tipo
# primeros_indices = dataFrameUsuarios.groupby("tipo_usuario").head(1).index
# primer_registro_por_tipo = dataFrameUsuarios.loc[primeros_indices]
# print(primer_registro_por_tipo)


# 8. ultimo registro por tipo
# ultimos_indices = dataFrameUsuarios.groupby("tipo_usuario").tail(1).index
# ultimo_registro_por_tipo = dataFrameUsuarios.loc[ultimos_indices]
# print(ultimo_registro_por_tipo)


# 9. combinacion tipo por especialidad
# combinacionTipoPorEspecialidad = dataFrameUsuarios.pivot_table(index='tipo_usuario', columns='especialidad', aggfunc='size', fill_value=0)
# print(combinacionTipoPorEspecialidad)

# 10. el mas viejo por especialidad
# dataFrameUsuarios['fecha_nacimiento']=pd.to_datetime(dataFrameUsuarios["fecha_nacimiento"], errors='coerce')
# dataFrameUsuariosValidos=dataFrameUsuarios.dropna(subset=['especialidad','fecha_nacimiento'])
# masViejoPorEspecialidad= dataFrameUsuariosValidos.sort_values('fecha_nacimiento').groupby('especialidad').first().reset_index()
# print(masViejoPorEspecialidad[['especialidad','nombre_usuario','fecha_nacimiento']])

# 11. cuantos de cada especialidad por tipo
# cuantosEspecialidadPorTipo= dataFrameUsuarios.groupby('especialidad')['tipo_usuario'].size()
# print(cuantosEspecialidadPorTipo)


# 12. edad promedio por tipo
# promedioEdadPorTipo=dataFrameUsuarios.groupby('tipo_usuario')['edad'].mean()
# print(promedioEdadPorTipo)


# 13. años de nacimeinto mas frecuente por especialidad
# dataFrameUsuarios["fecha_nacimiento"] = pd.to_datetime(dataFrameUsuarios["fecha_nacimiento"])
# dataFrameUsuarios["ano_nacimiento"] = dataFrameUsuarios["fecha_nacimiento"].dt.year
# anosNacimientoMasFrecuentes = (dataFrameUsuarios.groupby("especialidad")["fecha_nacimiento"].mean())
# print(anosNacimientoMasFrecuentes)

# 14. mes de nacimiento mas frecuente por tipo
# dataFrameUsuarios['fecha_nacimiento'] = pd.to_datetime(dataFrameUsuarios['fecha_nacimiento'], errors='coerce')
# dataFrameUsuarios['mes_nacimiento'] = dataFrameUsuarios['fecha_nacimiento'].dt.month_name()
# mes_frecuente_por_tipo = (
#    dataFrameUsuarios.groupby("tipo_usuario")["mes_nacimiento"]
#    .agg(lambda x: x.mode().iloc[0] if not x.mode().empty else None)
#    .reset_index(name="mes_mas_frecuente")
# )
# print(mes_frecuente_por_tipo)


# 15. UNA CONSULTA O FILTRO QUE UD PROPONGA: Usuarios con especialidad relacionada con tecnologías y nacidos después del año 2000
dataFrameUsuarios['fecha_nacimiento'] = pd.to_datetime(
    dataFrameUsuarios['fecha_nacimiento'], errors='coerce')
palabras_tecnologia = ['sistemas', 'software', 'datos',
                       'informática', 'computación', 'tecnología']

resultado = dataFrameUsuarios[
    (dataFrameUsuarios['fecha_nacimiento'] >= '2000-01-01') &
    (dataFrameUsuarios['especialidad'].fillna('').str.lower().apply(
        lambda x: any(palabra in x for palabra in palabras_tecnologia)
    ))
]

print(resultado)
