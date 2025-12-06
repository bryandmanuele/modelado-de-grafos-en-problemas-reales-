dependencias_academicas = {
    'M1': ['M2', 'M3'],
    'M2': ['M4'],
    'M3': ['M5', 'M4'],
    'M4': ['M6', 'M3'], 
    'M5': ['M6'],
    'M6': []
}
asignaturas = list(dependencias_academicas.keys())

# Cálculos para el Análisis
grados_salida = {m: len(reqs) for m, reqs in dependencias_academicas.items()}
grados_entrada = {m: 0 for m in asignaturas}
for origen, destinos in dependencias_academicas.items():
    for destino in destinos:
        grados_entrada[destino] += 1

#Definición
print("\na) Problema: Es la materia que tengo y su relacion con la otra materia.")
print("b) Vértice: Asignatura.")
print("c) Arista: Nos indica que la materia y la otra materia tiene relacion).")

# e) Análisis: Grados, Conexidad, Ciclos
print("\ne) Análisis: Grados, Conexidad, Ciclos ")
print("\nGrados (Salida/Entrada):")
for m in asignaturas:
    print(f"  {m}: S={grados_salida.get(m, 0)}, E={grados_entrada.get(m, 0)}")

print("\nConexidad:")
print("  El grafo es Débilmente Conexo. (Existe camino de 1 a 6, pero no viceversa.)")

print("\nCiclos:")
print("  Sí, existe un ciclo. Ciclo: M3 y M4. .")

# f) Pregunta Interesante
print("\nf) Pregunta Interesante ")
print("Pregunta: ¿Cuál es la secuencia más larga de dependencias (camino más largo)?")
print("Respuesta: **M1 > M3 > M4 > M6 (4 materias).")
