__all__ = ["codegeographique", "codification", "communesinsee", "correcteurorgues", "grep"]
from .correcteurorgues import detecter_type_edifice
from .correcteurorgues import corriger_nom_edifice
from .correcteurorgues import simplifier_nom_edifice
from .correcteurorgues import simplifier_nom_edifice_parentheses
from .correcteurorgues import reduire_edifice
from .correcteurorgues import supprimer_accents
#from .communesinsee import Communes
from .codegeographique import Communes

from utilsorgues import generiques

from .codification import codifier_instrument