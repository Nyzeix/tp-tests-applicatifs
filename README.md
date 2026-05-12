# TP Tests Applicatifs — Gestionnaire de Tâches

> Bienvenue. Ce dépôt est ton **terrain d'entraînement complet** pour monter en compétence sur les tests logiciels.
> Tu y trouveras la **même mini-application** implémentée deux fois — une fois en **Python (pytest)**, une fois en **TypeScript (Vitest)** — pour pratiquer **les 8 types de tests** sur un projet réel, et finir avec un dépôt GitHub à toi avec une **CI verte** automatique.

📄 **Le support PDF du TP** (« TP-Tests-Applicatifs.pdf ») t'a été remis par ton formateur. **Tu travailles avec le PDF + ce dépôt** — les deux sont complémentaires.

---

## 🚀 Démarrage 60 secondes

Tu n'as **pas besoin de demander à ton formateur** comment lancer ce projet. Tout est ici.

### Tu choisis Python ?

```bash
cd python
python -m venv .venv
# Windows : .venv\Scripts\activate
# macOS / Linux : source .venv/bin/activate
pip install -r requirements.txt
pytest
```

➡️ Tu dois voir **33 tests verts + 1 rouge** au premier lancement. Le rouge, c'est normal : c'est le test de régression du bug que tu corrigeras en Partie IV.

### Tu choisis TypeScript ?

```bash
cd typescript
npm install
npm test
```

➡️ Tu dois voir **32 tests verts + 1 rouge**. Même logique : le rouge attend que tu corriges le bug en Partie IV.

### Tu veux faire les deux ?

Vas-y. Le code est miroir, les principes sont identiques. C'est même une excellente idée pour mieux mémoriser.

---

## 📦 Contenu de ce dépôt

```
.
├── README.md                  ← tu es ici
├── COMMANDES-GIT.md           ← toutes les commandes Git utiles
├── .gitignore
├── .github/
│   └── workflows/
│       └── ci.yml             ← lance pytest + vitest à chaque push (intégration continue)
│
├── python/                    ← projet Python avec pytest
│   ├── requirements.txt
│   ├── pytest.ini
│   ├── src/                   ← code source (contient au moins 1 bug volontaire à trouver)
│   │   ├── task.py            ← modèle Task
│   │   ├── task_manager.py    ← logique métier (← bug-001 caché ici)
│   │   ├── storage.py         ← persistance JSON
│   │   ├── validators.py      ← validation des entrées
│   │   ├── exceptions.py
│   │   └── app.py             ← CLI interactive
│   ├── tests/                 ← 1 fichier de tests par type
│   │   ├── conftest.py
│   │   ├── test_unitaire_task.py
│   │   ├── test_unitaire_validators.py
│   │   ├── test_cas_limites.py
│   │   ├── test_entrees_invalides.py
│   │   ├── test_integration.py
│   │   ├── test_fonctionnel.py
│   │   ├── test_e2e.py
│   │   └── test_regression.py
│   └── data/                  ← stockage JSON local
│
└── typescript/                ← MÊME projet en TypeScript + Vitest
    ├── package.json
    ├── tsconfig.json
    ├── vitest.config.ts
    ├── src/
    │   ├── task.ts
    │   ├── taskManager.ts     ← bug-001 caché ici aussi
    │   ├── storage.ts
    │   ├── validators.ts
    │   ├── errors.ts
    │   └── app.ts
    ├── tests/
    │   ├── unitaire.task.test.ts
    │   ├── unitaire.validators.test.ts
    │   ├── casLimites.test.ts
    │   ├── entreesInvalides.test.ts
    │   ├── integration.test.ts
    │   ├── fonctionnel.test.ts
    │   ├── e2e.test.ts
    │   └── regression.test.ts
    └── data/
```

---

## 🎯 L'application support — « Mini gestionnaire de tâches »

Une application simple, suffisamment riche pour tout pratiquer :

