// PARTIE 1 - Premier test vert : tests UNITAIRES sur la classe Task.
// Pattern AAA : Arrange / Act / Assert.

import { describe, it, expect } from "vitest";
import { Task } from "../src/task.js";

describe("Task (unitaire)", () => {
  it("se cree avec un titre", () => {
    // Arrange
    const titre = "Faire les courses";
    // Act
    const tache = new Task({ id: 1, title: titre });
    // Assert
    expect(tache.title).toBe(titre);
  });

  it("garde son id", () => {
    const tache = new Task({ id: 42, title: "Apprendre Vitest" });
    expect(tache.id).toBe(42);
  });

  it("demarre en statut 'todo' par defaut", () => {
    const tache = new Task({ id: 1, title: "Demarrer le projet" });
    expect(tache.status).toBe("todo");
  });

  it("a une priorite 'medium' par defaut", () => {
    const tache = new Task({ id: 1, title: "Une tache" });
    expect(tache.priority).toBe("medium");
  });

  it("expose toDict() avec les bons champs", () => {
    const tache = new Task({ id: 1, title: "Voyager", priority: "high" });
    const d = tache.toDict();
    expect(d.id).toBe(1);
    expect(d.title).toBe("Voyager");
    expect(d.priority).toBe("high");
    expect(d.createdAt).toBeDefined();
  });


  // TODO ELEVE : ajoutez au moins 2 tests unitaires supplementaires ici.
  it("A une description vide par defaut", () => {
    const tache = new Task({ id: 2, title: "Tache sans description" });
    expect(tache.description).toBe("");
  });

  it("Respecte l'ordre low < medium < high", () => {
    const ordre: Record<"low" | "medium" | "high", number> = { low: 1, medium: 2, high: 3 };

    const low = new Task({ id: 1, title: "A", priority: "low" });
    const medium = new Task({ id: 2, title: "B", priority: "medium" });
    const high = new Task({ id: 3, title: "C", priority: "high" });

    expect(ordre[low.priority]).toBeLessThan(ordre[medium.priority]);
    expect(ordre[medium.priority]).toBeLessThan(ordre[high.priority]);
  });

  it("Date au format ISO", () => {
    const tache = new Task({ id: 3, title: "Verifier date" });
    expect(Number.isNaN(Date.parse(tache.createdAt))).toBe(false);
  });
});
