"""Persistance JSON des taches."""

import json
from pathlib import Path
from .task import Task
from .exceptions import StorageError


def save_tasks(file_path, tasks):
    try:
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        data = [task.to_dict() for task in tasks]
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    except OSError as e:
        raise StorageError(f"Impossible d'ecrire dans {file_path} : {e}")


def load_tasks(file_path):
    path = Path(file_path)
    if not path.exists():
        return []
    try:
        raw = path.read_text(encoding="utf-8")
        if not raw.strip():
            return []
        data = json.loads(raw)
        return [Task.from_dict(d) for d in data]
    except json.JSONDecodeError as e:
        raise StorageError(f"Fichier JSON corrompu ({file_path}) : {e}")
    except OSError as e:
        raise StorageError(f"Impossible de lire {file_path} : {e}")
