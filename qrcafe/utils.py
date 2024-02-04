from PIL import Image

from PIL import Image

def resize_image(image):
    # Desired dimensions
    desired_width = 3840
    desired_height = 2160
    
    # Open the image
    img = Image.open(image)

    # Resize the image
    img = img.resize((desired_width, desired_height))
    
    # Return the resized image
    return img