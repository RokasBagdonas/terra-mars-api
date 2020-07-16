from django.db import models

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
    nickname = models.CharField(primary_key=True, max_length=32)


class Game(models.Model):
    date = models.DateTimeField()
    game_map = models.CharField(choices=MAPS, max_length=10)
    number_of_players = models.PositiveSmallIntegerField(default=2)
    draft_variant = models.BooleanField(default=True)

    prelude = models.BooleanField(default=False)
    venus_next = models.BooleanField(default=False)
    colonies = models.BooleanField(default=False)


class PlayerScore(models.Model):
    player_nickname = models.ForeignKey(Player, models.SET_NULL, blank=True, null=True)
    game_id = models.ForeignKey(Game, models.CASCADE)
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