| Fonction | Ce qu'elle fait |
|----------|-----------------|
| `create_task` | Crée une tâche (titre, description, priorité, échéance) |
| `list_tasks` | Liste les tâches, triables par priorité / id / échéance, filtrables par statut |
| `get_task` | Récupère une tâche par son identifiant |
| `mark_done` | Marque une tâche comme terminée |
| `delete_task` | Supprime une tâche (← **attention, bug caché ici**) |
| `get_stats` | Retourne le décompte par statut |
| `save_tasks` / `load_tasks` | Sauvegarde / lecture du JSON |

Données d'une tâche :
- `id` (entier auto-incrémenté)
- `title` (texte 1–100 caractères, requis)
- `description` (texte 0–500, optionnel)
- `priority` parmi `low` / `medium` / `high`
- `status` parmi `todo` / `doing` / `done`
- `due_date` (date ISO `AAAA-MM-JJ`, optionnelle)
- `created_at` (généré automatiquement)

---

## 🧪 Les 8 types de tests pratiqués

| Type de test | Fichier Python | Fichier TypeScript | Question à laquelle il répond |
|--------------|----------------|--------------------|-------------------------------|
| **Unitaire** | `test_unitaire_task.py` | `unitaire.task.test.ts` | Cette fonction toute seule, fait-elle son job ? |
| **Unitaire** | `test_unitaire_validators.py` | `unitaire.validators.test.ts` | Les validateurs vérifient-ils les bonnes règles ? |
| **Cas limites** | `test_cas_limites.py` | `casLimites.test.ts` | Que fait le code aux frontières (0, max, max+1) ? |
| **Entrées invalides** | `test_entrees_invalides.py` | `entreesInvalides.test.ts` | Le code refuse-t-il proprement les mauvaises entrées ? |
| **Intégration** | `test_integration.py` | `integration.test.ts` | Plusieurs modules ensemble, ça fonctionne ? |
| **Fonctionnel** | `test_fonctionnel.py` | `fonctionnel.test.ts` | Du point de vue métier, ça fait ce qu'on attend ? |
| **End-to-End** | `test_e2e.py` | `e2e.test.ts` | Un parcours utilisateur complet, ça marche ? |
| **Régression** | `test_regression.py` | `regression.test.ts` | Le bug-001 ne reviendra-t-il plus jamais ? |
| **Validation** | (transverse : la CI complète) | (transverse) | Le produit fini répond-il à la spec ? |

---

## ⚙️ Lancer l'application interactive (optionnel, pour t'amuser)

### Python

```bash
cd python
python -m src.app data/taches.json
```

### TypeScript

```bash
cd typescript
npm start
```

Un menu CLI s'affiche : ajouter, lister, marquer terminée, supprimer, voir stats, quitter. Joue avec.

---

## 🧭 Comment travailler — les 5 parties du TP

> Suis l'ordre des **5 parties du PDF élève** remis par ton formateur. Chaque partie cible une compétence précise.

| Partie | Mission | Tu travailles dans |
|--------|---------|--------------------|
| I | Faire passer ton premier test, comprendre le pattern AAA | `test_unitaire_*` |
| II | Casser le code aux frontières + entrées invalides | `test_cas_limites`, `test_entrees_invalides` |
| III | Faire dialoguer plusieurs modules + scénarios métier | `test_integration`, `test_fonctionnel` |
| IV | Trouver le bug-001, écrire un test qui échoue, le corriger | `test_regression`, `src/task_manager.py` (ou `.ts`) |
| V | Activer la CI GitHub Actions, viser le badge vert | ton dépôt GitHub + `.github/workflows/ci.yml` |

À chaque fin de partie : **commit + push**.

---

## 🐛 Le bug-001 — indice (sans spoiler)

Quelque part dans `task_manager.py` (et son équivalent TS), **une méthode confond deux notions qui se ressemblent**. Le scénario qui le révèle est documenté en tête du fichier `test_regression.py`. Lis-le, écris le test qui doit échouer, observe le rouge, puis corrige le code.

