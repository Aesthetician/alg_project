import random
import math

MAXWEIGHT = 50
MINWEIGHT = 1
MAXDIST = math.inf

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {} # format: vertex -> weight 
        self.dist = MAXDIST
        self.pred_id = -1
        self.heap_idx = 0
        self.color = 0 # 0: white, 1:black, 2: gray

    def addNeighbor(self, nbr, weight = 0):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getConnectionsID(self):
        connList = []
        for v in self.connectedTo:
            connList.append(v.getId())
        return connList

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def getId(self):
        return self.id

    def getDist(self):
        return self.dist

    def setDist(self, d):
        self.dist = d

    def getPred(self):
        return self.pred_id

    def setPredID(self, pid):
        self.pred_id = pid
    
    def getColor(self):
        return self.color

    def setColor(self, c):
        self.color = c

class Graph:
    def __init__(self):
        self.vertList = {} # format: key(id) -> vertex
        self.numVertices = 0
        self.numEdges = 0
        self.edgeList = []

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    # v and w are keys
    def addEdge(self, v, w, weight = MINWEIGHT):
        if v not in self.vertList:
            nv = self.addVertex(v)
        if w not in self.vertList:
            nv = self.addVertex(w)
        self.numEdges = self.numEdges + 1        
        self.vertList[v].addNeighbor(self.vertList[w], weight)
        self.vertList[w].addNeighbor(self.vertList[v], weight)
        

    def getVertices(self):
        return self.vertList.keys()
    
    def genWeight(self):
        return random.randint(MINWEIGHT,MAXWEIGHT)
    
    # check if u is neighbor of v
    def isNeighbor(self, v, u): 
        if self.vertList[u] in self.vertList[v].connectedTo:
            return True
        else:
            return False

    def info(self):
        print('# vertices: %d, # edges: %d' % (self.numVertices, self.numEdges))
        print('degree: %f' % (2 * self.numEdges / self.numVertices))

    def buildCycle(self, givenNumVertices):
        urn = BallUrn(givenNumVertices)
        crtvid = urn.drawBall()   
        self.addVertex(crtvid)
        vid1st = crtvid
        for i in range(givenNumVertices):            
            if i == (givenNumVertices - 1):
                vid = vid1st
            else:
                vid = urn.drawBall()
                self.addVertex(vid)
            #weight = random.randint(MINWEIGHT,MAXWEIGHT)
            weight = self.genWeight()
            self.addEdge(crtvid, vid, weight)
            crtvid = vid

    #def __contains__(self,n):
    #    return n in self.vertList

    def collectEdges(self):
        self.edgeList = []
        for vid in self.vertList.keys(): # list key
            #print(vid)
            v = self.vertList[vid]
            for w in v.getConnections():
                edge = [v.connectedTo[w], v.getId(), w.getId()] # weight, vid, wid
                self.edgeList.append(edge)
    
    def showEdge(self):
        return print(self.edgeList)

    def getEdgeList(self):
        return self.edgeList

    def __iter__(self):
        return iter(self.vertList.values())

class BallUrn:
    def __init__(self, num):
        self.numBall = num
        self.ballList = []
        self.idxEnd = self.numBall - 1
        self.iniBallList()

    def iniBallList(self):
        for i in range(0,self.numBall):
            self.ballList.append(i)

    def drawBall(self):
        idx = random.randint(0,self.idxEnd)
        draw = self.ballList[idx]
        self.ballList[idx] = self.ballList[self.idxEnd]
        self.numBall = self.numBall - 1
        self.updateIdxEnd()
        return draw 

    def updateIdxEnd(self):
        self.idxEnd = self.numBall - 1

class Graph1(Graph):
    def __init__(self, num, degree):
        super(Graph1, self).__init__()
        self.buildCycle(num)
        self.buildEdges(degree)
    
    def buildEdges(self, degree):
        idxEnd = self.numVertices - 1
        totalEdges = int (degree * self.numVertices / 2)
        numAdded = totalEdges - self.numEdges
        skip = 0
        i = 0
        while i < numAdded:
            v = random.randint(0, idxEnd)
            w = random.randint(0, idxEnd)
            while v == w:            
                w = random.randint(0, idxEnd)
            
            if self.isNeighbor(v, w):
                skip = skip + 1
                #print('v=%d, w=%d' % (v, w))
            else:
                self.addEdge(v, w, self.genWeight())  
                i = i + 1 
            
        print('i: %d, skip: %d' % (i, skip)) 
        
class Graph2(Graph):
    def __init__(self, num, adjRate):
        super(Graph2, self).__init__()        
        self.buildCycle(num)
        self.buildEdges(adjRate)

    def buildEdges(self, adjRate):
        arr = []
        for key in self.vertList:
            arr.append(key)

        sizeVert = len(arr)
        total = 0
        skip = 0
        hit = 0
        for i in range(0, sizeVert):
            for j in range(i + 1, sizeVert):
                p = random.random()
                total = total + 1
                if p < adjRate:
                    if self.vertList[arr[j]] in self.vertList[arr[i]].connectedTo:
                        #print('%d is adj of %d' % (arr[j], arr[i]))
                        skip = skip + 1
                    else:
                        #print(p)
                        hit = hit + 1
                        self.addEdge(arr[i], arr[j])
        
        print('# of added: %d, total: %d, rate: %f, skip: %d' % (hit, total, hit/total, skip))
         

