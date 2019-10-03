import graph
import dijkstra
import kruskal
import time
import bfs
import bfsdfs
import matplotlib.pyplot as plt
import random
import gdfs

VNUM = 5000
glabel = '5'

# Turn interactive plotting off
plt.ioff()

def a_plot(y, title, fname):
    fig = plt.figure()
    plt.plot(y, 'bo')
    plt.ylabel('time(s)')
    plt.title(title)
    plt.savefig('./plot%s/%s.png' % (glabel, fname))
    plt.close(fig)
    #plt.show()

startTime = time.time()
print('---- G1 generation ----')
g1 = graph.Graph1(5000, 8)
g1.info()
#print(g11.vertList)
#g1.showEdge()
elaspedTime = time.time() - startTime
print('elaspedTime: %f' % elaspedTime)
print('')

startTime = time.time()
print('---- G2 generation ----')
g2 = graph.Graph2(5000, 0.2)
g2.info()
#print(g12.vertList)
#g2.showEdge()
elaspedTime = time.time() - startTime
print('elaspedTime: %f' % elaspedTime)
print('')

s_name = []
t_name = []
for i in range(0,6):
    sid = random.randint(1,VNUM)
    s_name.append(sid)
    tid = random.randint(1,VNUM)
    t_name.append(tid)
#print(s_name)
#print(t_name)


print('---- Test on G1 by kruskal ----')
k = kruskal.kruskal()        
startTime = time.time()
mst = k.kruskal(g1)
mst.collectEdges()
gmst = k.adjgraph()

s = s_name[0]
t = t_name[0]
#ssp = bfs.bfs(gmst, s, t)
ssp = bfsdfs.dfs_iter(gmst, s)
#print(ssp)
elaspedTime = time.time() - startTime
print('#1 pair elaspedTime: %f' % elaspedTime)
et_arr = [elaspedTime]
for i in range(1,6):
    #s_id = s_name[i]
    s = s_name[i]
    t = t_name[i]
    startTime = time.time()
    k = kruskal.kruskal()        
    startTime = time.time()
    mst = k.kruskal(g1)
    mst.collectEdges()
    #gmst = k.adjgraph()
    #dfs visit to get parent
    g_dfs = gdfs.gdfs()
    g_dfs.dfs_visit(mst, s)
    ssp = g_dfs.dfs_path(mst, s, t)    
    #ssp = bfsdfs.dfs_iter(gmst, s)
    et = time.time() - startTime
    #print(ssp)
    et_arr.append(et)
    print('#%d elaspedTime: %f' % (i+1, et))
title = 'Running time of the test on G1 by kruskal'
fn = 'kru_g1'
a_plot(et_arr, title, fn)


print('---- Test on G2 by kruskal ----')
#g11 = graph.Graph1(5000, 8)
#g11.info()
k = kruskal.kruskal()        
startTime = time.time()
#mst = k.kruskal(g11)
mst = k.kruskal(g2)
mst.collectEdges()
gmst = k.adjgraph()

s = s_name[0]
t = t_name[0]
#ssp = bfs.bfs(gmst, s, t)
#print(ssp)
elaspedTime = time.time() - startTime
print('#1 pair elaspedTime: %f' % elaspedTime)
et_arr = [elaspedTime]
for i in range(1,6):
    #s_id = s_name[i]
    s = s_name[i]
    t = t_name[i]
    startTime = time.time()
    k = kruskal.kruskal()
    startTime = time.time()
    mst = k.kruskal(g2)
    mst.collectEdges()
    #gmst = k.adjgraph()
    #ssp = bfsdfs.dfs_iter(gmst, s)
    #dfs visit to get parent
    g_dfs = gdfs.gdfs()
    g_dfs.dfs_visit(mst, s)
    ssp = g_dfs.dfs_path(mst, s, t)
    print(ssp)
    et = time.time() - startTime
    et_arr.append(et)
    print('#%d elaspedTime: %f' % (i+1, et))
title = 'Running time of the test on G2 by kruskal'
fn = 'kru_g2'
a_plot(et_arr, title, fn)