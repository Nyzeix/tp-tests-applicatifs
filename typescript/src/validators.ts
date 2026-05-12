import { InvalidInputError } from "./errors.js";

export type Priority = "low" | "medium" | "high";
export type Status = "todo" | "doing" | "done";

export const VALID_PRIORITIES: Priority[] = ["low", "medium", "high"];
export const VALID_STATUSES: Status[] = ["todo", "doing", "done"];
export const TITLE_MIN = 1;
export const TITLE_MAX = 100;
export const DESCRIPTION_MAX = 500;

export function validateTitle(value: unknown): string {
  if (typeof value !== "string") {
    throw new InvalidInputError("Le titre doit etre une chaine de caracteres.");
  }
  const cleaned = value.trim();
  if (cleaned.length < TITLE_MIN) {
    throw new InvalidInputError("Le titre ne peut pas etre vide.");
  }
  if (cleaned.length > TITLE_MAX) {
    throw new InvalidInputError(`Le titre doit faire au plus ${TITLE_MAX} caracteres.`);
  }
  return cleaned;
}

export function validateDescription(value: unknown): string {
  if (value === undefined || value === null) return "";
  if (typeof value !== "string") {
    throw new InvalidInputError("La description doit etre une chaine de caracteres.");
  }
  const cleaned = value.trim();
  if (cleaned.length > DESCRIPTION_MAX) {
    throw new InvalidInputError(`La description doit faire au plus ${DESCRIPTION_MAX} caracteres.`);
  }
  return cleaned;
}

export function validatePriority(value: unknown): Priority {
  if (!VALID_PRIORITIES.includes(value as Priority)) {
    throw new InvalidInputError(
      `Priorite invalide '${value}'. Valeurs attendues : ${VALID_PRIORITIES.join(", ")}.`
    );
  }
  return value as Priority;
}

export function validateStatus(value: unknown): Status {
  if (!VALID_STATUSES.includes(value as Status)) {
    throw new InvalidInputError(
      `Statut invalide '${value}'. Valeurs attendues : ${VALID_STATUSES.join(", ")}.`
    );
  }
  return value as Status;
}

export function validateDueDate(value: unknown): string | null {
  if (value === undefined || value === null || value === "") return null;
  if (typeof value !== "string") {
    throw new InvalidInputError("La date doit etre une chaine au format AAAA-MM-JJ.");
  }
  const isoRegex = /^\d{4}-\d{2}-\d{2}$/;
  if (!isoRegex.test(value)) {
    throw new InvalidInputError(
      `Date invalide '${value}'. Format attendu : AAAA-MM-JJ (ex : 2026-12-31).`
    );
  }
  const d = new Date(value + "T00:00:00Z");
  if (Number.isNaN(d.getTime()) || d.toISOString().slice(0, 10) !== value) {
    throw new InvalidInputError(`Date invalide '${value}'.`);
  }
  return value;
}
