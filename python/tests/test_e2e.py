"""PARTIE 4 - Tests END-TO-END (E2E).

On simule un PARCOURS UTILISATEUR COMPLET, du debut a la fin,
via les memes points d'entree que la vraie application.
"""

import pytest
from src.task_manager import TaskManager
from src.storage import save_tasks, load_tasks


@pytest.mark.e2e
def test_parcours_complet_journee_de_travail(tmp_path):
    """Scenario : un utilisateur planifie sa journee, fait une tache, sauvegarde."""
    fichier = tmp_path / "ma_journee.json"

    # 1. L'utilisateur lance l'app : aucune tache
    mgr = TaskManager()
    mgr.replace_all(load_tasks(str(fichier)))
    assert mgr.get_stats()["total"] == 0

    # 2. Il ajoute 3 taches de la journee
    mgr.create_task("Lire mes mails", priority="low")
    mgr.create_task("Reunion equipe a 10h", priority="high")
    mgr.create_task("Reviser pytest", priority="medium")

    # 3. Il consulte sa liste triee par priorite : la reunion remonte
    plus_prioritaire = mgr.list_tasks(sort_by="priority")[0]
    assert plus_prioritaire.title == "Reunion equipe a 10h"

    # 4. Il termine deux taches
    mgr.mark_done(1)
    mgr.mark_done(2)

    # 5. Il consulte les stats avant de fermer l'app
    stats = mgr.get_stats()
    assert stats["done"] == 2
    assert stats["todo"] == 1

    # 6. Il sauvegarde
    save_tasks(str(fichier), mgr.list_tasks(sort_by="id"))

    # 7. Il relance l'app le lendemain : les taches doivent etre la
    mgr2 = TaskManager()
    mgr2.replace_all(load_tasks(str(fichier)))
    assert mgr2.get_stats()["total"] == 3
    assert mgr2.get_stats()["done"] == 2
