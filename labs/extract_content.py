#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour extraire le contenu des fichiers XML WordPress et créer des fichiers Markdown
organisés en dossiers pour les pages et articles.
"""

import xml.etree.ElementTree as ET
import os
import re
import html
from pathlib import Path

def clean_filename(filename):
    """Nettoie le nom de fichier pour qu'il soit valide sur le système de fichiers"""
    # Remplace les caractères spéciaux par des tirets
    filename = re.sub(r'[<>:"/\\|?*]', '-', filename)
    # Remplace les espaces par des tirets
    filename = re.sub(r'\s+', '-', filename)
    # Supprime les tirets multiples
    filename = re.sub(r'-+', '-', filename)
    # Supprime les tirets en début et fin
    filename = filename.strip('-')
    return filename

def html_to_markdown(html_content):
    """Convertit le contenu HTML en Markdown basique"""
    if not html_content:
        return ""
    
    # Décode les entités HTML
    content = html.unescape(html_content)
    
    # Convertit les balises HTML en Markdown
    # Titres
    content = re.sub(r'<h1[^>]*>(.*?)</h1>', r'# \1', content, flags=re.DOTALL)
    content = re.sub(r'<h2[^>]*>(.*?)</h2>', r'## \1', content, flags=re.DOTALL)
    content = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1', content, flags=re.DOTALL)
    content = re.sub(r'<h4[^>]*>(.*?)</h4>', r'#### \1', content, flags=re.DOTALL)
    content = re.sub(r'<h5[^>]*>(.*?)</h5>', r'##### \1', content, flags=re.DOTALL)
    content = re.sub(r'<h6[^>]*>(.*?)</h6>', r'###### \1', content, flags=re.DOTALL)
    
    # Paragraphes
    content = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', content, flags=re.DOTALL)
    
    # Liens
    content = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', content, flags=re.DOTALL)
    
    # Gras et italique
    content = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', content, flags=re.DOTALL)
    content = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', content, flags=re.DOTALL)
    content = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', content, flags=re.DOTALL)
    content = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', content, flags=re.DOTALL)
    
    # Listes
    content = re.sub(r'<ul[^>]*>', '', content)
    content = re.sub(r'</ul>', '\n', content)
    content = re.sub(r'<ol[^>]*>', '', content)
    content = re.sub(r'</ol>', '\n', content)
    content = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1', content, flags=re.DOTALL)
    
    # Supprime les autres balises HTML
    content = re.sub(r'<[^>]+>', '', content)
    
    # Nettoie les espaces multiples et les sauts de ligne
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
    content = re.sub(r'^\s+|\s+$', '', content, flags=re.MULTILINE)
    
    return content.strip()

def extract_item_data(item):
    """Extrait les données d'un item XML"""
    data = {}
    
    # Titre
    title_elem = item.find('title')
    data['title'] = title_elem.text if title_elem is not None else "Sans titre"
    
    # Contenu
    content_elem = item.find('{http://purl.org/rss/1.0/modules/content/}encoded')
    data['content'] = content_elem.text if content_elem is not None else ""
    
    # Extrait
    excerpt_elem = item.find('{http://wordpress.org/export/1.2/excerpt/}encoded')
    data['excerpt'] = excerpt_elem.text if excerpt_elem is not None else ""
    
    # Type de post
    post_type_elem = item.find('{http://wordpress.org/export/1.2/}post_type')
    data['post_type'] = post_type_elem.text if post_type_elem is not None else "post"
    
    # Statut
    status_elem = item.find('{http://wordpress.org/export/1.2/}status')
    data['status'] = status_elem.text if status_elem is not None else "draft"
    
    # Ordre du menu
    menu_order_elem = item.find('{http://wordpress.org/export/1.2/}menu_order')
    data['menu_order'] = int(menu_order_elem.text) if menu_order_elem is not None and menu_order_elem.text.isdigit() else 0
    
    # Date de publication
    pub_date_elem = item.find('pubDate')
    data['pub_date'] = pub_date_elem.text if pub_date_elem is not None else ""
    
    # Lien
    link_elem = item.find('link')
    data['link'] = link_elem.text if link_elem is not None else ""
    
    # Nom du post (slug)
    post_name_elem = item.find('{http://wordpress.org/export/1.2/}post_name')
    data['post_name'] = post_name_elem.text if post_name_elem is not None else ""
    
    # Catégories
    categories = []
    for category in item.findall('category'):
        if category.text:
            categories.append(category.text)
    data['categories'] = categories
    
    return data

def create_markdown_file(data, output_path):
    """Crée un fichier Markdown à partir des données extraites"""
    content = f"""# {data['title']}

"""
    
    # Ajoute les métadonnées
    if data['pub_date']:
        content += f"**Date de publication:** {data['pub_date']}\n\n"
    
    if data['categories']:
        content += f"**Catégories:** {', '.join(data['categories'])}\n\n"
    
    if data['link']:
        content += f"**Lien original:** {data['link']}\n\n"
    
    content += "---\n\n"
    
    # Ajoute l'extrait s'il existe
    if data['excerpt']:
        content += f"## Résumé\n\n{html_to_markdown(data['excerpt'])}\n\n"
    
    # Ajoute le contenu principal
    if data['content']:
        content += f"## Contenu\n\n{html_to_markdown(data['content'])}\n"
    
    # Écrit le fichier
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

