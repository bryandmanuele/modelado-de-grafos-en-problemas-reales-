grafo_vuelos = {
    'Mexico': {'Cancun': 1500, 'Monterrey': 1200},
    'Cancun': {'Miami': 3500},
    'Monterrey': {'Houston': 2800},
    'Houston': {'Miami': 1800},
    'Miami': {'Mexico': 4000}
}
ciudades = ['Mexico', 'Cancun', 'Monterrey', 'Houston', 'Miami']

print("b) Clasificación: Dirigido y Ponderado. es dirigido porque indica que solo son vuelos de ida, y es ponderado porque cada arista tiene un valor especifico.")

grados_salida = {ciudad: len(conexiones) for ciudad, conexiones in grafo_vuelos.items()}
grados_entrada = {ciudad: 0 for ciudad in ciudades}
# Lógica para calcular grados de entrada: contar cuántas veces aparece una ciudad como destino.
for origen, conexiones in grafo_vuelos.items():
    for destino in conexiones:
        grados_entrada[destino] += 1

print("\n--- Pregunta c) Grados ")
for c in ciudades:
    print(f"  {c}: Salida={grados_salida.get(c, 0)}, Entrada={grados_entrada.get(c, 0)}")

ciudad_mas_salidas = max(grados_salida, key=grados_salida.get)

print("\n--- Pregunta d) Más Salientes ")
print(f"d) Ciudad con más vuelos salientes: {ciudad_mas_salidas} ({grados_salida[ciudad_mas_salidas]} vuelos)")


ruta_1_costo = grafo_vuelos['Mexico']['Cancun'] + grafo_vuelos['Cancun']['Miami']
ruta_2_costo = grafo_vuelos['Mexico']['Monterrey'] + grafo_vuelos['Monterrey']['Houston'] + grafo_vuelos['Houston']['Miami']

print("\n--- Pregunta e) Ruta más Barata ")
if ruta_1_costo < ruta_2_costo:
    print(f"e) Ruta más barata: México -> Cancún -> Miami. Costo: ${ruta_1_costo}")
else:
    print(f"e) Ruta más barata: México -> Monterrey -> Houston -> Miami. Costo: ${ruta_2_costo}")


tiene_vuelo_regreso_a_mexico = 'Mexico' in grafo_vuelos.get('Miami', {})
es_ciclo_simple_identificado = tiene_vuelo_regreso_a_mexico and len(grafo_vuelos['Mexico']) > 0

print("\n--- Pregunta f) Ciclo ")
if es_ciclo_simple_identificado:
    print(f"f) ¿Existe algún ciclo? Sí. Se identifica el ciclo: México -> Cancún -> Miami -> México.")
else:
    print("f) ¿Existe algún ciclo? No.")
