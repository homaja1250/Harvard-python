

from PIL import Image, ImageOps
import sys

def shirt():
    if len(sys.argv) != 3:
        sys.exit("Invalid number of command-line arguments")

    input_name = sys.argv[1]
    output_name = sys.argv[2]

    if not (input_name.lower().endswith(".jpg") or input_name.lower().endswith(".jpeg") or input_name.lower().endswith(".png")):
        sys.exit("Invalid input file type")
    if not (output_name.lower().endswith(".jpg") or output_name.lower().endswith(".jpeg") or output_name.lower().endswith(".png")):
        sys.exit("Invalid output file type")
    if input_name.split(".")[-1].lower() != output_name.split(".")[-1].lower():
        sys.exit("Input and output files must have the same extension")

    try:
        input_image = Image.open(input_name)
    except FileNotFoundError:
        sys.exit("Input file not found")

    shirt_image = Image.open("shirt.png")
    input_image = ImageOps.fit(input_image, shirt_image.size)
    output_image = input_image.copy()
    output_image.paste(shirt_image, (0, 0), shirt_image)

    output_image.save(output_name)

shirt()

