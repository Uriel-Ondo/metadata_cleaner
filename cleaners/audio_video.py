import subprocess

def clean_media(path_in, path_out):
    """
    Nettoie les métadonnées des fichiers audio et vidéo
    en utilisant ffmpeg. Tous les formats pris en charge
    par ffmpeg peuvent être traités.
    """
    cmd = [
        "ffmpeg",
        "-i", path_in,
        "-map_metadata", "-1",  # supprime toutes les métadonnées
        "-c", "copy",           # copie sans réencodage
        path_out
    ]
    subprocess.run(cmd, check=True)
