"""Exceptions personnalisees du gestionnaire de taches."""


class TaskError(Exception):
    """Exception de base."""


class InvalidInputError(TaskError):
    """Entree utilisateur invalide (titre vide, priorite inconnue, date mal formee...)."""


class TaskNotFoundError(TaskError):
    """Aucune tache trouvee avec cet identifiant."""


class StorageError(TaskError):
    """Erreur de lecture/ecriture du fichier de donnees."""
