import graph
import bfs
import heapsort
import time

class kruskal:
    
    def __init__(self):
        self.parent = dict()
        self.rank = dict()
        self.mst = graph.Graph()

    def make_set(self, vertice):
        self.parent[vertice] = vertice
        self.rank[vertice] = 0
        
    def find(self, vertice):
        if self.parent[vertice] != vertice:
            self.parent[vertice] = self.find(self.parent[vertice])
        return self.parent[vertice]
    
    def union(self, vertice1, vertice2):
        root1 = self.find(vertice1)
        root2 = self.find(vertice2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] += 1
    
    def kruskal(self, G):
        minimum_spanning_tree = graph.Graph()
        for vid in G.vertList.keys():
            self.make_set(vid)
            minimum_spanning_tree.addVertex(vid)
        
        G.collectEdges()
        #G.showEdge() 
        edges = G.getEdgeList()
        
        #print('edges:')        
        #print(edges)    
        startTime = time.time()      
        #edges.sort()
        heapsort.heapsort(edges)
        elaspedTime = time.time() - startTime
        print('edge sort elaspedTime: %f' % elaspedTime)
        #print('sorted edges:')
        #print(edges)  
        
        for edge in edges:
            weight, vertice1, vertice2 = edge
            if self.find(vertice1) != self.find(vertice2):
                self.union(vertice1, vertice2)
                minimum_spanning_tree.addEdge(vertice1, vertice2, weight)

        self.mst = minimum_spanning_tree    
        return minimum_spanning_tree

    def adjgraph(self):
        g = self.mst
        gmst = {}
        for v in g:
            gmst[v.getId()] = v.getConnectionsID()
        
        return gmst


if __name__ == "__main__":
    #test code 
    g = graph.Graph()
    for i in range(6):
        g.addVertex(i)
    g.vertList    
    g.addEdge(0,1,2)
    g.addEdge(0,2,1)
    g.addEdge(0,3,5)
    g.addEdge(1,2,2)
    g.addEdge(1,3,3)
    g.addEdge(2,4,1)
    g.addEdge(2,3,3)
    g.addEdge(3,4,1)
    g.addEdge(3,5,5)
    g.addEdge(4,5,1)
    g.collectEdges()
    g.showEdge()
    
    k = kruskal()        
    #assert k.kruskal(g) == minimum_spanning_tree
    mst = k.kruskal(g)
    print(mst.vertList)
    mst.collectEdges()
    mst.showEdge()
    gmst = k.adjgraph()
    print(gmst)

    s = 0
    t =5
    ssp = bfs.bfs(gmst, s, t)
    print(ssp)