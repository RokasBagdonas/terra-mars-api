from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from model_utils import Choices

CORPORATIONS = Choices(
    "Aphrodite",
    "Aridor",
    "Arklight",
    "Celestic",
    "Cheung Shing Mars",
    "Credicor",
    "Ecoline",
    "Helion",
    "Interplanetary Cinematics",
    "Inventrix",
    "Manutech",
    "Mining Guild",
    "Morning Star Inc.",
    "Phobolog",
    "Point Luna",
    "Polyphemos",
    "Poseidon",
    "Robinson Industries",
    "Saturn Systems",
    "Storm Craft Incorporated",
    "Terractor",
    "Tharsis Republic",
    "Thorgate",
    "United Nations Mars Initiative",
    "Valley Trust",
    "Viron",
    "Vitor",
)


MAPS = Choices("Tharsis", "Elysium", "Hellas")


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nickname = models.CharField(max_length=32, unique=True)
    motto = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nickname}"


class Game(models.Model):
    players = models.ManyToManyField(Player, through="PlayerScore")
    date = models.DateTimeField(default=timezone.now())
    game_map = models.CharField(choices=MAPS, default=MAPS.Tharsis, max_length=14)

    draft_variant = models.BooleanField(default=True)
    prelude = models.BooleanField(default=False)
    venus_next = models.BooleanField(default=False)
    colonies = models.BooleanField(default=False)

    def __str__(self):
        return f"id: {self.id}; date: {self.date}; game_map: {self.game_map}"


class PlayerScore(models.Model):
    player = models.ForeignKey(Player, models.SET_NULL, related_name="player", null=True)
    game = models.ForeignKey(Game, models.CASCADE)
    corporation = models.CharField(choices=CORPORATIONS, max_length=40)

    terraform_rating = models.PositiveSmallIntegerField(default=20)
    milestones = models.PositiveSmallIntegerField(default=0)
    awards = models.PositiveSmallIntegerField(default=0)
    greeneries = models.PositiveSmallIntegerField(default=0)
    cities = models.PositiveSmallIntegerField(default=0)

    event_cards = models.SmallIntegerField(default=0)
    automated_cards = models.SmallIntegerField(default=0)
    active_cards = models.SmallIntegerField(default=0)
    resources = models.SmallIntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["player", "game"], name="one_score_per_player_per_game"
            )
        ]

    def __str__(self):
        s = self.player.nickname + "," if self.player else "<no player>"
        return f"""player nickname: {s},
        game_id: {self.game_id},
        game date: {self.game.date},
        corporation: {self.corporation}."""
