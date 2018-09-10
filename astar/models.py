from django.db import models

class TileConfig(models.Model):
    title = models.CharField(max_length=50, default='Config')
    tile_config = models.TextField(max_length=300, default='')

    def __str__(self):
        return self.title

class Board(models.Model):
    title = models.CharField(max_length=50, default='Board')
    board = models.TextField(max_length=1000, default='')
    tile_config_fk = models.ForeignKey(TileConfig)
    start_character = models.CharField(max_length=1, default='A')
    end_character = models.CharField(max_length=1, default='B')
    tile_size = models.IntegerField(default=100)
    tile_margin = models.IntegerField(default=0)
    font_size = models.IntegerField(default=16)
    algo = models.IntegerField(default=0)
    prediction_multiplier = models.FloatField(default=1.0)

    def get(self, attr):
        if attr == 'tile_config':
            return self.tile_config_fk.tile_config
        else:
            return getattr(self, attr, '')

    @property
    def tile_config(self):
        return self.tile_config_fk.tile_config

    def __str__(self):
        return self.title
