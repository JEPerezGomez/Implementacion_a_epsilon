import heapq

# Grafo con distancias (costos de viaje)
graph = {
    'Museo': [('Depósito Central', 5), ('Galería Norte', 10)],
    'Depósito Central': [('Museo', 5), ('Galería Norte', 3), ('Centro de Restauración', 2)],
    'Galería Norte': [('Museo', 10), ('Depósito Central', 3), ('Centro de Restauración', 7), ('Galería Sur', 8)],
    'Centro de Restauración': [('Depósito Central', 2), ('Galería Norte', 7), ('Galería Sur', 4), ('Estación de Transporte', 6)],
    'Galería Sur': [('Galería Norte', 8), ('Centro de Restauración', 4), ('Estación de Transporte', 1)],
    'Estación de Transporte': [('Centro de Restauración', 6), ('Galería Sur', 1)]
}

# Heurísticas (estimación del costo hasta la Estación de Transporte)
heuristics = {
    'Museo': 12,
    'Depósito Central': 8,
    'Galería Norte': 5,
    'Centro de Restauración': 4,
    'Galería Sur': 2,
    'Estación de Transporte': 0  # Destino
}

def busqueda_a_epsilon(graph, heuristics, start, goal, epsilon=1):
    open_list = [(0 + heuristics[start] * epsilon, start)]  
    heapq.heapify(open_list)
    
    g_costs = {start: 0}  
    came_from = {}  

    while open_list:
        f_cost, current = heapq.heappop(open_list)

        if current == goal:
            return reconstruct_path(came_from, current), g_costs[current]

        for neighbor, cost in graph[current]:
            new_g_cost = g_costs[current] + cost
            if new_g_cost < g_costs.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_costs[neighbor] = new_g_cost
                f_cost = new_g_cost + heuristics[neighbor] * epsilon  # Ajuste con epsilon
                heapq.heappush(open_list, (f_cost, neighbor))
                
    return None, None

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

# Ejecutar el algoritmo A-epsilon para transportar la obra de arte
start_city = 'Museo'
destination_city = 'Estación de Transporte'

# Valores de epsilon para probar
epsilon_values = [1, 3]

results = {}
for epsilon_value in epsilon_values:
    path, total_cost = busqueda_a_epsilon(graph, heuristics, start_city, destination_city, epsilon=epsilon_value)
    results[epsilon_value] = {'path': path, 'total_cost': total_cost}
    print(f"Con epsilon = {epsilon_value} -> Ruta: {path}, Costo total: {total_cost}")

# Comparación entre A* (epsilon = 1) y A-epsilon (epsilon = 3)
path_a_star = results[1]['path']
cost_a_star = results[1]['total_cost']
path_a_epsilon = results[3]['path']
cost_a_epsilon = results[3]['total_cost']

if cost_a_star and cost_a_epsilon:
    difference = abs(cost_a_epsilon - cost_a_star) / cost_a_star * 100
    print(f"\nDiferencia entre A* y A-epsilon:")
    print(f"- Ruta A*: {path_a_star} | Costo: {cost_a_star}")
    print(f"- Ruta A-epsilon: {path_a_epsilon} | Costo: {cost_a_epsilon}")
    print(f"Diferencia porcentual en el costo: {difference:.2f}%")
else:
    print("No se encontraron rutas para ambas configuraciones.")
