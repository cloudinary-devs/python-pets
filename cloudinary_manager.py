import os
from dotenv import load_dotenv
import cloudinary
import cloudinary.api
from urllib.parse import urlparse

# Load environment variables from .env file
load_dotenv()

def parse_cloudinary_url(cloudinary_url):
    """
    Parse Cloudinary URL to extract credentials
    
    Expected format: cloudinary://api_key:api_secret@cloud_name
    
    Args:
        cloudinary_url (str): Cloudinary URL from .env
    
    Returns:
        tuple: (cloud_name, api_key, api_secret)
    """
    try:
        # Parse the URL
        parsed = urlparse(cloudinary_url)
        
        # Extract credentials from netloc (username:password@hostname)
        credentials, cloud_name = parsed.netloc.split('@')
        api_key, api_secret = credentials.split(':')
        
        return cloud_name, api_key, api_secret
    except Exception as e:
        print(f"Error parsing Cloudinary URL: {e}")
        print("Expected format: cloudinary://api_key:api_secret@cloud_name")
        return None, None, None

def configure_cloudinary():
    """Configure Cloudinary from environment variables"""
    cloudinary_url = os.getenv('CLOUDINARY_URL')
    
    if cloudinary_url:
        # Parse the URL to extract credentials
        cloud_name, api_key, api_secret = parse_cloudinary_url(cloudinary_url)
        
        if all([cloud_name, api_key, api_secret]):
            # Configure Cloudinary
            cloudinary.config(
                cloud_name=cloud_name,
                api_key=api_key,
                api_secret=api_secret
            )
            print("Cloudinary configured successfully")
            return True
        else:
            print("Failed to parse Cloudinary credentials")
            return False
    else:
        print("CLOUDINARY_URL not found in environment variables")
        return False

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
    new_tags = ["name:your_pets_name", "age:pets_age", "breed:pet_breed"]
    
    # Update the asset tags
    result = update_asset_tags(public_id, new_tags)
    
    if result:
        print("Asset updated successfully!")
        print(f"Asset details: {result}")
    else:
        print("Failed to update asset tags")

if __name__ == "__main__":
    main()