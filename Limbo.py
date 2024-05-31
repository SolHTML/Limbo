import tkinter as tk
from PIL import Image, ImageTk
import random
import pygame
import math
import time

# Initialize pygame
pygame.init()

# Function to create a window with a resized image
def create_window(image, position):
    window = tk.Toplevel()
    window.title("Key")
    window.configure(bg="black")

    img = ImageTk.PhotoImage(image)

    # Create a label to hold the image
    label = tk.Label(window, image=img, bg="black")
    label.image = img  # Keep a reference to avoid garbage collection
    label.pack(expand=True)

    # Set window position
    window.geometry(f"{window_width}x{window_height}+{position[0]}+{position[1]}")
    return label

# Function to switch the green key back to red
def switch_to_red(green_label, num_windows):
    global red_img
    red_img_tk = ImageTk.PhotoImage(red_img)  # Convert red_img to a PhotoImage object
    green_label.config(image=red_img_tk)
    green_label.image = red_img_tk  # Keep a reference to avoid garbage collection
    time.sleep(0.25)
    root.after(0, create_red_windows, num_windows)  # Start creating red key windows

# Function to create multiple red key windows
def create_red_windows(num_windows):
    global screen_width, screen_height, window_width, window_height, red_img

    for _ in range(num_windows):
        rx = random.randint(0, screen_width - window_width)
        ry = random.randint(0, screen_height - window_height)
        create_window(red_img, (rx, ry))

    if num_windows >= 500:
        print('stop the madness')
    else:
        # Double the number of red windows for the next call
        root.after(500, create_red_windows, num_windows * 2)

def errorCrash():
    pass
    time.sleep(32)
    KeyboardInterrupt


# Main function to create a green key window and then switch to red key windows
def main(image_path, green_image_path):
    global root, screen_width, screen_height, window_width, window_height, red_img

    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Initialize pygame mixer for audio
    pygame.mixer.init()

    # Load the audio file
    pygame.mixer.music.load("limbo.mp3")

    # Play the audio
    pygame.mixer.music.play()

    # Screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Window dimensions
    window_width = 200
    window_height = 200

    try:
        # Load the images
        red_img = Image.open(image_path).resize((window_width, window_height), Image.LANCZOS)
        green_img = Image.open(green_image_path).resize((window_width, window_height), Image.LANCZOS)
    except Exception as e:
        print("Error loading images:", e)
        root.destroy()  # Close the Tkinter window
        return

    # Calculate the position for the center window (convert to integer)
    x = int((screen_width - window_width) / 2)
    y = int((screen_height - window_height) / 2)

    # Create the green key window in the middle of the screen
    green_label = create_window(green_img, (x, y))


    # Schedule the switch to red after 9 seconds
    root.after(8750, switch_to_red, green_label, num_windows)


    # Schedule the introduction of a syntax error after 32 seconds
    root.after(32000, lambda: exec("raise SyntaxError('Intentional Syntax Error')"))

    root.mainloop()

if __name__ == "__main__":
    # Paths to your PNG images
    image_path = "red_key.png"
    green_image_path = "green_key.png"

    # Number of red key windows to spawn initially
    num_windows = 10

    # Run the main function
    main(image_path, green_image_path)
