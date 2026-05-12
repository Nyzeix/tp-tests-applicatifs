# Commandes Git pour ce TP

Toutes les commandes que tu vas utiliser pendant le TP, expliquées une par une.
Garde cette page ouverte à côté de toi.

---

## 0. Avant le TP : configurer ton identité Git (une seule fois sur ta machine)

```bash
git config --global user.name "Ton Prenom Nom"
git config --global user.email "ton.email@exemple.com"
git config --global init.defaultBranch main
```

Vérifie :
```bash
git config --global --list
```

---

## 1. Récupérer le dépôt de départ

**Option A — Tu forkes le dépôt du prof (recommandé) :**

1. Va sur le dépôt template fourni par le prof, clique sur **Fork** en haut à droite.
2. Sur **ton** fork, copie l'URL `Code > HTTPS`.
3. Clone-le :

```bash
git clone https://github.com/<ton-pseudo>/tp-tests-applicatifs.git
cd tp-tests-applicatifs
```

**Option B — Tu pars de zéro (Partie 5) :**

```bash
mkdir tp-tests-applicatifs
cd tp-tests-applicatifs
git init
# tu copies ici les fichiers source fournis
git add .
git commit -m "chore: import initial du projet"
git branch -M main
git remote add origin https://github.com/<ton-pseudo>/tp-tests-applicatifs.git
git push -u origin main
```

---

## 2. Travailler sur une branche (1 partie = 1 branche)

```bash
# Crée et bascule sur une nouvelle branche
git checkout -b partie-1-premier-test

# … tu codes, tu lances les tests …

# Tu regardes ce qui a change
git status
git diff

# Tu ajoutes les fichiers modifies
git add python/tests/test_unitaire_task.py

# Tu commits
git commit -m "test(unitaire): ajoute 3 tests sur la classe Task"

# Tu envoies ta branche sur GitHub
git push -u origin partie-1-premier-test
```

> **Astuce nommage de branche** : `partie-1-…`, `partie-2-…`, … `fix/bug-001-delete-task`.

---

## 3. Format des messages de commit (Conventional Commits)

Adopte ce format simple et pro :

```
<type>(<scope>): <resume court a l'imperatif>

[explication plus longue si necessaire]
```

| Type | Quand l'utiliser |
|------|------------------|
| `feat` | Tu ajoutes une fonctionnalité |
| `fix` | Tu corriges un bug |
| `test` | Tu ajoutes ou modifies des tests |
| `refactor` | Tu réécris sans changer le comportement |
| `docs` | Tu modifies uniquement la doc / README |
| `chore` | Maintenance, dépendances, CI… |

**Exemples de messages pour ce TP :**

```bash
git commit -m "test(unitaire): ajoute tests sur Task.toDict()"
git commit -m "test(cas-limites): borne haute du titre"
git commit -m "test(invalides): rejet de date au format JJ/MM/AAAA"
git commit -m "test(integration): aller-retour save/load preserve les taches"
git commit -m "test(regression): bug-001 delete_task par id"
git commit -m "fix(bug-001): delete_task supprime par id, plus par index"
git commit -m "ci: active GitHub Actions pour pytest et vitest"
```

---

## 4. Ouvrir une Pull Request (et la merger)

```bash
# Ta branche est deja poussee. GitHub te propose un bouton vert "Compare & pull request".
# Sinon, va sur l'onglet "Pull requests" -> "New pull request".
```

Dans la PR, écris :
- **Titre** : `Partie 1 — premier test vert`
- **Description** : ce que tu as fait, les tests ajoutés, ce qui passe ✅ et ce qui reste ⚠️.

Une fois validée :

```bash
# De retour sur main local :
git checkout main
git pull
# Supprime ta branche locale (deja mergee) :
git branch -d partie-1-premier-test
```

---

## 5. Quand quelque chose foire

| Situation | La bonne commande |
|-----------|-------------------|
| Je veux annuler les modifications non commitées d'un fichier | `git restore <fichier>` |
| Je veux annuler tout ce qui est `git add` mais pas encore commité | `git restore --staged <fichier>` |
| Je veux corriger mon dernier commit (message ou contenu) | `git commit --amend` (avant un push !) |
| J'ai poussé un commit nul, je veux en faire un nouveau qui annule | `git revert <sha>` puis `git push` |
| Ma branche est en retard sur `main` | `git pull origin main` |

---

## 6. Le badge CI dans le README (Partie 5)

Quand ta CI passe au vert sur GitHub :

1. Va dans **Actions > CI > … > 3 petits points > Create status badge**.
2. Copie le markdown proposé. Ça ressemble à :

```markdown
![CI](https://github.com/<ton-pseudo>/tp-tests-applicatifs/actions/workflows/ci.yml/badge.svg)
```

3. Colle-le en haut de ton `README.md`, juste sous le titre.
4. Commit + push :

```bash
git add README.md
git commit -m "docs: ajoute le badge CI"
git push
```

🟢 Bravo, tu viens d'arborer ton premier vrai trophée de dev.

---

## 7. Cheat-sheet à mémoriser

```bash
git status             # ou j'en suis ?
git diff               # qu'est-ce qui a change ?
git add <fichier>      # je prepare ce fichier pour le commit
git commit -m "..."    # je grave dans l'historique
git push               # j'envoie sur GitHub
git pull               # je recupere les dernieres modifs
git checkout -b <br>   # je cree une nouvelle branche
git log --oneline -10  # mes 10 derniers commits
```

Toujours, **TOUJOURS**, faire `git status` avant `git add`. C'est ta boussole.
