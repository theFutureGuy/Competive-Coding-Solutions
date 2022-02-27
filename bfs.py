class vertices:
    def __init__(self,n) -> None:
        self.name = n
        self.neighbour = list()
        self.weight = 9999
    def add_neighbour(self, v) -> None:
        if v not in self.neighbour:
            self.neighbour.append(v)

class Graph :
    g = {}

    def add_vertex(self,vertex):
        if isinstance(vertex,vertices) and vertex.name not in self.g : 
            self.g[vertex.name] = vertex
            return True
        return False
    def add_edge(self,u,v):
        if(u and v in self.g):
            for key ,val in self.g.items() :
                if(key==u):
                    val.add_neighbour(v)
                if(key==v):
                    val.add_neighbour(u)
            return True
        return False

    def display(self):
        for key in list().append(self.g.keys()):
            print(key + str(self.g[key].neighbour) + "  " + str(self.g[key].weight))
            
    def bfs(self,v):
        q = []
        v.weight = 0

        for i in v.neighbour:
            self.g[i].weight = v.weight+1
            q.append(i)
        
        while(len(q)):
            t = q.pop(0)
            ptr = self.g[t]

            for k in ptr.neighbour:
                ptr2 = self.g[k]
                q.append(k)
                if(ptr2.weight > ptr.weight + 1):
                    ptr2.weight = ptr.weight + 1

g = Graph()
a = vertices('A')
g.add_vertex(a)
g.add_vertex(vertices('B'))
for i in range(ord('A'), ord('K')):
	g.add_vertex(vertices(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
	g.add_edge(edge[:1], edge[1:])

g.display()




