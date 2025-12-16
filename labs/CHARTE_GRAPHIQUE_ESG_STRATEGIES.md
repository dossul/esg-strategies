# Charte Graphique ESG Stratégies

## 🎨 Identité Visuelle

### Logo Principal
Le logo ESG Stratégies se compose de :
- **ESG** : Lettres colorées représentant les trois piliers
- **Stratégies** : Texte en gris moderne
- Séparateur vertical entre ESG et Stratégies

### Spécifications Techniques des Logos

#### Formats Disponibles
| Fichier | Format | Fond | Usage Recommandé |
|---------|--------|------|------------------|
| `Logo ESG_noire.jpg` | JPG | Blanc opaque | Fonds blancs fixes |
| `Logo ESG_blanc.jpg` | JPG | Noir opaque | Fonds noirs fixes |
| `Logo_ESG_noire-transparent.png` | PNG | Transparent | Fonds clairs variables |
| `Logo_ESG_blanc-transparent.png` | PNG | Transparent | Fonds sombres variables |

#### Règles d'Utilisation
- **PNG transparents** : Privilégier pour le web (flexibilité maximale)
- **JPG avec fond** : Utiliser uniquement si le fond correspond exactement
- **Taille minimum** : 120px de largeur pour garantir la lisibilité
- **Espace de protection** : Minimum 20px autour du logo

### Déclinaisons du Logo

#### Fichiers Disponibles
Les logos sont disponibles dans le dossier `assets/logos/` :

**Versions JPG (avec fond)**
- `Logo ESG_noire.jpg` - Logo couleur sur fond blanc
- `Logo ESG_blanc.jpg` - Logo blanc sur fond noir

**Versions PNG (transparentes)**
- `Logo_ESG_noire-transparent.png` - Logo couleur avec fond transparent
- `Logo_ESG_blanc-transparent.png` - Logo blanc avec fond transparent

