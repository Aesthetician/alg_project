import graph

g = graph.Graph()
for i in range(6):
    g.addVertex(i)

print(g.vertList)
#g.collectEdges()
#g.showEdge()

g1 = graph.Graph()
g1.buildCycle(5)
print(g1.vertList)
print(g1.vertList[1].id)
print(g1.vertList[1].connectedTo)
print('get connections')
print(g1.vertList[1].getConnections())
print(g1.vertList[1].getConnectionsID())
g1.collectEdges()
print('showEdge')
g1.showEdge() 
elist = g1.getEdgeList()
print('sort edges')
#print(elist)
elist.sort()
print(elist)  
  


def showEdge(g):
    i = 0
    for v in g:
        for w in v.getConnections():
            print("%d: ( %s , %s )" % (i, v.getId(), w.getId()))
            i = i + 1


g11 = graph.Graph1(5000, 8)
g11.info()
print('----G1----')
#print(g11.vertList)
#showEdge(g11)

print('----G2----')
g12 = graph.Graph2(5000, 0.2)
g12.info()
#print(g12.vertList)
#showEdge(g12)