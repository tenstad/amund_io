from astar.astar import astar

def dijkstra(board):
    return astar(board, sort_li=lambda li: sorted(li, key=lambda x: -x.g))
