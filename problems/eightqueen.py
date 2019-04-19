import problems.abstract
class QueenProblem(problems.abstract.TreeProblem):
    def __init__(self, gridsize=8):
        self.rootnode = QueenNode([], self)
        self.relations = []
        self.gridsize = gridsize
    
    def renderNode(self, graph, node):
            if node.searched == False and not node.endState():
                graph.node(str(node),str(node),fillcolor="orange", style="filled")
            elif node.endState() and node.searched == False:
                graph.node(str(node),str(node),fillcolor="blue", style="filled")
            elif node.endState():
                graph.node(str(node),str(node),fillcolor="green", style="filled")
            else:
                graph.node(str(node),str(node))

class QueenNode(problems.abstract.TreeNode):
    def __init__(self, queens=[], base=None):
        self.base = QueenProblem(self) if base==None else base
        self.queens = queens
        self.searched = False
    
    def endState(self):
        return len(self.queens) == self.base.gridsize
    
    def valid(self):
        for i in range(len(self.queens)):
            for j in range(len(self.queens)):
                if i == j:
                    break
                if self.queens[i] == self.queens[j]:
                    return False
                if abs(i-j) == abs(self.queens[i]-self.queens[j]):
                    return False
        return True
    
    def children(self):
        out = []
        for i in range(self.base.gridsize):
            newNode = QueenNode(self.queens + [i], base=self.base)
            if newNode.valid():
                self.base.addNode(self, newNode)
                out.append(newNode)
        return out

    def __str__(self):
        return str(self.queens)
    
    def __repr__(self):
        out = "+"+("-"*self.base.gridsize)+"+\n"
        for i in self.queens:
            out += "|"
            out += " " * i
            out += "#"
            out += " " * (self.base.gridsize-1-i)
            out += "|\n"
        out += "+"+("-"*self.base.gridsize)+"+"
        return out