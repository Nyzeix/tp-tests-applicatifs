"""Fixtures partagees par tous les tests."""

import pytest
from src.task_manager import TaskManager


@pytest.fixture
def empty_manager():
    """Un gestionnaire totalement vide, repartant a id=1."""
    return TaskManager()


@pytest.fixture
def manager_with_3_tasks():
    """Un gestionnaire pre-rempli avec 3 taches (ids 1, 2, 3)."""
    mgr = TaskManager()
    mgr.create_task("Acheter du pain", priority="low")
    mgr.create_task("Reviser pytest", priority="high")
    mgr.create_task("Push GitHub", priority="medium")
    return mgr
