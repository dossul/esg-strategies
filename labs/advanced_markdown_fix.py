#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script avancé pour corriger le formatage des fichiers Markdown
Version améliorée pour traiter les cas complexes
"""

import os
import re
from pathlib import Path

def advanced_markdown_cleanup(content):
    """Nettoyage avancé du contenu Markdown"""
    
    # 1. Supprime complètement les liens vides et malformés
    content = re.sub(r'\[\s*\]\([^)]*\)', '', content)
    content = re.sub(r'\[\s*\]\(URL\)', '', content)
    
    # 2. Nettoie les lignes qui ne contiennent que des tirets et espaces
    content = re.sub(r'^-\s*$', '', content, flags=re.MULTILINE)
    
    # 3. Corrige les dates collées aux liens
    content = re.sub(r'\[([^\]]+)\]\(URL\)([a-zéèêëàâäôöûüçîï]+\s+\d{1,2},?\s+\d{4})', r'[\1](URL) - \2', content, flags=re.IGNORECASE)
    
    # 4. Sépare les mots collés avec des majuscules (CamelCase)
    content = re.sub(r'([a-zéèêëàâäôöûüçîï])([A-ZÉÈÊËÀÂÄÔÖÛÜÇÎÏ][a-zéèêëàâäôöûüçîï])', r'\1 \2', content)
    
    # 5. Corrige les listes mal formatées
    lines = content.split('\n')
    corrected_lines = []
    
    for line in lines:
        # Si la ligne contient plusieurs éléments de liste collés
        if '- **' in line and not line.strip().startswith('- **'):
            # Sépare les éléments de liste
            parts = re.split(r'(- \*\*[^*]+\*\*)', line)
            for part in parts:
                if part.strip():
                    if part.startswith('- **'):
                        corrected_lines.append(part.strip())
                    elif part.strip() and not part.startswith('- '):
                        # Texte avant ou après une liste
                        corrected_lines.append(part.strip())
        else:
            corrected_lines.append(line)
    
    content = '\n'.join(corrected_lines)
    
    # 6. Corrige les éléments de liste qui sont collés ensemble
    content = re.sub(r'(\*\*[^*]+\*\*[^-]*?)- \*\*', r'\1\n\n- **', content)
    
    # 7. Ajoute des espaces après les points suivis de majuscules
    content = re.sub(r'\.([A-ZÉÈÊËÀÂÄÔÖÛÜÇÎÏ])', r'. \1', content)
    
    # 8. Corrige les mots techniques collés
    content = re.sub(r'([a-zéèêëàâäôöûüçîï])(RSE|ESG|DD|ISO|ODD)', r'\1 \2', content)
    content = re.sub(r'(RSE|ESG|DD|ISO|ODD)([a-zéèêëàâäôöûüçîï])', r'\1 \2', content)
    
    # 9. Sépare les phrases collées
    content = re.sub(r'([.!?])([A-ZÉÈÊËÀÂÄÔÖÛÜÇÎÏ][a-zéèêëàâäôöûüçîï])', r'\1 \2', content)
    
    # 10. Corrige les dates françaises collées
    months = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 
              'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']
    for month in months:
        content = re.sub(f'([a-zéèêëàâäôöûüçîï])({month})', f'r\\1 \\2', content, flags=re.IGNORECASE)
        content = re.sub(f'({month})([A-ZÉÈÊËÀÂÄÔÖÛÜÇÎÏ])', f'r\\1 \\2', content, flags=re.IGNORECASE)
    
    # 11. Nettoie les espaces multiples
    content = re.sub(r' {2,}', ' ', content)
    
    # 12. Nettoie les sauts de ligne multiples
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # 13. Supprime les lignes vides qui ne contiennent que des espaces
    lines = content.split('\n')
    cleaned_lines = [line.rstrip() for line in lines]
    content = '\n'.join(cleaned_lines)
    
    # 14. Supprime les lignes qui ne contiennent que des tirets
    content = re.sub(r'^\s*-\s*$', '', content, flags=re.MULTILINE)
    
    return content.strip()

def restructure_content(content):
    """Restructure le contenu pour une meilleure lisibilité"""
    
    lines = content.split('\n')
    restructured = []
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Si c'est un titre
        if line.startswith('#'):
            if restructured and restructured[-1] != '':
                restructured.append('')
            restructured.append(line)
            restructured.append('')
        
        # Si c'est un élément de liste
        elif line.startswith('- '):
            restructured.append(line)
        
        # Si c'est une ligne normale
        elif line:
            restructured.append(line)
        
        # Ligne vide
        else:
            if restructured and restructured[-1] != '':
                restructured.append('')
        
        i += 1
    
    return '\n'.join(restructured)

def fix_specific_issues(content):
    """Corrige des problèmes spécifiques identifiés"""
    
    # Corrige les titres de niveau 5 mal utilisés
    content = re.sub(r'^##### ([^#\n]+)$', r'### \1', content, flags=re.MULTILINE)
    
    # Corrige les listes d'éléments collés
    content = re.sub(r'- \*\*([^*]+)\*\* ([^-]+?)- \*\*', r'- **\1** \2\n\n- **', content)
    
    # Sépare les éléments de contenu collés
    content = re.sub(r'([.!?])([A-Z][a-z]+ [A-Z])', r'\1\n\n\2', content)
    
    # Corrige les liens consécutifs
    content = re.sub(r'\]\(URL\)\s*-\s*\[', '](URL)\n\n[', content)
    
    return content

def process_markdown_file(file_path):
    """Traite un fichier Markdown complet"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Applique toutes les corrections
        content = advanced_markdown_cleanup(content)
        content = fix_specific_issues(content)
        content = restructure_content(content)
        
        # Sauvegarde
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"Erreur: {e}")
        return False

def main():
    """Fonction principale"""
    base_dir = Path(r'c:\wamp64\www\esg_strategies\labs')
    
    print("=== Correction avancée du formatage Markdown ===")
    
    total_processed = 0
    total_errors = 0
    
    # Traite les pages
    pages_dir = base_dir / 'pages'
    if pages_dir.exists():
        print(f"\n📄 Traitement des pages...")
        for md_file in pages_dir.glob('*.md'):
            print(f"  Correction: {md_file.name}")
            if process_markdown_file(md_file):
                total_processed += 1
                print(f"    ✅ Succès")
            else:
                total_errors += 1
                print(f"    ❌ Erreur")
    
    # Traite les articles
    articles_dir = base_dir / 'articles'
    if articles_dir.exists():
        print(f"\n📰 Traitement des articles...")
        for md_file in articles_dir.glob('*.md'):
            print(f"  Correction: {md_file.name}")
            if process_markdown_file(md_file):
                total_processed += 1
                print(f"    ✅ Succès")
            else:
                total_errors += 1
                print(f"    ❌ Erreur")
    
    # Traite le menu
    menu_file = base_dir / 'menu.md'
    if menu_file.exists():
        print(f"\n📋 Traitement du menu...")
        if process_markdown_file(menu_file):
            total_processed += 1
            print(f"  ✅ Menu corrigé")
        else:
            total_errors += 1
            print(f"  ❌ Erreur menu")
    
    print(f"\n=== Résumé final ===")
    print(f"✅ Fichiers traités avec succès: {total_processed}")
    print(f"❌ Erreurs: {total_errors}")
    
    if total_errors == 0:
        print("\n🎉 Toutes les corrections ont été appliquées avec succès!")
        print("📝 Le formatage Markdown a été considérablement amélioré.")
    else:
        print(f"\n⚠️ {total_errors} erreur(s) rencontrée(s).")

if __name__ == "__main__":
    main()