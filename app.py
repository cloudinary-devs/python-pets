
import os
from flask import Flask, render_template
from dotenv import load_dotenv
import cloudinary
from cloudinary import CloudinaryImage


load_dotenv()

cloudinary.config(cloudinary_url=os.getenv("CLOUDINARY_URL"), secure=True)

GALLERY_FOLDER = os.getenv("GALLERY_FOLDER", "pets")
MAX_RESULTS = int(os.getenv("MAX_RESULTS", "20"))

app = Flask(__name__)

def _thumb_url(public_id):
    return CloudinaryImage(public_id).build_url(
        transformation=[
            {"crop": "fill", "width": 300, "height": 300},
            {"fetch_format": "auto", "quality": "auto"}
        ]
    )

def _full_url(public_id):
    return CloudinaryImage(public_id).build_url(
        transformation=[
            {"crop": "fill", "width": 800, "height": 600},
            {"fetch_format": "auto", "quality": "auto"}
        ]
    )

@app.route("/")
def index():
    result = (
        cloudinary.Search()
        .expression(f"folder={GALLERY_FOLDER}")
        .sort_by("created_at", "desc")
        .max_results(MAX_RESULTS)
        .with_field("tags")
        .execute()
    )
    
    resources = result.get("resources", [])
    
    items = []
    for r in resources:
        pid = r.get("public_id")
        if pid:
            items.append({
                "public_id": pid,
                "thumb": _thumb_url(pid),
                "full": _full_url(pid),
                "tags": r.get("tags", [])
            })
    
    return render_template("index.html", items=items, folder=GALLERY_FOLDER)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=True)
