#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de correction ultra-ciblé pour les derniers problèmes
"""

import os
import re
from pathlib import Path

def ultra_targeted_fix(content):
    """Corrections ultra-ciblées pour les derniers problèmes"""
    
    # 1. Corrige "rmai s" en "mais"
    content = content.replace('rmai s', 'mais')
    
    # 2. Sépare les éléments de liste qui sont encore collés
    content = re.sub(r'(\*\*[^*]+\*\*[^-]*?)- ([A-Z][^*]+\*\*)', r'\1\n\n- **\2', content)
    
    # 3. Corrige les listes mal formatées avec des tirets manquants
    content = re.sub(r'^([A-Z][^*]*\*\* : [^-]+)$', r'- \1', content, flags=re.MULTILINE)
    
    # 4. Ajoute des sauts de ligne entre les sections de publications
    content = re.sub(r'(\*\* : [^-]+\.)- ([A-Z])', r'\1\n\n- **\2', content)
    
    # 5. Corrige spécifiquement le problème dans Publications.md
    content = re.sub(r'entreprise\.- Tendances', 'entreprise.\n\n- **Tendances', content)
    content = re.sub(r'confrontées\.- Études', 'confrontées.\n\n- **Études', content)
    content = re.sub(r'pratiques\.- Normes', 'pratiques.\n\n- **Normes', content)
    content = re.sub(r'élevés\.- Accès', 'élevés.\n\n- **Accès', content)
    content = re.sub(r'positif\.- Contribuez', 'positif.\n\n- **Contribuez', content)
    
    # 6. Ajoute des sauts de ligne avant les titres de niveau 3
    content = re.sub(r'2020### \[', '2020\n\n### [', content)
    
    return content

def process_file(file_path):
    """Traite un fichier avec les corrections ultra-ciblées"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = ultra_targeted_fix(content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"Erreur: {e}")
        return False

def main():
    """Fonction principale"""
    base_dir = Path(r'c:\wamp64\www\esg_strategies\labs')
    
    print("=== Corrections ultra-ciblées ===")
    
    # Fichiers spécifiques à corriger
    files_to_fix = [
        base_dir / 'pages' / 'Accueil.md',
        base_dir / 'articles' / 'Publications.md'
    ]
    
    for file_path in files_to_fix:
        if file_path.exists():
            print(f"Correction: {file_path.name}")
            if process_file(file_path):
                print(f"  ✅ Succès")
            else:
                print(f"  ❌ Erreur")
    
    print("\n🎯 Corrections ultra-ciblées terminées!")

if __name__ == "__main__":
    main()