#### Version Couleur (Fond Clair)
**Fichiers à utiliser** : `Logo ESG_noire.jpg` ou `Logo_ESG_noire-transparent.png`
- **E** : Vert (#7CB342 ou similaire)
- **S** : Orange/Jaune (#FFA726 ou similaire) 
- **G** : Rouge (#E53935 ou similaire)
- **Stratégies** : Gris foncé (#424242 ou similaire)
- **Séparateur** : Gris (#757575 ou similaire)

#### Version Blanche (Fond Sombre/Footer)
**Fichiers à utiliser** : `Logo ESG_blanc.jpg` ou `Logo_ESG_blanc-transparent.png`
- **ESG** : Blanc (#FFFFFF)
- **Stratégies** : Blanc (#FFFFFF)
- **Séparateur** : Blanc (#FFFFFF)
- À utiliser sur fond noir ou sombre

## 🎯 Palette de Couleurs Principale

### Couleurs ESG (Primaires)
```css
/* Environnement - Vert */
--esg-green: #7CB342;
--esg-green-light: #AED581;
--esg-green-dark: #558B2F;

/* Social - Orange/Jaune */
--esg-orange: #FFA726;
--esg-orange-light: #FFD54F;
--esg-orange-dark: #FF8F00;

/* Gouvernance - Rouge */
--esg-red: #E53935;
--esg-red-light: #EF5350;
--esg-red-dark: #C62828;
```

### Couleurs Neutres
```css
/* Texte principal */
--text-primary: #424242;
--text-secondary: #757575;
--text-light: #BDBDBD;

/* Arrière-plans */
--bg-white: #FFFFFF;
--bg-light: #FAFAFA;
--bg-dark: #212121;
--bg-black: #000000;

/* Bordures */
--border-light: #E0E0E0;
--border-medium: #BDBDBD;
```

### Couleurs d'Accent
```css
/* Succès */
--success: #4CAF50;
--success-light: #81C784;

/* Information */
--info: #2196F3;
--info-light: #64B5F6;

/* Attention */
--warning: #FF9800;
--warning-light: #FFB74D;

/* Erreur */
--error: #F44336;
--error-light: #E57373;
```

## 📝 Typographie

### Police Principale
**Recommandation** : Inter, Roboto, ou system fonts
```css
font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
```

### Hiérarchie Typographique
```css
/* Titres */
h1 { font-size: 2.5rem; font-weight: 700; color: var(--text-primary); }
h2 { font-size: 2rem; font-weight: 600; color: var(--text-primary); }
h3 { font-size: 1.5rem; font-weight: 600; color: var(--text-primary); }
h4 { font-size: 1.25rem; font-weight: 500; color: var(--text-primary); }

/* Corps de texte */
body { font-size: 1rem; font-weight: 400; color: var(--text-secondary); }
.lead { font-size: 1.125rem; font-weight: 400; color: var(--text-primary); }
.small { font-size: 0.875rem; font-weight: 400; color: var(--text-light); }
```

## 🎨 Utilisation des Couleurs

### Contextes d'Application

#### Header/Navigation
- Fond : Blanc (#FFFFFF)
- Logo : Version couleur
- Texte navigation : Gris foncé (#424242)
- Hover : Vert ESG (#7CB342)

#### Footer
- Fond : Noir (#000000) ou gris très foncé (#212121)
- Logo : Version blanche
- Texte : Blanc (#FFFFFF)
- Liens : Blanc avec hover en vert clair

#### Boutons Principaux
```css
/* Bouton primaire */
.btn-primary {
  background: var(--esg-green);
  color: white;
  border: none;
}
.btn-primary:hover {
  background: var(--esg-green-dark);
}

/* Bouton secondaire */
.btn-secondary {
  background: var(--esg-orange);
  color: white;
  border: none;
}

/* Bouton tertiaire */
.btn-outline {
  background: transparent;
  color: var(--esg-green);
  border: 2px solid var(--esg-green);
}
```

#### Sections Thématiques
- **Environnement** : Utiliser les verts (#7CB342, #AED581)
- **Social** : Utiliser les oranges (#FFA726, #FFD54F)
- **Gouvernance** : Utiliser les rouges (#E53935, #EF5350)

## 📐 Espacements et Grille

### Système d'Espacement
```css
/* Unité de base : 8px */
--space-xs: 4px;
--space-sm: 8px;
--space-md: 16px;
--space-lg: 24px;
--space-xl: 32px;
--space-2xl: 48px;
--space-3xl: 64px;
```

### Grille Responsive
```css
/* Container */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 var(--space-md);
}

/* Breakpoints */
--mobile: 768px;
--tablet: 1024px;
--desktop: 1200px;
```

## 🖼️ Utilisation des Images

### Style Photographique
- **Ton** : Professionnel, moderne, humain
- **Couleurs** : Privilégier les tons naturels qui s'harmonisent avec la palette ESG
- **Composition** : Épurée, avec espace pour le texte

### Filtres et Overlays
```css
/* Overlay pour hero sections */
.hero-overlay {
  background: linear-gradient(
    135deg, 
    rgba(124, 179, 66, 0.8) 0%, 
    rgba(66, 66, 66, 0.6) 100%
  );
}

/* Filtre pour images de fond */
.bg-image {
  filter: brightness(0.7) contrast(1.1);
}
```

## 🎯 Applications Spécifiques

### Cards/Cartes
```css
.card {
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  border-top: 4px solid var(--esg-green);
}
```

### Formulaires
```css
.form-input {
  border: 2px solid var(--border-light);
  border-radius: 4px;
  padding: var(--space-md);
}
.form-input:focus {
  border-color: var(--esg-green);
  outline: none;
}
```

### Navigation
```css
.nav-link {
  color: var(--text-primary);
  transition: color 0.3s ease;
}
.nav-link:hover,
.nav-link.active {
  color: var(--esg-green);
}
```

## 📱 Adaptations Mobile

### Logo Mobile
- Utiliser une version compacte si nécessaire
- Maintenir la lisibilité sur petits écrans
- Possibilité d'utiliser uniquement "ESG" en version très compacte

### Couleurs Mobile
- Conserver la même palette
- Attention aux contrastes pour l'accessibilité
- Tester sur différents types d'écrans

## ♿ Accessibilité

### Contrastes Minimum
- Texte normal : Ratio 4.5:1 minimum
- Texte large : Ratio 3:1 minimum
- Éléments interactifs : Ratio 3:1 minimum

### Tests de Couleurs
```css
/* Vérifications WCAG */
--esg-green: #7CB342; /* ✓ Contraste suffisant sur blanc */
--esg-orange: #FFA726; /* ⚠️ Vérifier contraste sur blanc */
--esg-red: #E53935; /* ✓ Contraste suffisant sur blanc */
```

## 📋 Guidelines d'Usage

### À Faire ✅
- Utiliser `Logo_ESG_blanc-transparent.png` ou `Logo ESG_blanc.jpg` sur fond noir/sombre
- Utiliser `Logo_ESG_noire-transparent.png` ou `Logo ESG_noire.jpg` sur fond clair
- Privilégier les versions PNG transparentes pour plus de flexibilité
- Respecter les espacements minimum autour du logo (20px minimum)
- Maintenir les proportions du logo
- Utiliser les couleurs ESG pour les sections thématiques
- Taille minimum de 120px de largeur

### À Éviter ❌
- Déformer ou étirer le logo
- Utiliser `Logo ESG_noire.jpg` sur fond sombre
- Utiliser `Logo ESG_blanc.jpg` sur fond clair
- Modifier les couleurs du logo
- Placer le logo sur des fonds trop chargés
- Utiliser une taille inférieure à 120px de largeur
- Ignorer l'espace de protection autour du logo

### Choix du Fichier Logo

#### Pour Fonds Clairs (blanc, gris clair, couleurs pastel)
1. **Recommandé** : `Logo_ESG_noire-transparent.png`
2. **Alternative** : `Logo ESG_noire.jpg` (uniquement sur fond blanc pur)

#### Pour Fonds Sombres (noir, gris foncé, couleurs vives)
1. **Recommandé** : `Logo_ESG_blanc-transparent.png`
2. **Alternative** : `Logo ESG_blanc.jpg` (uniquement sur fond noir pur)

## 🎨 Exemples d'Application

### Header
```html
<!-- Version avec fond transparent (recommandée) -->
<header style="background: white;">
  <img src="assets/logos/Logo_ESG_noire-transparent.png" alt="ESG Stratégies">
</header>

<!-- Version avec fond blanc -->
<header style="background: white;">
  <img src="assets/logos/Logo ESG_noire.jpg" alt="ESG Stratégies">
</header>
```

### Footer
```html
<!-- Version avec fond transparent (recommandée) -->
<footer style="background: #000000;">
  <img src="assets/logos/Logo_ESG_blanc-transparent.png" alt="ESG Stratégies">
</footer>

<!-- Version avec fond noir -->
<footer style="background: #000000;">
  <img src="assets/logos/Logo ESG_blanc.jpg" alt="ESG Stratégies">
</footer>
```

### Recommandations d'Usage des Fichiers

#### Utilisation Préférentielle
- **PNG Transparents** : À privilégier pour l'intégration web (flexibilité maximale)
  - `Logo_ESG_noire-transparent.png` pour fonds clairs
  - `Logo_ESG_blanc-transparent.png` pour fonds sombres

#### Utilisation Alternative
- **JPG avec fond** : Pour des cas spécifiques où le fond est fixe
  - `Logo ESG_noire.jpg` sur fond blanc uniquement
  - `Logo ESG_blanc.jpg` sur fond noir uniquement

### Section Environnement
```html
<section style="background: linear-gradient(135deg, #7CB342, #AED581);">
  <!-- Utiliser le logo blanc sur ce fond coloré -->
  <img src="assets/logos/Logo_ESG_blanc-transparent.png" alt="ESG Stratégies">
</section>
```

---

*Cette charte graphique assure une cohérence visuelle forte tout en respectant l'identité ESG Stratégies et les meilleures pratiques du web design moderne.*