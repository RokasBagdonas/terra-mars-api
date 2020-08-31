# Generated by Django 3.0.8 on 2020-08-31 19:55

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Player",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nickname", models.CharField(max_length=32, unique=True)),
                ("motto", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Game",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField()),
                (
                    "game_map",
                    models.CharField(
                        choices=[
                            ("THR", "Tharsis"),
                            ("ELS", "Elysium"),
                            ("HEL", "Hellas"),
                        ],
                        max_length=10,
                    ),
                ),
                ("draft_variant", models.BooleanField(default=True)),
                ("prelude", models.BooleanField(default=False)),
                ("venus_next", models.BooleanField(default=False)),
                ("colonies", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="PlayerScore",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "corporation",
                    models.CharField(
                        choices=[
                            ("Aphrodite", "Aphrodite"),
                            ("Aridor", "Aridor"),
                            ("Arklight", "Arklight"),
                            ("Celestic", "Celestic"),
                            ("Cheung Shing Mars", "Cheung Shing Mars"),
                            ("Credicor", "Credicor"),
                            ("Ecoline", "Ecoline"),
                            ("Helion", "Helion"),
                            ("Interplanetary Cinematics", "Interplanetary Cinematics"),
                            ("Inventrix", "Inventrix"),
                            ("Manutech", "Manutech"),
                            ("Mining Guild", "Mining Guild"),
                            ("Morning Star Inc.", "Morning Star Inc."),
                            ("Phobolog", "Phobolog"),
                            ("Point Luna", "Point Luna"),
                            ("Polyphemos", "Polyphemos"),
                            ("Poseidon", "Poseidon"),
                            ("Robinson Industries", "Robinson Industries"),
                            ("Saturn Systems", "Saturn Systems"),
                            ("Storm Craft Incorporated", "Storm Craft Incorporated"),
                            ("Terractor", "Terractor"),
                            ("Tharsis Republic", "Tharsis Republic"),
                            ("Thorgate", "Thorgate"),
                            (
                                "United Nations Mars Initiative",
                                "United Nations Mars Initiative",
                            ),
                            ("Valley Trust", "Valley Trust"),
                            ("Viron", "Viron"),
                            ("Vitor", "Vitor"),
                        ],
                        max_length=40,
                    ),
                ),
                ("terraform_rating", models.PositiveSmallIntegerField(default=20)),
                ("milestones", models.PositiveSmallIntegerField(default=0)),
                ("awards", models.PositiveSmallIntegerField(default=0)),
                ("greeneries", models.PositiveSmallIntegerField(default=0)),
                ("cities", models.PositiveSmallIntegerField(default=0)),
                ("event_cards", models.SmallIntegerField(default=0)),
                ("automated_cards", models.SmallIntegerField(default=0)),
                ("active_cards", models.SmallIntegerField(default=0)),
                ("resources", models.SmallIntegerField(default=0)),
                (
                    "game",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="mars_api.Game"
                    ),
                ),
                (
                    "player",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="player",
                        to="mars_api.Player",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="game",
            name="players",
            field=models.ManyToManyField(
                through="mars_api.PlayerScore", to="mars_api.Player"
            ),
        ),
        migrations.AlterField(
            model_name="game",
            name="game_map",
            field=models.CharField(
                choices=[
                    ("Tharsis", "Tharsis"),
                    ("Elysium", "Elysium"),
                    ("Hellas", "Hellas"),
                ],
                default="Tharsis",
                max_length=14,
            ),
        ),
        migrations.AlterField(
            model_name="game",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2020, 8, 6, 12, 15, 23, 867035, tzinfo=utc)
            ),
        ),
        migrations.AlterField(
            model_name="game",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2020, 8, 10, 9, 5, 46, 309975, tzinfo=utc)
            ),
        ),
        migrations.AddConstraint(
            model_name="playerscore",
            constraint=models.UniqueConstraint(
                fields=("player", "game"), name="one_score_per_player_per_game"
            ),
        ),
        migrations.AlterField(
            model_name="game",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2020, 8, 11, 18, 11, 11, 320928, tzinfo=utc)
            ),
        ),
        migrations.AlterField(
            model_name="playerscore",
            name="player",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="player_scores",
                to="mars_api.Player",
            ),
        ),
        migrations.AlterField(
            model_name="game",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2020, 8, 12, 7, 22, 59, 146804, tzinfo=utc)
            ),
        ),
        migrations.AlterField(
            model_name="game",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2020, 8, 12, 7, 28, 8, 250418, tzinfo=utc)
            ),
        ),
        migrations.AlterField(
            model_name="playerscore",
            name="game",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="player_scores",
                to="mars_api.Game",
            ),
        ),
        migrations.AlterField(
            model_name="game",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2020, 8, 13, 19, 29, 48, 997605, tzinfo=utc)
            ),
        ),
        migrations.AlterField(
            model_name="game",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2020, 8, 14, 8, 4, 45, 100099, tzinfo=utc)
            ),
        ),
        migrations.AlterField(
            model_name="game",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2020, 8, 14, 8, 5, 47, 352265, tzinfo=utc)
            ),
        ),
        migrations.AlterField(
            model_name="game",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2020, 8, 14, 8, 6, 43, 626576, tzinfo=utc)
            ),
        ),
        migrations.AlterField(
            model_name="game",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2020, 8, 14, 8, 6, 50, 135670, tzinfo=utc)
            ),
        ),
        migrations.RemoveField(model_name="game", name="players",),
        migrations.AlterField(
            model_name="game",
            name="date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="playerscore",
            name="game",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="players_scores",
                to="mars_api.Game",
            ),
        ),
        migrations.AlterField(
            model_name="playerscore",
            name="player",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="player_score",
                to="mars_api.Player",
            ),
        ),
        migrations.AddConstraint(
            model_name="game",
            constraint=models.CheckConstraint(
                check=models.Q(game_map__in=["Tharsis", "Elysium", "Hellas"]),
                name="Only ['Tharsis', 'Elysium', 'Hellas'] maps are allowed.",
            ),
        ),
        migrations.AddConstraint(
            model_name="playerscore",
            constraint=models.CheckConstraint(
                check=models.Q(
                    corporation__in=[
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
                    ]
                ),
                name="Only defined corporations are allowed.",
            ),
        ),
        migrations.AddConstraint(
            model_name="playerscore",
            constraint=models.UniqueConstraint(
                fields=("corporation",), name="one_unique_corporation_per_game"
            ),
        ),
        migrations.RemoveConstraint(
            model_name="playerscore", name="one_unique_corporation_per_game",
        ),
        migrations.AddConstraint(
            model_name="playerscore",
            constraint=models.UniqueConstraint(
                fields=("corporation", "game"), name="one_unique_corporation_per_game"
            ),
        ),
        migrations.RemoveConstraint(
            model_name="playerscore", name="one_unique_corporation_per_game",
        ),
        migrations.AddConstraint(
            model_name="playerscore",
            constraint=models.UniqueConstraint(
                fields=("corporation", "game"), name="only_unique_corporations_per_game"
            ),
        ),
        migrations.AlterField(
            model_name="playerscore",
            name="player",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="scores",
                to="mars_api.Player",
            ),
        ),
    ]
