# Via CheatSheet

Installer `requirements.txt`

## Utilisation

Lancer `py main.py`. Le programme va alors vous demandez votre nom et prénom. Finalement, le programe lancera chrome pour remplir le formulaire.

## Arguments

- `--offset #` : recule le jour de départ de # jours
- `--work` : permet de préciser une suite précise d'évènement à remplir (e.g : `--work "Cours" "Projet" "Kahoot" "Malade" "Projet" "Projet" "Dojo" "Projet" "Cours"`)

## Exemple

Avec `--work`:

```shell
> py main.py --work "Cours" "Projet" "Kahoot" "Malade" "Projet" "Projet" "Dojo" "Projet" "Cours"
```

Avec `--offset`:

```shell
> py main.py --offset 3
```
