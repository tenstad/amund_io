from django.shortcuts import render
from django.views import View

from astar.board import Board
from astar.models import Board as BoardModel

class Index(View):

    def get(self, request, *args, **kwargs):
        board = Board()
        context = {
            'board': board,
            'boards': BoardModel.objects.all(),
        }
        return render(request, 'astar/index.html', context)

    def post(self, request, *args, **kwargs):
        try:
            board = Board()

            for attr in ['board', 'start_character', 'end_character', 'tile_config']:
                if request.POST.get(attr):
                    board.__setattr__(attr, request.POST.get(attr))
            for attr in ['algo', 'tile_size', 'tile_margin', 'font_size']:
                try:
                    if request.POST.get(attr):
                        board.__setattr__(attr, int(request.POST.get(attr)))
                except ValueError:
                    pass

            try:
                board_model = BoardModel.objects.get(pk=int(request.POST.get('board_model')))
                for attr in ['algo', 'board', 'start_character', 'end_character', 'tile_size', 'tile_margin', 'font_size', 'tile_config']:
                    board.__setattr__(attr, board_model.__getattribute__(attr))
            except Exception:
                pass

            board.init()
            board.solve()
        except Exception:
            board = Board()
            board.board = 'ERROR!\nInvalid input!'

        context = {
            'board': board,
            'boards': BoardModel.objects.all(),
        }
        return render(request, 'astar/index.html', context)