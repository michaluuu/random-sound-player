import os
import random
import pygame


# Set the working directory to the script's location
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
def get_random_sound():
    sounds = [file for file in os.listdir() if file.endswith(('.wav', '.mp3'))]  # Assuming you have wav files in the same folder
    return random.choice(sounds)

def main():
    pygame.mixer.init()

    while True:
        random_sound = get_random_sound()
        print(f"Playing: {random_sound}")
        pygame.mixer.music.load(random_sound)
        pygame.mixer.music.play()

        # Add a delay before stopping the current sound and playing the next one
        pygame.time.delay(random.randint(5000, 15000))  # Adjust the range as desired

if __name__ == "__main__":
    main()
