import graph

class gdfs():
    def __init__(self):
        self.t = 0
        
    def dfs_graph(self, G):
        for v in G.vertList:
            if v.getColor() == 0:
                self.dfs_visit(G, v)
            
    def dfs_visit(self, G, uid):
        #self.t += 1
        black = 1
        gray = 2
        u = G.vertList[uid]
        u.setColor(gray) #2: gray
        for v in u.connectedTo:
            if v.getColor() == 0:
                v.setPredID(u.getId())
                self.dfs_visit(G, v.getId())
        u.setColor(black)

    def dfs_path(self, G, sid, tid):
        '''tid->sid'''
        path = [tid]
        prt_id = G.vertList[tid].getPred()
        while prt_id != sid:
            v = G.vertList[prt_id]
            path.append(v.getId())
            prt_id = v.getPred()
        path.append(prt_id)
        return path

            


if __name__ == "__main__":
    #test code 
    g = graph.Graph()
    for i in range(6):
        g.addVertex(i)
    g.vertList
    
    g.addEdge(0,1,2)
    g.addEdge(0,2,1)
    #g.addEdge(0,3,5)
    #g.addEdge(1,2,2)
    #g.addEdge(1,3,3)
    g.addEdge(2,4,1)
    #g.addEdge(2,3,3)
    g.addEdge(3,4,1)
    #g.addEdge(3,5,5)
    g.addEdge(4,5,1)
    s = 0
    t = 5
    g_dfs = gdfs()
    g_dfs.dfs_visit(g, s)
    ssp = g_dfs.dfs_path(g, s, t)    
    print(ssp)

