from astar.astar import astar

def depth(board):
    return astar(board, sort_li=lambda li: li)
