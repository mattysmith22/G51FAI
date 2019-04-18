# Here are base classes for a tree problem
# Includes basic graphing

from abc import abstractmethod, ABC
from graphviz import Digraph

class TreeProblem(ABC):
    def __init__(self):
        self.relations = []
        self.rootnode = None
    
    def addNode(self, parent, child):
        self.relations.append([parent, child])
    
    def numNodes(self):
        return 1 + len(self.relations)
    
    def clear(self):
        self.relations = []
    
    def makeDistinct(self):
        uniqueRelation = []
        for [parent, child] in self.relations:
            if [parent, child] not in uniqueRelation:
                uniqueRelation.append([parent, child])
        self.relations = uniqueRelation
    
    @abstractmethod
    def renderNode(self, graph, node):
        pass
    
    def render(self, *args, **kwargs):
        nodes = [self.rootnode]
        self.makeDistinct()
        for [_,child] in self.relations:
            if child not in nodes:
                nodes.append(child)
        graph = Digraph(*args, **kwargs)
        for i in nodes:
            self.renderNode(graph, i)
        for [parent, child] in self.relations:
            graph.edge(str(parent), str(child))
        return graph


class TreeNode(ABC):
    @abstractmethod
    def __str__(self):
        pass
    @abstractmethod
    def __repr__(self):
        pass
    
    @abstractmethod
    def endState(self):
        pass
    
    @abstractmethod
    def children(self):
        pass

class CostTreeNode(TreeNode):
    @abstractmethod
    def fcost(self):
        pass

class HeuristicTreeNode(CostTreeNode):
    @abstractmethod
    def hcost(self):
        pass

class AdversarialTreeNode(TreeNode):
    @abstractmethod
    def maximisingPlayer(self):
        pass
    
    @abstractmethod
    def setUtility(self, value):
        pass