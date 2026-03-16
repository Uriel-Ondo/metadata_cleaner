import pikepdf

def clean_pdf(path_in, path_out):
    # Ouvrir le PDF
    pdf = pikepdf.open(path_in)

    # Supprimer les métadonnées classiques (docinfo)
    for key in list(pdf.docinfo.keys()):
        del pdf.docinfo[key]

    # Supprimer les métadonnées XMP si présentes
    try:
        with pdf.open_metadata() as meta:
            meta.clear()  # efface tout le contenu XMP
    except Exception:
        # Si pas de métadonnées XMP, on ignore
        pass

    # Sauvegarder le PDF nettoyé
    pdf.save(path_out)
    pdf.close()
