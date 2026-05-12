"""CLI interactive du gestionnaire de taches.

Exemple d'usage :
    python -m src.app data/taches.json
"""

import sys
from pathlib import Path

from .task_manager import TaskManager
from .storage import save_tasks, load_tasks
from .exceptions import TaskError


MENU = """
==============================
  Gestionnaire de Taches CLI
==============================
1) Ajouter une tache
2) Lister les taches
3) Marquer une tache comme terminee
4) Supprimer une tache
5) Statistiques
6) Quitter
> """


def run(data_path):
    manager = TaskManager()
    manager.replace_all(load_tasks(data_path))

    while True:
        choice = input(MENU).strip()
        try:
            if choice == "1":
                title = input("Titre : ")
                desc = input("Description (optionnelle) : ")
                prio = input("Priorite (low/medium/high) [medium] : ") or "medium"
                due = input("Echeance AAAA-MM-JJ (optionnelle) : ") or None
                task = manager.create_task(title, desc, prio, due)
                print(f"Cree : {task}")
            elif choice == "2":
                tasks = manager.list_tasks(sort_by="priority")
                if not tasks:
                    print("(aucune tache)")
                for t in tasks:
                    flag = "[X]" if t.status == "done" else "[ ]"
                    print(f"  #{t.id} {flag} [{t.priority:6}] {t.title}")
            elif choice == "3":
                task_id = int(input("ID a marquer terminee : "))
                manager.mark_done(task_id)
                print("Marquee terminee.")
            elif choice == "4":
                task_id = int(input("ID a supprimer : "))
                manager.delete_task(task_id)
                print("Supprimee.")
            elif choice == "5":
                print(manager.get_stats())
            elif choice == "6":
                save_tasks(data_path, manager.list_tasks(sort_by="id"))
                print("Sauvegarde. A bientot.")
                return
            else:
                print("Choix inconnu.")
        except (TaskError, ValueError) as e:
            print(f"Erreur : {e}")


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "data/taches.json"
    run(path)
