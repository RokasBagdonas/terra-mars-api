from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

CORPORATIONS = [
    ("APH", "Aphrodite"),
    ("ARD", "Aridor"),
    ("ARK", "Arklight"),
    ("CLS", "Celestic"),
    ("CRE", "Credicor"),
    ("CSM", "Cheung Shing Mars"),
    ("ECO", "Ecoline"),
    ("HEL", "Helion"),
    ("IPC", "Interplanetary Cinematics"),
    ("IVN", "Inventrix"),
    ("MNG", "Mining Guild"),
    ("MNT", "Manutech"),
    ("MSI", "Morning Star Inc."),
    ("PBL", "Phobolog"),
    ("PLP", "Polyphemos"),
    ("PNL", "Point Luna"),
    ("PSD", "Poseidon"),
    ("RBI", "Robinson Industries"),
    ("SCI", "Storm Craft Incorporated"),
    ("STS", "Saturn Systems"),
    ("TAR", "Tharsis Republic"),
    ("TER", "Terractor"),
    ("THR", "Thorgate"),
    ("UMN", "United Nations Mars Initiative"),
    ("VIR", "Viron"),
    ("VLT", "Valley Trust"),
    ("VTR", "Vitor"),
]

MAPS = [("THR", "Tharsis"), ("ELS", "Elysium"), ("HEL", "Hellas")]


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=32, blank=True, null=True)
    motto = models.CharField(max_length=100, blank=True, null=True)

class Game(models.Model):
    players = models.ManyToManyField(Player, through="PlayerScore")
    date = models.DateTimeField()
    game_map = models.CharField(choices=MAPS, max_length=10)

    draft_variant = models.BooleanField(default=True)
    prelude = models.BooleanField(default=False)
    venus_next = models.BooleanField(default=False)
    colonies = models.BooleanField(default=False)


class PlayerScore(models.Model):
    player = models.ForeignKey(
        Player, models.SET_NULL, related_name="username", null=True
    )
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
