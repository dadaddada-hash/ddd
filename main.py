import os
import random
from PIL import Image
import pygame

def display_random_image(directory_path):
    # Initialize an empty list to hold all image file paths
    image_files = []

    # Walk through all subdirectories
    for root, dirs, files in os.walk(directory_path):
        # Add image files to the list if they have an appropriate extension
        for file in files:
            if file.endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                image_files.append(os.path.join(root, file))
    
    # Check if there are any images in the directory or subdirectories
    if not image_files:
        print("No images found in the directory or its subdirectories.")
        return

    # Select a random image from the list
    random_image_path = random.choice(image_files)
    
    # Open the image with PIL and convert it to a format that pygame can use
    img = Image.open(random_image_path)
    img = img.convert('RGB')  # Convert to RGB if necessary
    img_width, img_height = img.size
    image_data = pygame.image.fromstring(img.tobytes(), img.size, img.mode)

    # Initialize pygame and create a window with the image size
    pygame.init()
    window = pygame.display.set_mode((img_width, img_height))
    pygame.display.set_caption("cat database image creator")

    # Display the image in the pygame window
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Blit (copy) the image to the pygame window and update the display
        window.blit(image_data, (0, 0))
        pygame.display.flip()

    pygame.quit()

# Usage: specify the path to your main image directory
display_random_image('C:\\Users\\Huda Arain\\.cache\\kagglehub\\datasets\\crawford\\cat-dataset\\versions\\2')

