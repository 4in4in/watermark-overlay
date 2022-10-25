
import os

from src.postprocessor import ImagePostprocessor

SAMPLES_DIR = "input"
OUTPUT_DIR = "output"

ESCAPE_FILES = [".gitkeep"]

proc = ImagePostprocessor()


if __name__ == "__main__":
    samples = os.listdir(SAMPLES_DIR)
    for sample in (s for s in samples if s not in ESCAPE_FILES):
        processed_image = None
        with open(f"./{SAMPLES_DIR}/{sample}", "rb") as file:
            processed_image = proc.add_watermark(file.read(), False)

        with open(f"./{OUTPUT_DIR}/{sample}", "wb") as file:
            file.write(processed_image)
