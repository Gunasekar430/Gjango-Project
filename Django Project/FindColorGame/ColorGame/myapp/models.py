from django.db import models


class GameResult(models.Model):
    player_name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    treasures_found = models.IntegerField(default=0)
    moves = models.IntegerField(default=0)
    played_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.player_name