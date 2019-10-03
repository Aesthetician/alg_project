import graph
import gheap

NUMVERT = 5002

def dijkstra(G, s_id):
    for vid in G.vertList.keys():
        G.vertList[vid].setDist(gheap.MAXVAL) #v.d = inf
        G.vertList[vid].setPredID(-1) #v.predecessor = []
    G.vertList[s_id].setDist(0) #s.d = 0
    q = gheap.min_gheap(NUMVERT)
    vid_list = [ v for v in G.vertList.keys()]
    #print(vid_list)
    #print(G.vertList[2].getDist())
    dist_list = [ G.vertList[vid].getDist() for vid in vid_list ]
    #print(dist_list)
    q.build_heap(vid_list, dist_list)
    #q.show_arrarys()
    while not q.isEmpty():
        uid, u_dist = q.extract_min()
        #s = s U {u}
        for v in G.vertList[uid].getConnections():
            #relax(u,v,w)
            u = G.vertList[uid]
            newDist = u.getDist() + u.getWeight(v)        
            if v.getDist() > newDist:
                v.setDist(newDist)
                v.setPredID(uid)                
                vid = v.getId()
                q.decrease_key(vid, newDist)

def min_in_arr(a, val):
    size = len(a)
    min = val[0]
    midx = 0
    for i in range(0, size):
        if min > val[a[i]]:
            min = val[a[i]]
            midx = i
    
    #print(min)
    #print('midx')
    #print(midx)
    minid = a[midx]
    min = val[minid]
    #print(minid)
    a[-1], a[midx] = a[midx], a[-1]
    a.pop()
    return minid, min 


def dijkstra_array(G, s_id):
    for vid in G.vertList.keys():
        G.vertList[vid].setDist(gheap.MAXVAL) #v.d = inf
        G.vertList[vid].setPredID(-1) #v.predecessor = []
    dist_arr = [gheap.MAXVAL] * NUMVERT
    #dist_arr = [gheap.MAXVAL] * 10
    
    ssp_arr = {}
    #print(dist_arr)
    #G.vertList[s_id].setDist(0) #s.d = 0
    #q = gheap.min_gheap(NUMVERT)
    dist_arr[s_id] = 0
    #print(dist_arr)
    
    vid_list = [ v for v in G.vertList.keys()]
    #print(vid_list)
    #print(G.vertList[2].getDist())
    #dist_list = [ G.vertList[vid].getDist() for vid in vid_list ]
    #print(dist_list)
    #q.build_heap(vid_list, dist_list)
    #q.show_arrarys()
    q_size = len(vid_list)
    while q_size > 0:
        #uid, u_dist = min_array(q)
        uid, u_dist = min_in_arr(vid_list, dist_arr)
        q_size = len(vid_list)
        #print(uid)
        ssp_arr[uid] = u_dist
        #s = s U {u}
        for v in G.vertList[uid].getConnections():
            #relax(u,v,w)
            u = G.vertList[uid]
            #newDist = u.getDist() + u.getWeight(v)
            newDist = dist_arr[uid] + u.getWeight(v)                        
            if v.getDist() > newDist:
                v.setDist(newDist)
                v.setPredID(uid)                
                vid = v.getId()
                #q.decrease_key(vid, newDist)
                dist_arr[vid] = newDist
    
    return ssp_arr


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
    for v in g:
        for w in v.getConnections():
            print("( %s , %s )" % (v.getId(), w.getId()))
    
    s_id = 2
    dijkstra(g, s_id)
    print('dij')
    for v in g:
        print("( %s , %s )" % (v.getId(), v.getDist()))
        
    s_id = 2
    ssp = dijkstra_array(g, s_id)
    print('dij array')
    print(ssp)


    #a = [1,2,3,4,5]
    #v = [12,4,5,1,11,9] 

    #print(min_in_arr(a, v))
    #print(a)

