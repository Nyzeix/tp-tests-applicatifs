/**
 * CLI interactive (minimaliste) du gestionnaire de taches.
 * Usage : npx tsx src/app.ts data/taches.json
 */

import { createInterface } from "node:readline";
import { TaskManager } from "./taskManager.js";
import { loadTasks, saveTasks } from "./storage.js";
import { TaskError } from "./errors.js";
import type { Priority } from "./validators.js";

const MENU = `
==============================
  Gestionnaire de Taches CLI
==============================
1) Ajouter une tache
2) Lister les taches
3) Marquer une tache comme terminee
4) Supprimer une tache
5) Statistiques
6) Quitter
> `;

function ask(rl: ReturnType<typeof createInterface>, q: string): Promise<string> {
  return new Promise((res) => rl.question(q, res));
}

async function main() {
  const path = process.argv[2] ?? "data/taches.json";
  const mgr = new TaskManager();
  mgr.replaceAll(loadTasks(path));

  const rl = createInterface({ input: process.stdin, output: process.stdout });

  while (true) {
    const choice = (await ask(rl, MENU)).trim();
    try {
      if (choice === "1") {
        const title = await ask(rl, "Titre : ");
        const description = await ask(rl, "Description (optionnelle) : ");
        const priority = ((await ask(rl, "Priorite (low/medium/high) [medium] : ")) || "medium") as Priority;
        const dueDate = (await ask(rl, "Echeance AAAA-MM-JJ (optionnelle) : ")) || null;
        const task = mgr.createTask({ title, description, priority, dueDate });
        console.log(`Cree : #${task.id} ${task.title}`);
      } else if (choice === "2") {
        const tasks = mgr.listTasks({ sortBy: "priority" });
        if (tasks.length === 0) console.log("(aucune tache)");
        for (const t of tasks) {
          const flag = t.status === "done" ? "[X]" : "[ ]";
          console.log(`  #${t.id} ${flag} [${t.priority.padEnd(6)}] ${t.title}`);
        }
      } else if (choice === "3") {
        const id = parseInt(await ask(rl, "ID a marquer terminee : "), 10);
        mgr.markDone(id);
        console.log("Marquee terminee.");
      } else if (choice === "4") {
        const id = parseInt(await ask(rl, "ID a supprimer : "), 10);
        mgr.deleteTask(id);
        console.log("Supprimee.");
      } else if (choice === "5") {
        console.log(mgr.getStats());
      } else if (choice === "6") {
        saveTasks(path, mgr.listTasks({ sortBy: "id" }));
        console.log("Sauvegarde. A bientot.");
        rl.close();
        return;
      } else {
        console.log("Choix inconnu.");
      }
    } catch (e) {
      if (e instanceof TaskError) console.log(`Erreur : ${e.message}`);
      else throw e;
    }
  }
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
