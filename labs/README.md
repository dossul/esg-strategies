# Documentation ESG Stratégies - Structure Markdown

Ce projet contient la documentation complète du site ESG Stratégies, extraite des fichiers XML WordPress et organisée en structure Markdown.

## 📁 Structure des Dossiers

```
c:\wamp64\www\esg_strategies\labs\
├── menu.md                    # Menu principal et navigation du site
├── pages/                     # Dossier contenant toutes les pages du site (25 pages)
│   ├── Accueil.md
│   ├── Contact.md
│   ├── Nos-Services.md
│   ├── A-Propos.md
│   └── ... (21 autres pages)
├── articles/                  # Dossier contenant tous les articles/posts (6 articles)
│   ├── Publications.md
│   ├── Formations.md
│   ├── Gouvernance.md
│   └── ... (3 autres articles)
└── extract_content.py         # Script d'extraction utilisé
```

## 📋 Contenu Extrait

### Pages (25 au total)
Les pages sont organisées selon leur ordre de menu WordPress :

**Pages Principales (avec ordre de menu défini) :**
- Accueil (Ordre: 10)
- Qui sommes-nous ? (Ordre: 20)
- Africa Corporate Sustainability Conference (Ordre: 30)
- Nos Services (Ordre: 40)
- Environnement et Ressources Naturelles (Ordre: 42)
- Société (Ordre: 44)
- A Propos (Ordre: 50)
- News & articles (Ordre: 50)
- Récompenses (Ordre: 52)
- Programme (Ordre: 54)
- Contact (Ordre: 70)
- Demo design system (Ordre: 990)

**Autres Pages :**
- Blog, Certification/Labélisation et Notation ESG, Conseil en stratégie RSE/DD, Formations, Gouvernance, Publications, etc.

### Articles (6 au total)
Les articles sont organisés par catégories :
- **Conseils :** Conseils en stratégies RSE et DD
- **Environnement :** Environnement et Ressources Naturelles
- **Formations :** Formations
- **Gouvernance :** Gouvernance
- **Publications :** Publications
- **Société :** Société

## 🔧 Fonctionnalités du Script d'Extraction

Le script `extract_content.py` effectue les opérations suivantes :

1. **Analyse des fichiers XML WordPress** (3 fichiers traités)
2. **Extraction des métadonnées** : titre, date, catégories, ordre de menu, liens
3. **Conversion HTML vers Markdown** : 
   - Titres (h1-h6)
   - Paragraphes
   - Liens
   - Texte en gras/italique
   - Listes
4. **Nettoyage des noms de fichiers** : caractères spéciaux remplacés par des tirets
5. **Suppression des doublons** basée sur les titres
6. **Filtrage du contenu** : exclusion des éléments système, navigation, et médias

## 📝 Format des Fichiers Markdown

Chaque fichier Markdown contient :

```markdown
# Titre de la Page/Article

**Date de publication:** [Date]
**Catégories:** [Catégories] (pour les articles)
**Lien original:** [URL]

---

## Résumé
[Extrait si disponible]

## Contenu
[Contenu principal converti en Markdown]
```

## 🚀 Utilisation

1. **Navigation :** Commencez par consulter `menu.md` pour comprendre la structure du site
2. **Pages :** Explorez le dossier `pages/` pour le contenu statique
3. **Articles :** Consultez le dossier `articles/` pour le contenu du blog
4. **Recherche :** Utilisez la recherche de fichiers pour trouver du contenu spécifique

## 📊 Statistiques

- **Total des pages extraites :** 25
- **Total des articles extraits :** 6
- **Fichiers XML traités :** 3
- **Format de sortie :** Markdown (.md)
- **Encodage :** UTF-8

## 🔄 Mise à Jour

Pour mettre à jour la documentation avec de nouveaux contenus XML :

1. Placez les nouveaux fichiers XML dans le répertoire `labs/`
2. Modifiez la liste `xml_files` dans `extract_content.py`
3. Exécutez le script : `python extract_content.py`

---

*Documentation générée automatiquement à partir des exports WordPress ESG Stratégies*