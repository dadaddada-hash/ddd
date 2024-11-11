# Random Image Display Tool

A Python project that selects a random image from a specified directory (including subdirectories) and displays it in a `pygame` window. This tool is ideal if you have a folder of images and want to display a randomly selected one.

## Requirements

Ensure the following Python libraries are installed before running the project:

- **pygame**: For displaying the image in a window.
- **Pillow (PIL)**: For opening and processing image files.
- **random**: This is included with Python by default, so no additional installation is necessary.

Install the required libraries using the following command:

```bash
pip install pygame pillow

code example =
Project Structure
main.py: The main file of the project containing functions to select a random image and display it in a pygame window.
Functionality
The script searches a specified directory and all its subdirectories for image files with extensions .png, .jpg, .jpeg, .gif, and .bmp. It randomly selects one of these image files and displays it in a pygame window.

Configuration
Image Directory Path: Open the main.py file and locate the last line in the script:

python
Code kopieren
display_random_image("path/to/your/image_directory")
Replace "path/to/your/image_directory" with the actual path to the folder containing your images. Only replace the text within the quotation marks.

Example:

python
Code kopieren
display_random_image("C:/Users/MyUsername/Pictures")
Ensure the path is entered correctly. You can use either an absolute path or a relative path if the image folder is within your project directory.

Usage
Confirm that all dependencies are installed, including pygame and Pillow.

Open a terminal or command prompt and navigate to your project directory, where main.py is located.

Run the script with the following command:

bash
Code kopieren
python main.py
The script will open a pygame window displaying a randomly selected image from the specified directory or any of its subdirectories. Each time you run the script, a new random image will be displayed.

Example Code for main.py
python
Code kopieren
import os
import random
from PIL import Image
import pygame

def display_random_image(directory_path):
    image_files = []

    # Walk through all subdirectories and gather image files
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                image_files.append(os.path.join(root, file))
    
    # Check if images were found
    if not image_files:
        print("No images found in the directory or its subdirectories.")
        return

    # Select a random image
    random_image_path = random.choice(image_files)
    
    # Open the image with PIL and prepare it for pygame
    img = Image.open(random_image_path)
    img = img.convert('RGB')
    img_width, img_height = img.size
    image_data = pygame.image.fromstring(img.tobytes(), img.size, img.mode)

    # Initialize the pygame window
    pygame.init()
    window = pygame.display.set_mode((img_width, img_height))
    pygame.display.set_caption("Random Image Display Tool")

    # Display the image in the pygame window
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw and show the image in the window
        window.blit(image_data, (0, 0))
        pygame.display.flip()

    pygame.quit()

# Specify the path to your image directory here
display_random_image("path/to/your/image_directory")
Notes
Image Size: Ensure that images are not too large for your screen, as the window size will automatically adjust to the image size.
Image Formats: If you are using images with uncommon formats, make sure Pillow supports them.
License
This project is licensed under the MIT License. You can view more details about the license here.  so you cant use it for everything



