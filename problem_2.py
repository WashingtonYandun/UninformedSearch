# Usando como entrada el grafo presentado en la Figura 2, donde ‘S’ es el nodo inicial y ‘G’
# es el objetivo de la b´usqueda, resuelva los siguientes ejercicios (considere que en cualquiera
# de las b´usquedas los nodos son generados en orden alfab´etico y que la visita a un nodo
# corresponde al proceso de expansi´on del mismo):
# a) Determine el orden de visita de los nodos y el camino retornado por la estrategia de
# b´usqueda BFS (primero en amplitud).
# 1
# b) Determine el orden de visita de los nodos y el camino retornado por la estrategia de
# b´usqueda DFS (primero en profundidad).
# c) Determine el orden de visita de los nodos y el camino retornado por la estrategia de
# b´usqueda UCS (costo uniforme).

def create_fig2() -> nx.Graph:
    fig = nx.Graph()
    fig.add_edge('S', 'A', weight=3)
    fig.add_edge('S', 'B', weight=6)
    fig.add_edge('S', 'C', weight=2)
    fig.add_edge('A', 'B', weight=4)
    fig.add_edge('A', 'D', weight=3)
    fig.add_edge('B', 'D', weight=9)
    fig.add_edge('B', 'E', weight=2)
    fig.add_edge('C', 'E', weight=1)
    fig.add_edge('D', 'F', weight=5)
    fig.add_edge('D', 'E', weight=4)
    fig.add_edge('E', 'H', weight=5)
    fig.add_edge('F', 'G', weight=5)
    fig.add_edge('G', 'H', weight=8)
    return fig