"""Validation des entrees utilisateur."""

from datetime import date
from .exceptions import InvalidInputError

VALID_PRIORITIES = {"low", "medium", "high"}
VALID_STATUSES = {"todo", "doing", "done"}

TITLE_MIN = 1
TITLE_MAX = 100
DESCRIPTION_MAX = 500


def validate_title(value):
    if not isinstance(value, str):
        raise InvalidInputError("Le titre doit etre une chaine de caracteres.")
    cleaned = value.strip()
    if len(cleaned) < TITLE_MIN:
        raise InvalidInputError("Le titre ne peut pas etre vide.")
    if len(cleaned) > TITLE_MAX:
        raise InvalidInputError(f"Le titre doit faire au plus {TITLE_MAX} caracteres.")
    return cleaned


def validate_description(value):
    if value is None:
        return ""
    if not isinstance(value, str):
        raise InvalidInputError("La description doit etre une chaine de caracteres.")
    cleaned = value.strip()
    if len(cleaned) > DESCRIPTION_MAX:
        raise InvalidInputError(f"La description doit faire au plus {DESCRIPTION_MAX} caracteres.")
    return cleaned


def validate_priority(value):
    if value not in VALID_PRIORITIES:
        raise InvalidInputError(
            f"Priorite invalide '{value}'. Valeurs attendues : {sorted(VALID_PRIORITIES)}."
        )
    return value


def validate_status(value):
    if value not in VALID_STATUSES:
        raise InvalidInputError(
            f"Statut invalide '{value}'. Valeurs attendues : {sorted(VALID_STATUSES)}."
        )
    return value


def validate_due_date(value):
    if value is None or value == "":
        return None
    if not isinstance(value, str):
        raise InvalidInputError("La date doit etre une chaine au format AAAA-MM-JJ.")
    try:
        return date.fromisoformat(value).isoformat()
    except ValueError:
        raise InvalidInputError(
            f"Date invalide '{value}'. Format attendu : AAAA-MM-JJ (ex : 2026-12-31)."
        )
