#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script final pour corriger les derniers problèmes de formatage Markdown
"""

import os
import re
from pathlib import Path

def final_cleanup(content):
    """Nettoyage final et ciblé"""
    
    # 1. Corrige les titres de niveau 5 mal placés
    content = re.sub(r'##### \[([^\]]+)\]\(URL\)', r'### [\1](URL)', content)
    
    # 2. Sépare les liens qui sont collés
    content = re.sub(r'\]\(URL\)\[', '](URL)\n\n[', content)
    
    # 3. Corrige les listes mal formatées avec des éléments collés
    # Trouve les patterns comme "- **Titre** texte- **Autre titre**"
    content = re.sub(r'(- \*\*[^*]+\*\*[^-]*?)- \*\*', r'\1\n\n- **', content)
    
    # 4. Sépare les mots collés dans le texte (comme "rmai" qui devrait être "r mai")
    content = re.sub(r'([a-z])rmai([a-z])', r'\1r mai\2', content)
    content = re.sub(r'rmai ntenir', 'maintenir', content)
    content = re.sub(r'rmai ntenant', 'maintenant', content)
    content = re.sub(r'dro rmai ne', 'domaine', content)
    
    # 5. Corrige les espaces manquants après les points
    content = re.sub(r'\.([A-ZÉÈÊËÀÂÄÔÖÛÜÇÎÏ])', r'. \1', content)
    
    # 6. Sépare les éléments de liste collés
    content = re.sub(r'(\*\*[^*]+\*\* [^-]+?)([A-Z][a-z]+ [A-Z])', r'\1\n\n- **\2', content)
    
    # 7. Corrige les liens consécutifs avec des catégories
    content = re.sub(r'\[([^\]]+)\]\(URL\)([A-Z][a-z]+ [a-z]+)', r'[\1](URL) - \2', content)
    
    # 8. Ajoute des sauts de ligne avant les nouveaux paragraphes
    content = re.sub(r'([.!?])([A-ZÉÈÊËÀÂÄÔÖÛÜÇÎÏ][a-z]+ [a-z]+ [a-z]+)', r'\1\n\n\2', content)
    
    # 9. Corrige les listes avec des tirets manquants
    content = re.sub(r'^([A-ZÉÈÊËÀÂÄÔÖÛÜÇÎÏ][^.!?]*[.!?])$', r'- \1', content, flags=re.MULTILINE)
    
    # 10. Nettoie les espaces multiples
    content = re.sub(r' {2,}', ' ', content)
    
    # 11. Corrige les sauts de ligne multiples
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    return content

def restructure_lists(content):
    """Restructure spécifiquement les listes mal formatées"""
    lines = content.split('\n')
    result = []
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Si on trouve une ligne qui contient plusieurs éléments de liste
        if '- **' in line and line.count('- **') > 1:
            # Sépare les éléments
            parts = re.split(r'(- \*\*[^*]+\*\*[^-]*)', line)
            for part in parts:
                if part.strip() and '- **' in part:
                    result.append(part.strip())
                    result.append('')
        else:
            result.append(line)
        
        i += 1
    
    return '\n'.join(result)

def fix_specific_content_issues(content):
    """Corrige des problèmes spécifiques identifiés dans le contenu"""
    
    # Corrige les mots techniques mal séparés
    replacements = {
        'Stratégies RSE Innovantes Exploration': 'Stratégies RSE Innovantes** : Exploration',
        'Tendances Émergentes en Développement Durable Analyse': 'Tendances Émergentes en Développement Durable** : Analyse',
        'Études de Cas Inspirantes Présentation': 'Études de Cas Inspirantes** : Présentation',
        'Normes et Certifications en RSEDémystification': 'Normes et Certifications en RSE** : Démystification',
        'Accès à Nos Publications Toutes': 'Accès à Nos Publications** : Toutes',
        'Contribuez à la Conversation Nous': 'Contribuez à la Conversation** : Nous'
    }
    
    for old, new in replacements.items():
        content = content.replace(old, new)
    
    # Corrige les listes mal formatées
    content = re.sub(r'- \*\*([^*]+)\*\* ([^-]+?)([A-Z][a-z]+ [A-Z])', r'- **\1** : \2\n\n- **\3', content)
    
    return content

def process_file(file_path):
    """Traite un fichier avec toutes les corrections finales"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Applique toutes les corrections
        content = final_cleanup(content)
        content = restructure_lists(content)
        content = fix_specific_content_issues(content)
        
        # Sauvegarde
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"Erreur lors du traitement de {file_path}: {e}")
        return False

def main():
    """Fonction principale"""
    base_dir = Path(r'c:\wamp64\www\esg_strategies\labs')
    
    print("=== Correction finale du formatage Markdown ===")
    
    total_processed = 0
    total_errors = 0
    
    # Traite tous les fichiers Markdown
    for folder in ['pages', 'articles']:
        folder_path = base_dir / folder
        if folder_path.exists():
            print(f"\n📁 Traitement du dossier {folder}...")
            for md_file in folder_path.glob('*.md'):
                print(f"  Correction finale: {md_file.name}")
                if process_file(md_file):
                    total_processed += 1
                    print(f"    ✅ Succès")
                else:
                    total_errors += 1
                    print(f"    ❌ Erreur")
    
    # Traite le menu
    menu_file = base_dir / 'menu.md'
    if menu_file.exists():
        print(f"\n📋 Correction finale du menu...")
        if process_file(menu_file):
            total_processed += 1
            print(f"  ✅ Menu corrigé")
        else:
            total_errors += 1
            print(f"  ❌ Erreur menu")
    
    print(f"\n=== Résumé final ===")
    print(f"✅ Fichiers traités: {total_processed}")
    print(f"❌ Erreurs: {total_errors}")
    
    if total_errors == 0:
        print("\n🎉 Correction finale terminée avec succès!")
        print("📝 Le formatage Markdown est maintenant optimisé.")
    else:
        print(f"\n⚠️ {total_errors} erreur(s) rencontrée(s).")

if __name__ == "__main__":
    main()