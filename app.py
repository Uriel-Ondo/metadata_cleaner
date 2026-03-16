from flask import Flask, render_template, request, send_from_directory
import os
from cleaners.images import clean_image
from cleaners.pdfs import clean_pdf
from cleaners.office import clean_office
from cleaners.audio_video import clean_media
from cleaners.texts import clean_text

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
CLEANED_FOLDER = "cleaned"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CLEANED_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Vérification de la présence du champ "file"
        if "file" not in request.files:
            return "Aucun fichier reçu. Veuillez sélectionner un fichier."

        file = request.files["file"]

        # Vérification du nom de fichier
        if file.filename == "":
            return "Fichier vide. Veuillez sélectionner un fichier valide."

        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        cleaned_path = os.path.join(CLEANED_FOLDER, file.filename)

        filename = file.filename.lower()

        # PDF
        if filename.endswith(".pdf"):
            clean_pdf(filepath, cleaned_path)

        # Images (formats courants + iPhone HEIC/HEIF)
        elif filename.endswith((
            ".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".webp",
            ".heic", ".heif"
        )):
            clean_image(filepath, cleaned_path)

        # Documents Office et OpenDocument
        elif filename.endswith((
            ".docx", ".xlsx", ".pptx", ".odt", ".ods", ".odp"
        )):
            clean_office(filepath, cleaned_path)

        # Fichiers texte
        elif filename.endswith(".txt"):
            clean_text(filepath, cleaned_path)

        # Audio et vidéo (formats pris en charge par ffmpeg + MOV iPhone)
        elif filename.endswith((
            ".mp3", ".flac", ".wav", ".aac", ".ogg", ".m4a", ".wma", ".opus",
            ".mp4", ".mkv", ".avi", ".mov", ".webm", ".mpg", ".mpeg", ".ts", ".flv"
        )):
            clean_media(filepath, cleaned_path)

        else:
            return "Format non supporté pour l'instant."

        return render_template("result.html", filename=file.filename)

    return render_template("index.html")

@app.route("/download/<filename>")
def download(filename):
    return send_from_directory(CLEANED_FOLDER, filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8021, debug=True)