def process_xml_file(xml_file_path, pages_dir, articles_dir):
    """Traite un fichier XML et extrait les pages et articles"""
    print(f"Traitement du fichier: {xml_file_path}")
    
    try:
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        
        pages = []
        articles = []
        
        # Trouve tous les items
        for item in root.findall('.//item'):
            data = extract_item_data(item)
            
            # Ignore les éléments sans titre ou avec un statut non publié
            if not data['title'] or data['status'] != 'publish':
                continue
            
            # Ignore les éléments système ou de navigation
            if any(keyword in data['title'].lower() for keyword in ['footer', 'header', 'menu', 'widget', 'sidebar']):
                continue
            
            # Ignore les images et fichiers média
            if any(keyword in data['title'].lower() for keyword in ['img', 'image', 'logo', 'icon', '.jpg', '.png', '.gif']):
                continue
            
            if data['post_type'] == 'page':
                pages.append(data)
            elif data['post_type'] == 'post':
                articles.append(data)
        
        # Traite les pages
        for page_data in pages:
            filename = clean_filename(page_data['title']) + '.md'
            page_path = pages_dir / filename
            create_markdown_file(page_data, page_path)
            print(f"  Page créée: {filename}")
        
        # Traite les articles
        for article_data in articles:
            filename = clean_filename(article_data['title']) + '.md'
            article_path = articles_dir / filename
            create_markdown_file(article_data, article_path)
            print(f"  Article créé: {filename}")
        
        return pages, articles
        
    except ET.ParseError as e:
        print(f"Erreur lors du parsing du fichier {xml_file_path}: {e}")
        return [], []
    except Exception as e:
        print(f"Erreur lors du traitement du fichier {xml_file_path}: {e}")
        return [], []

def create_menu_file(all_pages, output_path):
    """Crée le fichier menu.md avec la structure du site"""
    # Trie les pages par ordre de menu
    sorted_pages = sorted(all_pages, key=lambda x: (x['menu_order'], x['title']))
    
    content = """# Menu du Site ESG Stratégies

## Structure de Navigation

### Pages Principales

"""
    
    for page in sorted_pages:
        if page['menu_order'] > 0:  # Pages avec un ordre de menu défini
            content += f"- [{page['title']}](pages/{clean_filename(page['title'])}.md) (Ordre: {page['menu_order']})\n"
    
    content += "\n### Autres Pages\n\n"
    
    for page in sorted_pages:
        if page['menu_order'] == 0:  # Pages sans ordre de menu spécifique
            content += f"- [{page['title']}](pages/{clean_filename(page['title'])}.md)\n"
    
    content += """

## Structure des Dossiers

- `pages/` - Contient toutes les pages du site
- `articles/` - Contient tous les articles/posts du blog

## Catégories d'Articles

Les articles sont organisés par catégories :
- Conseils
- Environnement
- Formations
- Gouvernance
- Publications
- Société

"""
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    """Fonction principale"""
    # Répertoire de base
    base_dir = Path(r'c:\wamp64\www\esg_strategies\labs')
    
    # Crée les dossiers de sortie
    pages_dir = base_dir / 'pages'
    articles_dir = base_dir / 'articles'
    
    pages_dir.mkdir(exist_ok=True)
    articles_dir.mkdir(exist_ok=True)
    
    # Liste des fichiers XML à traiter
    xml_files = [
        'esgstratgies.WordPress.2025-07-24.xml',
        'esgstratgies.WordPress.2025-07-24 (1).xml',
        'esgstratgies.WordPress.2025-07-24 (2).xml'
    ]
    
    all_pages = []
    all_articles = []
    
    # Traite chaque fichier XML
    for xml_file in xml_files:
        xml_path = base_dir / xml_file
        if xml_path.exists():
            pages, articles = process_xml_file(xml_path, pages_dir, articles_dir)
            all_pages.extend(pages)
            all_articles.extend(articles)
        else:
            print(f"Fichier non trouvé: {xml_path}")
    
    # Supprime les doublons basés sur le titre
    unique_pages = []
    seen_titles = set()
    for page in all_pages:
        if page['title'] not in seen_titles:
            unique_pages.append(page)
            seen_titles.add(page['title'])
    
    unique_articles = []
    seen_titles = set()
    for article in all_articles:
        if article['title'] not in seen_titles:
            unique_articles.append(article)
            seen_titles.add(article['title'])
    
    # Crée le fichier menu
    menu_path = base_dir / 'menu.md'
    create_menu_file(unique_pages, menu_path)
    
    print(f"\n=== Résumé ===")
    print(f"Pages créées: {len(unique_pages)}")
    print(f"Articles créés: {len(unique_articles)}")
    print(f"Menu créé: menu.md")
    print(f"Dossier pages: {pages_dir}")
    print(f"Dossier articles: {articles_dir}")

if __name__ == "__main__":
    main()