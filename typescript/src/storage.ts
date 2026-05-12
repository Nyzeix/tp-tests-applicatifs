import { readFileSync, writeFileSync, existsSync, mkdirSync } from "node:fs";
import { dirname } from "node:path";
import { Task } from "./task.js";
import { StorageError } from "./errors.js";

export function saveTasks(filePath: string, tasks: Task[]): void {
  try {
    mkdirSync(dirname(filePath), { recursive: true });
    const data = tasks.map((t) => t.toDict());
    writeFileSync(filePath, JSON.stringify(data, null, 2), "utf-8");
  } catch (e) {
    throw new StorageError(`Impossible d'ecrire dans ${filePath} : ${(e as Error).message}`);
  }
}

export function loadTasks(filePath: string): Task[] {
  if (!existsSync(filePath)) return [];
  try {
    const raw = readFileSync(filePath, "utf-8");
    if (!raw.trim()) return [];
    const data = JSON.parse(raw);
    return (data as any[]).map((d) => Task.fromDict(d));
  } catch (e) {
    throw new StorageError(`Lecture impossible de ${filePath} : ${(e as Error).message}`);
  }
}
