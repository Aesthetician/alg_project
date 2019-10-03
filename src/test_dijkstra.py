import graph
import dijkstra

g = graph.Graph()
for i in range(6):
    g.addVertex(i)
    print(g.vertList)
    
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)

s_id = 2
ssp = [3, 4, 0, 4, 4, 1]
dijkstra.dijkstra(g, s_id)
for v in g:
    print("( %s , %s )" % (v.getId(), v.getDist()))
    if v.getDist() != ssp[v.getId()]:
        print('SSP error @ %d' % v.getId())

s_id = 0
ssp = [0, 5, 3, 5, 1, 2]
dijkstra.dijkstra(g, s_id)
for v in g:
    print("( %s , %s )" % (v.getId(), v.getDist()))
    if v.getDist() != ssp[v.getId()]:
        print('SSP error @ %d' % v.getId())

for v in g:
    print("pred ( %s , %s )" % (v.getId(), v.getPred()))   

s_id = 3
ssp = [5, 8, 4, 0, 6, 3]
dijkstra.dijkstra(g, s_id)
for v in g:
    print("( %s , %s )" % (v.getId(), v.getDist()))
    if v.getDist() != ssp[v.getId()]:
        print('SSP error @ %d' % v.getId())

for v in g:
    print("pred ( %s , %s )" % (v.getId(), v.getPred()))   
