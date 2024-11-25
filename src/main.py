import sys
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

    color_map = {}
    ascii_art = []
    parsing_colors = True

    for line in lines:
        line = line.strip()
        if parsing_colors:
            if line == '':
                parsing_colors = False
                continue
            parts = line.split(':')
            namePart = parts[0].split(',')
            name = namePart[0].strip()
            key = namePart[1].strip().strip("'")
            color = convert_to_rgb(parts[1].strip().strip("'"))
            color_map[key] = (name, color)
            print(f"Adding color {name} with key {key} and color {color}")
        else:
            ascii_art.append(line)

    print("Color Map:", color_map)
    print("ASCII Art:", ascii_art)
    return color_map, ascii_art

def create_gif(color_map, ascii_art, output_path, box_size=20, fps=10, transparent_key=None):
    frames = []
    width = len(ascii_art[0]) * box_size
    height = len(ascii_art) * box_size

    transparent_color = color_map.get(transparent_key, (None, (255, 255, 255)))[1] if transparent_key else None

    for frame in range(1):  # Only iterate through one frame for now
        img = Image.new('RGB', (width, height), (255, 255, 255))
        draw = ImageDraw.Draw(img)

        for y, row in enumerate(ascii_art):
            for x, char in enumerate(row):
                color_name, color = color_map.get(char, ('default', (255, 255, 255)))
                if color == transparent_color:
                    continue  # Skip drawing for transparent pixels
                print(f"Drawing {char} at ({x}, {y}) with color {color_name}")
                draw.rectangle(
                    [x * box_size, y * box_size, (x + 1) * box_size, (y + 1) * box_size],
                    fill=color
                )

        # Convert to palette-based image for GIF
        frame = img.convert('P', palette=Image.ADAPTIVE)
        # Set the transparency color index
        if transparent_color:
            palette = frame.getpalette()
            transparent_index = palette.index(transparent_color[0]) // 3
            frame.info['transparency'] = transparent_index

        frames.append(frame)

    # Save the GIF with transparency
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=1000 // fps,
        loop=0,
        transparency=frames[0].info.get('transparency', 0),
    )


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <input_file> <output_gif>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_gif = sys.argv[2]

    print(f"Input File: {input_file}")
    print(f"Output GIF: {output_gif}")

    color_map, ascii_art = parse_input_file(input_file)
    create_gif(color_map, ascii_art, output_gif)