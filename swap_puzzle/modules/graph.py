from collections import deque
class Graph:
    def __init__(self, nodes=[]):
        self.nodes = nodes 
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
        self.edges = []
        
    def __str__(self):
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output

    def __repr__(self):
        return f"<graph.Graph: nb_nodes={self.nb_nodes}, nb_edges={self.nb_edges}>"

    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.graph[node1] = []
            self.nb_nodes += 1
            self.nodes.append(node1)
        if node2 not in self.graph:
            self.graph[node2] = []
            self.nb_nodes += 1
            self.nodes.append(node2)

        self.graph[node1].append(node2)
        self.graph[node2].append(node1)
        self.nb_edges += 1
        self.edges.append((node1, node2))

    def bfs(self, src, dst):
        visited = set()
        queue = deque([(src, [src])])  # Queue stores tuples of current node and path

        while queue:
            current_node, path = queue.popleft()
            if current_node == dst:
                return path  # Destination atteinte, retourne le chemin

            if current_node not in visited:
                visited.add(current_node)

                for neighbor in self.graph[current_node]:
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))
        return None


    @classmethod
    def graph_from_file(cls, file_name):
        with open(file_name, "r") as file:
            n, m = map(int, file.readline().split())
            graph = Graph(range(1, n+1))
            for _ in range(m):
                edge = list(map(int, file.readline().split()))
                if len(edge) == 2:
                    node1, node2 = edge
                    graph.add_edge(node1, node2) # will add dist=1 by default
                else:
                    raise Exception("Format incorrect")
        return graph

#Test de bfs sur  graph1.in et graph1.path.out
#graph1 = Graph.graph_from_file("ENSAE-prog2024/input/graph1.in")
source_node = 7
destination_node = 14
#result = graph1.bfs(source_node, destination_node)
#print(result)


