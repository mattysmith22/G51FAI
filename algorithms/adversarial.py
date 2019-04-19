import math

def minimax(node):
    func = max if node.maximisingPlayer() else min
    if node.endState():
        utility = node.endUtility()
    else:
        children = (minimax(x) for x in node.children())
        utility = func(children)
    node.setUtility(utility)
    return utility

def alphabeta(node, a=-math.inf, b=math.inf):
    if node.endState():
        value = node.endUtility()
    elif node.maximisingPlayer():
        value = -math.inf
        for child in node.children():
            value = max(value, alphabeta(child, a, b))
            a = max(a, value)
            if a >= b:
                break
    else:
        value = math.inf
        for child in node.children():
            value = min(value, alphabeta(child, a, b))
            b = min(b, value)
            if a >= b:
                break
    node.setUtility(value)
    return value