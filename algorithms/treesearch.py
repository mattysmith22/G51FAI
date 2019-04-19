def generalsearch(node, queuingfn):
    queue = [node]
    while len(queue) > 0:
        currNode = queue.pop(0)
        currNode.searched = True
        if currNode.endState():
            return currNode
        queue = queuingfn(queue, currNode.children())
    return None

def breadthfirst(node):
    return generalsearch(node, lambda q, n: q + n)

def depthfirst(node):
    return generalsearch(node, lambda q, n: n + q)

def ucs(node):
    def ucsFunc(q, n):
        arr = q + n
        arr.sort(reverse=True, key = lambda x: x.fcost())
        return arr
    return generalsearch(node, ucsFunc)

def astar(node):
    def astarFunc(q, n):
        arr = q + n
        arr.sort(reverse=True, key = lambda x: x.fcost() + x.hcost())
        return arr
    return generalsearch(node, astarFunc)