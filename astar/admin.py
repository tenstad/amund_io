from django.contrib.admin import site

from astar.models import Board, TileConfig

site.register(Board)
site.register(TileConfig)