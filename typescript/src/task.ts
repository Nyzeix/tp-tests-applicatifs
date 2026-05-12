import {
  validateTitle,
  validateDescription,
  validatePriority,
  validateStatus,
  validateDueDate,
  type Priority,
  type Status,
} from "./validators.js";

export interface TaskData {
  id: number;
  title: string;
  description: string;
  priority: Priority;
  status: Status;
  dueDate: string | null;
  createdAt: string;
}

export class Task implements TaskData {
  id: number;
  title: string;
  description: string;
  priority: Priority;
  status: Status;
  dueDate: string | null;
  createdAt: string;

  constructor(params: {
    id: number;
    title: string;
    description?: string;
    priority?: Priority;
    status?: Status;
    dueDate?: string | null;
    createdAt?: string;
  }) {
    this.id = params.id;
    this.title = validateTitle(params.title);
    this.description = validateDescription(params.description);
    this.priority = validatePriority(params.priority ?? "medium");
    this.status = validateStatus(params.status ?? "todo");
    this.dueDate = validateDueDate(params.dueDate);
    this.createdAt = params.createdAt ?? new Date().toISOString().split(".")[0];
  }

  toDict(): TaskData {
    return {
      id: this.id,
      title: this.title,
      description: this.description,
      priority: this.priority,
      status: this.status,
      dueDate: this.dueDate,
      createdAt: this.createdAt,
    };
  }

  static fromDict(data: Partial<TaskData> & { id: number; title: string }): Task {
    return new Task({
      id: data.id,
      title: data.title,
      description: data.description,
      priority: data.priority,
      status: data.status,
      dueDate: data.dueDate ?? null,
      createdAt: data.createdAt,
    });
  }
}
