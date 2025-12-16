#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour corriger le formatage des fichiers Markdown générés
Corrige les mots collés, les liens vides, et améliore le formatage général
"""

import os
import re
from pathlib import Path

def clean_markdown_content(content):
    """Nettoie et améliore le formatage du contenu Markdown"""
    
    # 1. Supprime les liens vides [](URL)
    content = re.sub(r'\[\]\([^)]*\)', '', content)
    
    # 2. Corrige les espaces autour des liens
    content = re.sub(r'\]\([^)]*\)\[', '](URL) [', content)
    
    # 3. Ajoute des espaces après les dates et avant les liens
    content = re.sub(r'(\d{4})\[', r'\1 [', content)
    content = re.sub(r'(\d{1,2}, \d{4})\[', r'\1 [', content)
    
    # 4. Corrige les listes mal formatées
    content = re.sub(r':-\s*([A-Z])', r':\n\n- **\1', content)
    content = re.sub(r'([a-z])-\s*([A-Z])', r'\1\n\n- **\2', content)
    
    # 5. Ajoute des espaces après les points et avant les majuscules
    content = re.sub(r'\.([A-Z])', r'. \1', content)
    
    # 6. Corrige les titres collés
    content = re.sub(r'([a-z])#', r'\1\n\n#', content)
    
    # 7. Ajoute des sauts de ligne avant les titres
    content = re.sub(r'([.!?])\s*(#{1,6}\s)', r'\1\n\n\2', content)
    
    # 8. Corrige les espaces multiples
    content = re.sub(r' {2,}', ' ', content)
    
    # 9. Corrige les sauts de ligne multiples
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # 10. Ajoute des espaces après les virgules si manquants
    content = re.sub(r',([A-Za-z])', r', \1', content)
    
    # 11. Corrige les listes avec tirets
    content = re.sub(r'([a-z])\s*-\s*([A-Z])', r'\1\n\n- \2', content)
    
    # 12. Nettoie les liens consécutifs
    content = re.sub(r'\]\([^)]*\)\s*\[([^\]]*)\]\([^)]*\)', r'](URL) - [\1](URL)', content)
    
    # 13. Corrige les mots collés avec des majuscules
    content = re.sub(r'([a-z])([A-Z][a-z])', r'\1 \2', content)
    
    # 14. Ajoute des espaces autour des mots importants
    content = re.sub(r'([a-z])(RSE|ESG|DD|ISO)', r'\1 \2', content)
    content = re.sub(r'(RSE|ESG|DD|ISO)([a-z])', r'\1 \2', content)
    
    # 15. Corrige les dates collées
    content = re.sub(r'([a-z])(\d{1,2}\s+(janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre))', r'\1 \2', content, flags=re.IGNORECASE)
    
    # 16. Améliore le formatage des listes
    lines = content.split('\n')
    improved_lines = []
    
    for i, line in enumerate(lines):
        # Si la ligne commence par un tiret, s'assurer qu'il y a un espace après
        if re.match(r'^-[A-Za-z]', line):
            line = re.sub(r'^-([A-Za-z])', r'- \1', line)
        
        # Si la ligne contient des éléments de liste collés
        if '- ' in line and not line.startswith('- '):
            parts = line.split('- ')
            if len(parts) > 1:
                improved_lines.append(parts[0].strip())
                for part in parts[1:]:
                    if part.strip():
                        improved_lines.append(f"- {part.strip()}")
                continue
        
        improved_lines.append(line)
    
    content = '\n'.join(improved_lines)
    
    # 17. Derniers nettoyages
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
    content = content.strip()
    
    return content

def fix_markdown_file(file_path):
    """Corrige un fichier Markdown spécifique"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Applique les corrections
        cleaned_content = clean_markdown_content(content)
        
        # Sauvegarde le fichier corrigé
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)
        
        return True
    except Exception as e:
        print(f"Erreur lors de la correction de {file_path}: {e}")
        return False

def fix_all_markdown_files(base_dir):
    """Corrige tous les fichiers Markdown dans les dossiers pages et articles"""
    base_path = Path(base_dir)
    
    # Dossiers à traiter
    folders = ['pages', 'articles']
    
    total_fixed = 0
    total_errors = 0
    
    for folder in folders:
        folder_path = base_path / folder
        if not folder_path.exists():
            print(f"Dossier non trouvé: {folder_path}")
            continue
        
        print(f"\n=== Correction des fichiers dans {folder}/ ===")
        
        # Traite tous les fichiers .md dans le dossier
        for md_file in folder_path.glob('*.md'):
            print(f"Correction de: {md_file.name}")
            if fix_markdown_file(md_file):
                total_fixed += 1
                print(f"  ✓ Corrigé avec succès")
            else:
                total_errors += 1
                print(f"  ✗ Erreur lors de la correction")
    
    # Corrige aussi le fichier menu.md
    menu_file = base_path / 'menu.md'
    if menu_file.exists():
        print(f"\n=== Correction du fichier menu.md ===")
        if fix_markdown_file(menu_file):
            total_fixed += 1
            print(f"  ✓ menu.md corrigé avec succès")
        else:
            total_errors += 1
            print(f"  ✗ Erreur lors de la correction de menu.md")
    
    print(f"\n=== Résumé ===")
    print(f"Fichiers corrigés avec succès: {total_fixed}")
    print(f"Erreurs rencontrées: {total_errors}")
    
    return total_fixed, total_errors

def main():
    """Fonction principale"""
    base_dir = r'c:\wamp64\www\esg_strategies\labs'
    
    print("=== Correction du formatage des fichiers Markdown ===")
    print(f"Répertoire de base: {base_dir}")
    
    fixed, errors = fix_all_markdown_files(base_dir)
    
    if errors == 0:
        print("\n🎉 Toutes les corrections ont été appliquées avec succès!")
    else:
        print(f"\n⚠️  {errors} erreur(s) rencontrée(s) lors de la correction.")

if __name__ == "__main__":
    main()