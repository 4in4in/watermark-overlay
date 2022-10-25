
import os

from src.postprocessor import ImagePostprocessor

SAMPLES_DIR = "input"
OUTPUT_DIR = "output"

ESCAPE_FILES = [".gitkeep"]

proc = ImagePostprocessor()


if __name__ == "__main__":
    images = os.listdir(SAMPLES_DIR)
    for image_fname in images:
        if image_fname in ESCAPE_FILES: continue

        processed_image = None
        with open(f"./{SAMPLES_DIR}/{image_fname}", "rb") as file:
            processed_image = proc.add_watermark(file.read(), False)

        with open(f"./{OUTPUT_DIR}/{image_fname}", "wb") as file:
            file.write(processed_image)
