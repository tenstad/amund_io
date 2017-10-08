
def astar(board, sort_li=lambda li: sorted(li, key=lambda x: -x.f)):
    start, end = start_and_end(board)
    board.start = start
    board.end = end
    open_li = []
    closed_li = [start]
    start.g = 0
    start.h = distance(start, end, board.prediction_multiplier)
    expand(start, end, open_li, closed_li)

    while end not in closed_li:
        open_li = sort_li(open_li)
        tile = open_li.pop()
        closed_li.append(tile)
        expand(tile, end, open_li, closed_li)

    for tile in open_li:
        tile.text = "+"
    for tile in closed_li:
        tile.text = "*"
    tile = end
    while tile != start:
        tile.text = 'O'
        tile = tile.parent
    tile.text = 'O'
    return board


def expand(tile, end, open_li, closed_li):
    for n in neighbours(tile):
        if n in closed_li or n in open_li:
            if n.g > tile.g + n.weight:
                amount = n.g - tile.g + n.weight
                n.parent.children.remove(n)
                tile.children.append(n)
                n.parent = tile
                shorten(n, amount)
        else:
            tile.children.append(n)
            n.parent = tile
            n.g = tile.g + n.weight
            n.h = distance(n, end, tile.board.prediction_multiplier)
            if n not in open_li:
                open_li.append(n)


def shorten(tile, amount):
    for c in tile.children:
        c.g -= amount
        shorten(c, amount)


def distance(a, b, prediction_multiplier):
    return prediction_multiplier * (abs(a.x - b.x) + abs(a.y - b.y))


def start_and_end(board):
    start, end = None, None
    for row in board.tiles:
        for tile in row:
            if board.start_character == tile.character:
                start = tile
            elif board.end_character == tile.character:
                end = tile
    return start, end


def neighbours(tile):
    s = set()
    try:
        s.add(tile.board.tiles[tile.y][tile.x + 1])
    except IndexError:
        pass
    try:
        if tile.x - 1 >= 0:
            s.add(tile.board.tiles[tile.y][tile.x - 1])
    except IndexError:
        pass
    try:
        s.add(tile.board.tiles[tile.y + 1][tile.x])
    except IndexError:
        pass
    try:
        if tile.y - 1 >= 0:
            s.add(tile.board.tiles[tile.y - 1][tile.x])
    except IndexError:
        pass
    return s
