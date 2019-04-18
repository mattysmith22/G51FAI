def minimax(node):
    func = max if node.maximisingPlayer() else min
    if node.endState():
        utility = 0 if node.maximisingPlayer() else 1
    else:
        children = (minimax(x) for x in node.children())
        utility = func(children)
    node.setUtility(utility)
    return utility

def alphabeta(node, a=0, b=1):
    if node.endState():
        value = 0 if node.maximisingPlayer() else 1
    elif node.maximisingPlayer():
        value = 0
        for child in node.children():
            value = max(value, alphabeta(child, a, b))
            a = max(a, value)
            if a >= b:
                break
    else:
        value = 1
        for child in node.children():
            value = min(value, alphabeta(child, a, b))
            b = min(b, value)
            if a >= b:
                break
    node.setUtility(value)
    return value