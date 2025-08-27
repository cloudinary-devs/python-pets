
# Cloudinary + Flask Gallery

A minimal Flask app that displays a gallery of images stored in **Cloudinary**.  
Server fetches image metadata via Cloudinary **Search API** and renders transformed thumbnails.

## Features
- Server‑side: Flask + Cloudinary SDK (credentials via `CLOUDINARY_URL` env var)
- Responsive thumbnails: 300×300 `c_fill,g_auto,f_auto,q_auto`
- Full-size images: 800×600 `c_fill,g_auto,f_auto,q_auto`
- Configurable by **folder** only

## Quick Start

1. **Clone/Unzip** this project.
2. Create `.env` file and set:
   ```env
   CLOUDINARY_URL=cloudinary://<api_key>:<api_secret>@<cloud_name>
   GALLERY_FOLDER=pets
   MAX_RESULTS=20
   PORT=5000
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run:
   ```bash
   python app.py
   ```
5. Open http://localhost:5000

> Tip: Upload a few images into the `pets/` folder so they appear in the gallery.

## Environment Variables
- `CLOUDINARY_URL` (required): Your Cloudinary connection string
- `GALLERY_FOLDER` (optional): Folder to search for images (default: "pets")
- `MAX_RESULTS` (optional): Maximum number of images to display (default: 20)
- `PORT` (optional): Port to run on (default: 5000)

## Notes
- This app uses server‑side credentials; keep `.env` out of version control.
- If you get no results, double‑check the folder name and ensure your Cloudinary account has images in that folder.
