from django.db import models
from enum import Enum

class Player(models.Model):
    name = models.charField(max_length = 30)

class 

class Map(Enum):
    DEFAULT = "Default"
    ELYSIUM = "Elysium"
    HELLAS = "Hellas"

class Corporation(Enum):
    CREDICOR = "Credicor"
    ECOLINE = "Ecoline"
    HELION = "Helion"
    MINING_GUILD = "Mining Guild"
    INTERPLANETARY_CINEMATICS = "Interplanetary Cinematics"
    INVENTRIX = "Inventrix"
    PHOBOLOG = "Phobolog"
    THARSIS_REPUBLIC = "Tharsis Republic"
    THORGATE = "Thorgate"
    UMNI = "UMNI"
    TERACTOR = "Teractor"
    SATURN_SYSTEMS = "Saturn Systems"
    APHRODITE = "Aphrodite"
    CELESTIC = "Celestic"
    MANUTECH = "Manutech"
    MORNING_STAR_INC = "Morning Star Inc."
    VIRON = "Viron"
    CHEUNG_SHING_MARS = "Cheung Shing Mars"
    POINT_LUNA = "Point Luna"
    ROBINSON_INDUSTRIES = "Robinson Industries"
    VALLEY_TRUST = "Valley Trust"
    VITOR = "Vitor"
    ARIDOR = "Aridor"
    ARKLIGHT = "Arklight"



