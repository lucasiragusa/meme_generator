from PIL import Image, ImageDraw, ImageFont
import os
import sys
sys.path.append('.')

class MemeEngine:
    """
    A class for generating memes with text captions.

    Attributes:
    - output_dir (str): the directory where generated memes are saved
    """

    def __init__(self, output_dir):
        """
        Initializes a new MemeGenerator object.

        Args:
        - output_dir (str): the directory where generated memes are saved
        """
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """
        Generates a new meme image with a text caption.

        Args:
        - img_path (str): the file path of the input image
        - text (str): the text to include in the meme caption
        - author (str): the author of the meme caption
        - width (int): the maximum width of the output image in pixels (default: 500)

        Returns:
        - output_path (str): the file path of the generated meme image
        """
        try:
            image = Image.open(img_path)
        except Exception as e:
            raise Exception(f"Error loading image {img_path}: {e}")

        # Resize the image while maintaining the aspect ratio
        w, h = image.size
        ratio = width / float(w)
        height = int(ratio * h)
        image = image.resize((width, height), Image.NEAREST)

        # Add text to the image
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20, encoding="unic")

        author = author.upper()
        text_width, text_height = draw.textsize(text, font)
        author_font =  ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=10, encoding="unic")
        author_width, author_height = draw.textsize(author, author_font)
        x = 20
        y = height - text_height - author_height - 30
        draw.text((x, y), text, font=font, fill='white')
        draw.text((x, y + text_height + 10), '- ' + author, font=author_font, fill='white')

        # Save the new image to disk
        output_path = os.path.join(self.output_dir, os.path.basename(img_path))
        image.save(output_path)

        return output_path