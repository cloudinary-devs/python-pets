# ==============================
import os
from dotenv import load_dotenv

# Load environment variables from .env file FIRST
load_dotenv()

# Now import Cloudinary after environment variables are loaded
import cloudinary
from cloudinary import CloudinaryImage
import cloudinary.uploader
import cloudinary.api

# Import to format the JSON responses
# ==============================
import json

# Set configuration parameter: return "https" URLs by setting secure=True  
# ==============================
# The Cloudinary SDK automatically reads from CLOUDINARY_URL environment variable
config = cloudinary.config(secure=True)

# Log the configuration
# ==============================
print("****1. Set up and configure the SDK:****\nCredentials: ", config.cloud_name, config.api_key, "\n")

def configure_cloudinary():
    """Configure Cloudinary from environment variables"""
    # Configuration is now handled at module level
    print("Cloudinary configured successfully")
    return True

def update_asset_tags(public_id, tags):
    """
    Update tags on an existing Cloudinary asset
    
    Args:
        public_id (str): The public ID of the asset to update
        tags (list): List of tags to assign to the asset
    
    Returns:
        dict: Response from Cloudinary API
    """
    try:
        result = cloudinary.api.update(public_id, tags=tags)
        print(f"Successfully updated tags for {public_id}")
        print(f"New tags: {result.get('tags', [])}")
        return result
    except cloudinary.api.Error as e:
        print(f"Error updating tags: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def main():
    """Test function for the Cloudinary manager"""
    if not configure_cloudinary():
        return
    
    # Example usage
    public_id = "public_id"  # Replace with actual public ID
    new_tags = ["name:pet_name", "age:pet_age", "breed:pet_breed"]
    
    # Update the asset tags
    result = update_asset_tags(public_id, new_tags)
    
    if result:
        print("Asset updated successfully!")
        print(f"Asset details: {result}")
    else:
        print("Failed to update asset tags")

if __name__ == "__main__":
    main()