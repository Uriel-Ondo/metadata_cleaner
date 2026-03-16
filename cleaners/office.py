import shutil

def clean_office(path_in, path_out):
    # Pour simplifier, copie brute. Améliorable avec LibreOffice headless.
    shutil.copy(path_in, path_out)
