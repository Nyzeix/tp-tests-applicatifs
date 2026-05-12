"""PARTIE 2 - Casser les fonctions : tests des CAS LIMITES.

Un cas limite, c'est la frontiere :
    - longueur 0, longueur 1, longueur max, longueur max + 1
    - liste vide, liste a 1 element, gros volume
    - bornes numeriques (0, -1, INT_MAX...)
"""

import pytest
from src.exceptions import InvalidInputError
from src.task import Task
from src.task_manager import TaskManager
from src.validators import TITLE_MAX, validate_due_date, validate_title


@pytest.mark.cas_limites
def test_titre_un_seul_caractere_est_accepte():
    t = Task(id=1, title="A")
    assert t.title == "A"


@pytest.mark.cas_limites
def test_titre_a_la_longueur_max_est_accepte():
    titre = "x" * TITLE_MAX
    t = Task(id=1, title=titre)
    assert len(t.title) == TITLE_MAX


@pytest.mark.cas_limites
def test_lister_un_manager_vide_renvoie_liste_vide():
    mgr = TaskManager()
    assert mgr.list_tasks() == []


@pytest.mark.cas_limites
def test_lister_une_seule_tache_renvoie_un_element(empty_manager):
    empty_manager.create_task("Une seule")
    assert len(empty_manager.list_tasks()) == 1


@pytest.mark.cas_limites
def test_filtre_statut_inexistant_dans_le_lot_renvoie_liste_vide(manager_with_3_tasks):
    # toutes les taches creees sont en "todo", aucune en "done"
    assert manager_with_3_tasks.list_tasks(status_filter="done") == []


@pytest.mark.cas_limites
def test_get_stats_sur_manager_vide(empty_manager):
    assert empty_manager.get_stats() == {"todo": 0, "doing": 0, "done": 0, "total": 0}


# ------------------------------------------------------------------
# TODO ELEVE : ajoutez au moins 2 tests de cas limites.
# Pistes : titre apres trim qui devient vide, beaucoup de taches (1000),
# date au 29 fevrier d'une annee non bissextile.
# ------------------------------------------------------------------

@pytest.mark.cas_limites
def test_titre_apres_trim_devient_vide_rejete():
    with pytest.raises(InvalidInputError):
        validate_title("   ")

@pytest.mark.cas_limites
def test_creer_1000_taches_dans_le_manager():
    mgr = TaskManager()
    for i in range(1000):
        mgr.create_task(f"Tache {i}")
    assert len(mgr.list_tasks()) == 1000

@pytest.mark.cas_limites
def test_date_29_fevrier_annee_non_bissextile_rejetee():
    with pytest.raises(InvalidInputError):
        validate_due_date("2021-02-29")