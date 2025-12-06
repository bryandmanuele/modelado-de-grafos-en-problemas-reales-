red_computadoras = {
    'Router': ['Servidor', 'Switch1', 'Switch2'],
    'Servidor': ['Router'],
    'Switch1': ['Router', 'PC1', 'PC2', 'Impresora1'],
    'Switch2': ['Router', 'PC3', 'PC4', 'Impresora2'],
    'PC1': ['Switch1'], 'PC2': ['Switch1'], 'Impresora1': ['Switch1'],
    'PC3': ['Switch2'], 'PC4': ['Switch2'], 'Impresora2': ['Switch2']
}
nodos = list(red_computadoras.keys())

print("\n\n## EJERCICIO 2: ANÁLISIS CODIFICADO")


num_vertices = len(nodos)
# Aristas = (Suma de grados) / 2
num_aristas = sum(len(adyacentes) for adyacentes in red_computadoras.values()) // 2 

print(" Pregunta b) Conteo ")
print(f"b) Vértices: {num_vertices}. Aristas: {num_aristas}")
print(f"\n Pregunta c) Conexidad ")
print(f"c) ¿Es conexo? Sí. Significa que hay un camino de comunicación entre todos.")

es_arbol = num_vertices == num_aristas + 1

print(f"\nPregunta d) ¿Es un árbol? ")
if es_arbol:
    print(f"d) ¿Es un árbol? Sí. Justificación: Es conexo y cumple la propiedad de que el número de vértices ({num_vertices}) es igual al número de aristas más uno ({num_aristas} + 1).")

num_componentes = 3
componentes_aislados = ["Servidor (aislado)", "Switch1", "Switch2"]

print(f"\nPregunta e) Componentes sin Router ")
print(f"e) Si se desconecta el Router, quedan {num_componentes} componentes conexas:")
for comp in componentes_aislados:
    print(f"   - {comp}")

dispositivo_critico = 'Router'

print(f"\n Pregunta f) Dispositivo más Crítico")
print(f"f) El dispositivo más crítico es el {dispositivo_critico}. Su falla divide la red en 3 componentes, aislando al Servidor y separando las dos subredes de los Switchs.")
