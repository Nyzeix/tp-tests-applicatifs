export class TaskError extends Error {
  constructor(message: string) {
    super(message);
    this.name = "TaskError";
  }
}

export class InvalidInputError extends TaskError {
  constructor(message: string) {
    super(message);
    this.name = "InvalidInputError";
  }
}

export class TaskNotFoundError extends TaskError {
  constructor(message: string) {
    super(message);
    this.name = "TaskNotFoundError";
  }
}

export class StorageError extends TaskError {
  constructor(message: string) {
    super(message);
    this.name = "StorageError";
  }
}
