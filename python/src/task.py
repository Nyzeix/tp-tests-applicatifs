"""Modele Task : representation d'une tache unique."""

from datetime import datetime, timezone
from .validators import (
    validate_title,
    validate_description,
    validate_priority,
    validate_status,
    validate_due_date,
)


class Task:
    def __init__(self, id, title, description="", priority="medium",
                 status="todo", due_date=None, created_at=None):
        self.id = id
        self.title = validate_title(title)
        self.description = validate_description(description)
        self.priority = validate_priority(priority)
        self.status = validate_status(status)
        self.due_date = validate_due_date(due_date)
        self.created_at = created_at or datetime.now(timezone.utc).replace(tzinfo=None).isoformat(timespec="seconds")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "status": self.status,
            "due_date": self.due_date,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            title=data["title"],
            description=data.get("description", ""),
            priority=data.get("priority", "medium"),
            status=data.get("status", "todo"),
            due_date=data.get("due_date"),
            created_at=data.get("created_at"),
        )

    def __repr__(self):
        return f"Task(id={self.id}, title={self.title!r}, status={self.status})"

    def __eq__(self, other):
        if not isinstance(other, Task):
            return NotImplemented
        return self.to_dict() == other.to_dict()
