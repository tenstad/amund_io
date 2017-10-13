
def astar(board, sort_li=lambda li: sorted(li, key=lambda x: -x.f), pop_li=lambda li: li.pop()):
    start, end = start_and_end(board)
    board.start = start
    board.end = end
    open_li = [start]
    closed_li = []
    start.g = 0
    start.h = distance(start, end, board.prediction_multiplier)

    while end not in closed_li:
        open_li = sort_li(open_li)
        tile = pop_li(open_li)
        closed_li.append(tile)
        expand(tile, end, open_li, closed_li)

    for tile in open_li:
        tile.text = "+"
    for tile in closed_li:
        tile.text = "*"
    tile = end
    path_len = 1
    while tile != start:
        path_len += 1
        tile.text = 'O'
        tile = tile.parent
    tile.text = 'O'

    board.open_li_len = len(open_li)
    board.closed_li_len = len(closed_li)
    board.path_len = path_len

    return board


def expand(tile, end, open_li, closed_li):
    for n in neighbours(tile):
        if n in closed_li or n in open_li:
            if n.g > tile.g + n.weight:
                amount = n.g - (tile.g + n.weight)
                n.parent.children.remove(n)
                tile.children.append(n)
                n.parent = tile
                shorten(n, amount)
        else:
            tile.children.append(n)
            n.parent = tile
            n.g = tile.g + n.weight
            n.h = distance(n, end, tile.board.prediction_multiplier)
            open_li.append(n)


def shorten(tile, amount):
    tile.g -= amount
    for c in tile.children:
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


def tryadd(s, tiles, x, y):
    try:
        tile = tiles[y][x]
        if tile.weight >= 0:
            s.add(tile)
    except IndexError:
        pass


def neighbours(tile):
    s = set()
    tryadd(s, tile.board.tiles, tile.x + 1, tile.y)
    if tile.x - 1 >= 0:
        tryadd(s, tile.board.tiles, tile.x - 1, tile.y)
    tryadd(s, tile.board.tiles, tile.x, tile.y + 1)
    if tile.y - 1 >= 0:
        tryadd(s, tile.board.tiles, tile.x, tile.y - 1)
    return s
