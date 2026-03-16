def clean_text(path_in, path_out):
    """
    Nettoie un fichier texte :
    - supprime les éventuels BOM (Byte Order Mark)
    - supprime les espaces ou lignes vides en début/fin
    """
    with open(path_in, "r", encoding="utf-8-sig") as f:
        content = f.read()

    # Nettoyage simple
    cleaned = content.strip()

    with open(path_out, "w", encoding="utf-8") as f:
        f.write(cleaned)
