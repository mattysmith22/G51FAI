import abstractproblems
from copy import deepcopy
class NimProblem(abstractproblems.TreeProblem):
    def __init__(self, startvalue = 7, maxStarts=True):
        start = startvalue if isinstance(startvalue, list) else [startvalue]
        self.rootnode = NimNode(start, self, 1, maxStarts)
        self.relations = []


    def renderNode(self, graph, node):
            if node.result == 0:
                if node.endState():
                    graph.node(str(node),str(node.sticks),fillcolor="red", style="filled")
                else:
                    graph.node(str(node),str(node.sticks),fillcolor="darkorange", style="filled")
            elif node.result == 1:
                if node.endState():
                    graph.node(str(node),str(node.sticks),fillcolor="green", style="filled")
                else:
                    graph.node(str(node),str(node.sticks),fillcolor="lawngreen", style="filled")
            else:
                graph.node(str(node),str(node.sticks))

class NimNode(abstractproblems.AdversarialTreeNode):
    def __init__(self, sticks, base, depth, maximising=True):
        self.sticks = sticks
        self.base = base
        self.depth = depth
        self.result = None
        self.maximising = maximising
    
    def __str__(self):
        strout = str(self.depth) + "d"
        for i in self.sticks:
            strout += "{}s".format(i)
        return strout[:-1] + "u" + ("" if self.result == None else str(self.result))
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        return  self.sticks == other.sticks and self.depth == other.depth and self.base is other.base and self.result == other.result
    
    def endState(self):
        for stick in self.sticks:
            if stick not in [1,2]:
                return False
        return True
    
    def children(self):
        childs = []

        for i in range(len(self.sticks)):
            for j in range(1,int((self.sticks[i]-1)/2)+1):
                sticks = deepcopy(self.sticks)
                changed = sticks.pop(i)
                sticks.append(j)
                sticks.append(changed-j)
                sticks.sort(reverse=True) # Comment out to speed up, makes easier to read
                childs.append(NimNode(sticks, self.base, self.depth, not self.maximising))
                self.base.addNode(self, childs[-1])
        return childs
    
    def setUtility(self, value):
        self.result = value

    def maximisingPlayer(self):
        return self.maximising