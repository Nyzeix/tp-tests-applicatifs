"""PARTIE 3 - Tests FONCTIONNELS.

On verifie un comportement metier coherent du point de vue de l'utilisateur.
Pas de details d'implementation : seuls les RESULTATS observables comptent.
"""

import pytest
from src.task_manager import TaskManager
from src.exceptions import TaskNotFoundError


@pytest.mark.fonctionnel
def test_creer_une_tache_la_rend_listable():
    mgr = TaskManager()
    mgr.create_task("Aller a la salle de sport")
    titres = [t.title for t in mgr.list_tasks()]
    assert "Aller a la salle de sport" in titres


@pytest.mark.fonctionnel
def test_marquer_done_change_les_stats():
    mgr = TaskManager()
    mgr.create_task("A faire")
    mgr.create_task("Aussi a faire")
    mgr.mark_done(1)
    stats = mgr.get_stats()
    assert stats["done"] == 1
    assert stats["todo"] == 1


@pytest.mark.fonctionnel
def test_liste_triee_par_priorite_descendante(manager_with_3_tasks):
    triees = manager_with_3_tasks.list_tasks(sort_by="priority")
    priorites = [t.priority for t in triees]
    assert priorites == ["high", "medium", "low"]


@pytest.mark.fonctionnel
def test_get_task_inexistante_leve_une_erreur_explicite(empty_manager):
    with pytest.raises(TaskNotFoundError):
        empty_manager.get_task(999)
