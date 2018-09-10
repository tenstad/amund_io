from astar.astar import astar

def breadth(board):
    return astar(board, sort_li=lambda li: li, pop_li=lambda li: li.pop(0))
