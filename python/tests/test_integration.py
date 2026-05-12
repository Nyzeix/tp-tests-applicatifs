"""PARTIE 3 - Tests d'INTEGRATION.

On teste que plusieurs modules cooperent correctement.
Ici : task_manager + storage (persistance JSON sur disque).
"""

import pytest
from src.task_manager import TaskManager
from src.storage import save_tasks, load_tasks


@pytest.mark.integration
def test_sauvegarder_puis_recharger_preserve_les_taches(tmp_path):
    fichier = tmp_path / "taches.json"
    mgr = TaskManager()
    mgr.create_task("Tache A", priority="low")
    mgr.create_task("Tache B", priority="high")

    save_tasks(str(fichier), mgr.list_tasks(sort_by="id"))

    rechargees = load_tasks(str(fichier))
    assert len(rechargees) == 2
    assert rechargees[0].title == "Tache A"
    assert rechargees[1].priority == "high"


@pytest.mark.integration
def test_chargement_depuis_fichier_inexistant_renvoie_liste_vide(tmp_path):
    fichier = tmp_path / "inexistant.json"
    assert load_tasks(str(fichier)) == []


@pytest.mark.integration
def test_replace_all_remet_le_compteur_id_a_la_bonne_valeur(tmp_path):
    fichier = tmp_path / "taches.json"
    mgr1 = TaskManager()
    mgr1.create_task("Existante")
    save_tasks(str(fichier), mgr1.list_tasks(sort_by="id"))

    mgr2 = TaskManager()
    mgr2.replace_all(load_tasks(str(fichier)))
    nouvelle = mgr2.create_task("Suivante")
    assert nouvelle.id == 2


# ------------------------------------------------------------------
# Eleve

@pytest.mark.integration
def test_edit_task_check_persist(tmp_path):
    fichier = tmp_path / "taches.json"
    mgr = TaskManager()
    tache = mgr.create_task("Tache a editer")
    tache_id = tache.id
    mgr.update_task(tache_id, title="Titre modifie")
    save_tasks(str(fichier), mgr.list_tasks(sort_by="id"))

    rechargees = load_tasks(str(fichier))
    assert len(rechargees) == 1
    assert rechargees[0].id == tache_id
    assert rechargees[0].title == "Titre modifie"


@pytest.mark.integration
def test_filter_task_with_status_done(tmp_path):
    fichier = tmp_path / "taches.json"
    mgr = TaskManager()
    mgr.create_task("Tache a faire")
    tache2 = mgr.create_task("Tache faite")
    mgr.mark_done(tache2.id)
    save_tasks(str(fichier), mgr.list_tasks(sort_by="id"))

    mgr_recharge = TaskManager()
    mgr_recharge.replace_all(load_tasks(str(fichier)))
    done_tasks = mgr_recharge.list_tasks(status_filter="done", sort_by="id")

    assert len(done_tasks) == 1
    assert done_tasks[0].title == "Tache faite"