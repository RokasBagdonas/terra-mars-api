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
    "N/A",
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
    "Teractor",
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
    motto = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return f"{self.nickname}"


class Game(models.Model):
    date = models.DateTimeField(default=timezone.now)
    game_map = models.CharField(choices=MAPS, default=MAPS.Tharsis, max_length=16)
    number_of_generations = models.PositiveSmallIntegerField(default=10)

    draft_variant = models.BooleanField(default=True)
    prelude = models.BooleanField(default=False)
    venus_next = models.BooleanField(default=False)
    colonies = models.BooleanField(default=False)

    def __str__(self):
        return f"id: {self.id}; date: {self.date}; game_map: {self.game_map}"

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(game_map__in=set(dict(MAPS))),
                name="Only defined maps are allowed.",
            )
        ]


class GamePlayerScoreManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related("game", "player")


class PlayerScore(models.Model):
    player = models.ForeignKey(Player, models.SET_NULL, null=True)
    game = models.ForeignKey(Game, models.CASCADE)
    corporation = models.CharField(
        choices=CORPORATIONS, max_length=64, blank=False, null=False
    )

    terraform_rating = models.PositiveSmallIntegerField(default=20)
    milestones = models.PositiveSmallIntegerField(default=0)
    awards = models.PositiveSmallIntegerField(default=0)
    greeneries = models.PositiveSmallIntegerField(default=0)
    cities = models.PositiveSmallIntegerField(default=0)

    event_cards = models.SmallIntegerField(default=0)
    automated_cards = models.SmallIntegerField(default=0)
    active_cards = models.SmallIntegerField(default=0)
    resources = models.SmallIntegerField(default=0)

    objects = models.Manager()
    game_player_objects = GamePlayerScoreManager()

    class Meta:
        default_related_name = "scores"
        constraints = [
            models.UniqueConstraint(
                fields=["player", "game"], name="one_score_per_player_per_game"
            ),
            models.UniqueConstraint(
                fields=["corporation", "game"],
                condition=Q()
                name="only_unique_corporations_per_game"
            ),
            models.CheckConstraint(
                check=models.Q(corporation__in=set(dict(CORPORATIONS))),
                name="Only defined corporations are allowed.",
            ),
        ]

    def __str__(self):
        p = self.player.nickname if self.player else "<no player>"
        g = self.game
        return f"""player nickname: {p},
        game_id: {g.id},
        game date: {g.date},
        corporation: {self.corporation}."""
