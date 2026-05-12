// PARTIE 4 - Tests END-TO-END.
// Scenario complet de la vraie vie, du debut a la fin, via les vrais points d'entree.

import { describe, it, expect, beforeEach, afterEach } from "vitest";
import { mkdtempSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { TaskManager } from "../src/taskManager.js";
import { saveTasks, loadTasks } from "../src/storage.js";

describe("E2E - parcours utilisateur complet", () => {
  let tmpDir: string;
  beforeEach(() => {
    tmpDir = mkdtempSync(join(tmpdir(), "tp-e2e-"));
  });
  afterEach(() => {
    rmSync(tmpDir, { recursive: true, force: true });
  });

  it("planifier sa journee, faire des taches, sauvegarder, relancer", () => {
    const fichier = join(tmpDir, "ma_journee.json");

    // 1. Premier lancement de l'app : rien
    const mgr = new TaskManager();
    mgr.replaceAll(loadTasks(fichier));
    expect(mgr.getStats().total).toBe(0);

    // 2. Ajout des 3 taches
    mgr.createTask({ title: "Lire mes mails", priority: "low" });
    mgr.createTask({ title: "Reunion equipe a 10h", priority: "high" });
    mgr.createTask({ title: "Reviser Vitest", priority: "medium" });

    // 3. Tri par priorite : la reunion remonte
    expect(mgr.listTasks({ sortBy: "priority" })[0].title).toBe("Reunion equipe a 10h");

    // 4. L'utilisateur termine 2 taches
    mgr.markDone(1);
    mgr.markDone(2);

    // 5. Verification des stats
    const stats = mgr.getStats();
    expect(stats.done).toBe(2);
    expect(stats.todo).toBe(1);

    // 6. Sauvegarde
    saveTasks(fichier, mgr.listTasks({ sortBy: "id" }));

    // 7. Relance le lendemain : tout doit etre la
    const mgr2 = new TaskManager();
    mgr2.replaceAll(loadTasks(fichier));
    expect(mgr2.getStats().total).toBe(3);
    expect(mgr2.getStats().done).toBe(2);
  });
});
