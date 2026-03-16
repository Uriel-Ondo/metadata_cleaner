# Metadata Cleaner

Application Flask multi‑plateforme pour supprimer les métadonnées de fichiers (images, PDF, documents Office, audio/vidéo, texte).  
Elle fonctionne en local, avec une interface web simple, et peut être déployée via Docker/Docker Compose.  
Compatible PWA (installable sur desktop et mobile).

---

## 🚀 Fonctionnalités
- Nettoyage des métadonnées EXIF des images (JPEG, PNG, BMP, GIF, TIFF, WebP, HEIC/HEIF).
- Suppression des métadonnées PDF (docinfo + XMP).
- Nettoyage des documents Office (Word, Excel, PowerPoint) et OpenDocument (ODT, ODS, ODP).
- Suppression des tags audio/vidéo via ffmpeg (MP3, FLAC, WAV, AAC, OGG, M4A, WMA, Opus, MP4, MKV, AVI, MOV, WebM, MPG, MPEG, TS, FLV).
- Nettoyage des fichiers texte `.txt` (suppression du BOM et des espaces/lignes vides).
- Interface web moderne et responsive.
- Compatible PWA (manifest + service worker).

---

## 📂 Formats pris en charge

| Catégorie       | Formats pris en charge |
|-----------------|------------------------|
| **Images**      | `.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`, `.tiff`, `.webp`, `.heic`, `.heif` |
| **PDF**         | `.pdf` |
| **Documents**   | `.docx`, `.xlsx`, `.pptx`, `.odt`, `.ods`, `.odp` |
| **Texte**       | `.txt` |
| **Audio**       | `.mp3`, `.flac`, `.wav`, `.aac`, `.ogg`, `.m4a`, `.wma`, `.opus` |
| **Vidéo**       | `.mp4`, `.mkv`, `.avi`, `.mov`, `.webm`, `.mpg`, `.mpeg`, `.ts`, `.flv` |

---

## 📦 Installation locale (sans Docker)

1. Cloner le projet :
   ```bash
   git clone https://github.com/toncompte/metadata_cleaner.git
   cd metadata_cleaner
   ```

2. Créer un environnement virtuel et installer les dépendances :
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
   pip install -r requirements.txt
   ```

3. Installer **ffmpeg** sur votre système :
   - macOS : `brew install ffmpeg`
   - Linux : `sudo apt install ffmpeg`
   - Windows : télécharger depuis [ffmpeg.org](https://ffmpeg.org)

4. Lancer l’application :
   ```bash
   python app.py
   ```
   Puis ouvrir `http://127.0.0.1:8021` dans votre navigateur.

---

## 🐳 Exécution avec Docker

### 1. Construire l’image
```bash
docker build -t metadata-cleaner .
```

### 2. Lancer le conteneur
```bash
docker run -d -p 8021:8021 --name cleaner metadata-cleaner
```

L’application sera disponible sur `http://localhost:8021`.

---

## 🐙 Exécution avec Docker Compose

Le projet inclut un fichier `docker-compose.yml`.  
Pour démarrer directement :

```bash
docker compose up -d
```

### Arrêter le service
```bash
docker compose down
```

### Volumes persistants
Les dossiers `uploads/` et `cleaned/` sont montés en volumes pour conserver les fichiers entre les redémarrages.

---

## 📱 Utilisation en PWA
- L’application inclut un `manifest.json` et un `service worker (sw.js)`.  
- Depuis Chrome/Edge/Android, vous pouvez installer l’application via le bouton **“Installer”** dans la barre d’adresse.  
- Une fois installée, elle apparaît comme une application native (icône sur bureau ou écran d’accueil).  

---

## ⚠️ Notes
- `ffmpeg` est requis pour le nettoyage audio/vidéo.  
- Les fichiers texte `.txt` sont nettoyés en supprimant le BOM et les espaces/lignes vides.  
- Les formats non supportés renvoient un message d’erreur.  

---