> **Tu sauras que tu as réussi quand** : les tests de régression passent au vert *sans* avoir supprimé aucun autre test.

---

## 📤 Pousser sur ton propre GitHub

Suis le pas-à-pas dans [COMMANDES-GIT.md](./COMMANDES-GIT.md). Résumé express :

```bash
# Sur GitHub.com : crée un nouveau dépôt vide "tp-tests-applicatifs"

git remote add origin https://github.com/<ton-pseudo>/tp-tests-applicatifs.git
git branch -M main
git push -u origin main
```

Une fois poussé, ouvre l'onglet **Actions** sur GitHub : ta CI tourne automatiquement.

---

## ❓ FAQ — Si ça ne marche pas

| Problème | Solution |
|----------|----------|
| `python: command not found` | Installe Python 3.10+ sur [python.org](https://python.org). Sous Windows, coche "Add to PATH" pendant l'installation. |
| `pip install` est très lent | Normal au premier lancement. Patiente. Pour le coup d'après, l'env virtuel `.venv` est mis en cache. |
| `pytest` plante avec `ModuleNotFoundError: src` | Tu n'es probablement pas dans le dossier `python/`. Fais `cd python` d'abord. |
| `npm: command not found` | Installe Node.js LTS sur [nodejs.org](https://nodejs.org). |
| `npm install` échoue | Supprime `node_modules/` et `package-lock.json`, puis relance `npm install`. |
| Vitest dit "no test files found" | Vérifie que tu es dans le dossier `typescript/` et que tes fichiers terminent par `.test.ts`. |
| Mes tests passent en local mais la CI est rouge | Vérifie que tu as bien commit + push **tous** tes fichiers. Souvent c'est un fichier oublié. Lis les logs GitHub Actions, ils sont explicites. |
| Je ne trouve pas le bug-001 | Relis attentivement la méthode `delete_task`. Demande-toi : qu'est-ce qu'on lui passe en argument ? Comment l'utilise-t-elle ? |

---

## ✅ Validation finale (avant de rendre)

Coche cette mini-checklist avant de remettre ton lien GitHub :

- [ ] `pytest` est tout vert dans `python/`
- [ ] `npm test` est tout vert dans `typescript/`
- [ ] Le bug-001 est corrigé, le test de régression est en vert
- [ ] Tous les `TODO ÉLÈVE` sont remplis (≥ 1 test ajouté par fichier)
- [ ] CI GitHub Actions verte sur la branche `main`
- [ ] Badge CI dans ce README (voir COMMANDES-GIT.md section "Badge CI")
- [ ] Section "Ce que j'ai appris" ajoutée en bas du README
- [ ] Au moins 10 commits clairs en convention `type(scope): message`

---

## 📚 Lexique express

| Mot | Définition de poche |
|-----|---------------------|
| **AAA** | Arrange / Act / Assert — la structure d'un test propre |
| **Fixture** | Donnée préparée à l'avance, partagée entre plusieurs tests |
| **Couverture** | % du code source touché par au moins un test |
| **CI** | Continuous Integration — un robot qui relance tes tests à chaque push |
| **Régression** | Un bug qui revient après avoir été corrigé une fois |
| **AAA-pattern** | la structure (Arrange, Act, Assert) qui rend un test lisible |
| **Marker** | étiquette pytest (`@pytest.mark.unitaire`) pour filtrer les tests |
| **Flaky test** | test qui passe ou échoue de façon aléatoire (mauvais — à corriger) |

---

## 🏆 Trophée final

Quand tu auras une **CI verte** avec le badge dans ce README, tu pourras montrer ce dépôt en stage / entretien / portfolio. Ce n'est pas un exercice scolaire de plus : c'est ta **première vraie carte de visite de développeur testeur**.

Bon TP. 🚀
