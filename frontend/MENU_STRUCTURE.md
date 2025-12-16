# Structure du Menu - ESG Stratégies

## Menu Principal (Navigation Horizontale)

### 1. Accueil
- **Route**: `/`
- **Description**: Page d'accueil avec présentation générale

### 2. Qui sommes-nous ?
- **Route**: `/qui-sommes-nous`
- **Description**: Présentation de l'entreprise
- **Sous-pages**:
  - Vision, Mission, Valeurs (`/vision-mission-valeurs`)
  - Pourquoi nous choisir ? (`/pourquoi-nous-choisir`)

### 3. Nos Services
- **Route**: `/nos-services`
- **Description**: Présentation des services
- **Sous-pages**:
  - Conseil Stratégie RSE/DD (`/conseil-strategie-rse-dd`)
  - Certification ESG (`/certification-labelisation-notation-esg`)
  - Engagement Politique RSE/DD (`/engagement-politique-rse-dd`)

### 4. Domaines d'Expertise (Mega Menu)
- **Description**: Les trois piliers ESG
- **Sous-sections**:
  
  #### Environnement
  - Environnement et Ressources Naturelles (`/environnement-et-ressources-naturelles`)
  
  #### Social
  - Société (`/societe`)
  
  #### Gouvernance
  - Gouvernance (`/gouvernance`)

### 5. Formations
- **Route**: `/formations`
- **Description**: Catalogue des formations
- **Sous-pages**:
  - Programme (`/programme`)

### 6. Événements
- **Description**: Événements et conférences
- **Sous-pages**:
  - Conférence Africa Corporate Sustainability (`/africa-corporate-sustainability-conference`)
  - After Work RSE (`/les-after-work-rse`)
  - Récompenses (`/recompenses`)

### 7. Ressources
- **Description**: Publications et contenus
- **Sous-pages**:
  - Publications (`/publications`)
  - News & Articles (`/news-articles`)
  - Blog (`/blog`)

### 8. Partenariat
- **Route**: `/devenez-partenaire`
- **Description**: Opportunités de partenariat

### 9. Contact
- **Route**: `/contact`
- **Description**: Informations de contact

---

## Structure Recommandée pour le Menu

### Menu Principal (Barre de navigation)
```
Accueil | Qui sommes-nous | Services | Expertise ESG | Formations | Événements | Ressources | Partenariat | Contact
```

### Mega Menu pour "Expertise ESG"
```
┌─────────────────────────────────────────────────────────────┐
│ EXPERTISE ESG                                               │
├─────────────────┬─────────────────┬─────────────────────────┤
│ ENVIRONNEMENT   │ SOCIAL          │ GOUVERNANCE             │
│                 │                 │                         │
│ • Ressources    │ • Société       │ • Gouvernance           │
│   Naturelles    │ • Diversité     │ • Éthique               │
│ • Climat        │ • Inclusion     │ • Transparence          │
│ • Biodiversité  │ • Droits        │ • Conformité            │
│                 │   Humains       │                         │
└─────────────────┴─────────────────┴─────────────────────────┘
```

### Menu Dropdown pour "Qui sommes-nous"
- Vision, Mission, Valeurs
- Pourquoi nous choisir ?

### Menu Dropdown pour "Services"
- Conseil Stratégie RSE/DD
- Certification ESG
- Engagement Politique RSE/DD

### Menu Dropdown pour "Événements"
- Conférence Africa Corporate Sustainability
- After Work RSE
- Récompenses

### Menu Dropdown pour "Ressources"
- Publications
- News & Articles
- Blog

---

## Navigation Mobile
Pour mobile, utiliser un menu hamburger avec structure hiérarchique :

```
☰ Menu
├── Accueil
├── Qui sommes-nous
│   ├── Vision, Mission, Valeurs
│   └── Pourquoi nous choisir ?
├── Services
│   ├── Conseil Stratégie RSE/DD
│   ├── Certification ESG
│   └── Engagement Politique RSE/DD
├── Expertise ESG
│   ├── Environnement
│   ├── Social
│   └── Gouvernance
├── Formations
│   └── Programme
├── Événements
│   ├── Conférence
│   ├── After Work RSE
│   └── Récompenses
├── Ressources
│   ├── Publications
│   ├── News & Articles
│   └── Blog
├── Partenariat
└── Contact
```

---

## Priorités d'Affichage

### Menu Principal (Toujours visible)
1. Accueil
2. Qui sommes-nous
3. Services
4. Expertise ESG
5. Contact

### Menu Secondaire (Dropdown/Mega Menu)
- Formations
- Événements
- Ressources
- Partenariat

---

## Notes d'Amélioration

1. **Réduction du nombre d'éléments** : Passer de 20+ éléments à 9 éléments principaux
2. **Hiérarchisation claire** : Groupement logique par thématiques
3. **Mega Menu ESG** : Mise en avant des trois piliers ESG
4. **Navigation intuitive** : Structure logique pour l'utilisateur
5. **Responsive** : Adaptation mobile avec menu hiérarchique
6. **SEO Friendly** : URLs claires et structure logique

---

## Actions à Implémenter

1. ✅ Créer ce fichier de documentation
2. 🔄 Restructurer le menu dans App.vue
3. 🔄 Implémenter le mega menu pour "Expertise ESG"
4. 🔄 Créer les sous-menus dropdown
5. 🔄 Adapter la navigation mobile
6. 🔄 Tester la navigation sur tous les écrans