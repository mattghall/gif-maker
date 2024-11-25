import sys
import re
from PIL import Image, ImageDraw
import json

def convert_to_rgb(color):
    if color.startswith('#'):
        return tuple(int(color[i:i+2], 16) for i in (1, 3, 5))
    elif color.startswith('rgba'):
        color = color[5:-1]
        return tuple(map(int, color.split(',')[:3]))
    elif color.startswith('rgb'):
        color = color[4:-1]
        return tuple(map(int, color.split(',')))
    else:
        raise ValueError(f"Unknown color format: {color}")

def parse_input_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    speed = 10  # Default speed
    color_map = {}
    ascii_art = []
    parsing_colors = True

    for line in lines:
        line = line.strip()
        if not line:
            parsing_colors = False
            continue

        if parsing_colors:
            if line.startswith('speed:'):
                speed = int(line.split(':')[1].strip())
            else:
                match = re.match(r"(\w+),\s*'(\w)':\s*'(.+)'", line)
                if match:
                    name, char, color = match.groups()
                    color_map[char] = (name, color)
        else:
            ascii_art.append(line)

    return speed, color_map, ascii_art

def create_gif(color_map, ascii_art, output_path, box_size=20, fps=10, transparent_key=None):
    frames = []
    width = len(ascii_art[0]) * box_size
    height = len(ascii_art) * box_size

    transparent_color = color_map.get(transparent_key, (None, (255, 255, 255, 0)))[1] if transparent_key else (255, 255, 255, 0)

    img = Image.new('RGBA', (width, height), transparent_color)
    draw = ImageDraw.Draw(img)

    for y, row in enumerate(ascii_art):
        for x, char in enumerate(row):
            color_name, color = color_map.get(char, ('default', (255, 255, 255, 0)))
            if color == transparent_color:
                continue  # Skip drawing for transparent pixels
            print(f"Drawing {char} at ({x}, {y}) with color {color_name}")
            draw.rectangle(
                [x * box_size, y * box_size, (x + 1) * box_size, (y + 1) * box_size],
                fill=color
            )
            # Append a copy of the current image to frames
            frames.append(img.copy())

    # Draw 1px white boxes in the outer corners to ensure the full image is rendered
    draw.rectangle([0, 0, 1, 1], fill=(255, 255, 255, 255))
    draw.rectangle([width-1, 0, width, 1], fill=(255, 255, 255, 255))
    draw.rectangle([0, height-1, 1, height], fill=(255, 255, 255, 255))
    draw.rectangle([width-1, height-1, width, height], fill=(255, 255, 255, 255))
    frames.append(img.copy())

    # Save the frames as a GIF with transparency
    frames[0].save(output_path, save_all=True, append_images=frames[1:], duration=1000//fps, loop=0, transparency=0)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <input_file> <output_gif>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_gif = sys.argv[2]

    print(f"Input File: {input_file}")
    print(f"Output GIF: {output_gif}")

    speed, color_map, ascii_art = parse_input_file(input_file)
    print("Parsed Color Map:", color_map)
    create_gif(color_map, ascii_art, output_gif, fps=speed)