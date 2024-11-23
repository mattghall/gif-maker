from PIL import Image, ImageDraw
import imageio
import random
import os

# Constants for the grid
GRID_SIZE = 4
BOX_SIZE = 100  # Size of each box
SPACING = 5     # Space between boxes
GRID_COLOR = (239, 239, 230)
FILL_COLORS = ['#f9df6d', '#a0c35a','#b0c4ef','#ba81c5']  # Example colors

def create_frame(filled_boxes):
    """Create a single frame of the grid with the given filled boxes."""
    img_size = GRID_SIZE * BOX_SIZE + (GRID_SIZE + 1) * SPACING
    img = Image.new("RGBA", (img_size, img_size), (255, 255, 255, 0))  # Transparent background
    draw = ImageDraw.Draw(img)

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x0 = col * BOX_SIZE + (col + 1) * SPACING
            y0 = row * BOX_SIZE + (row + 1) * SPACING
            x1 = x0 + BOX_SIZE
            y1 = y0 + BOX_SIZE

            # Decide the color of the box
            box_index = row * GRID_SIZE + col
            if box_index < len(filled_boxes):
                color = filled_boxes[box_index]
            else:
                color = GRID_COLOR

            draw.rounded_rectangle([x0, y0, x1, y1], radius=6, fill=color)

    return img

def generate_gif(output_filename, duration=100):
    """Generate the GIF by filling in boxes one by one, flashing random boxes, and then erasing them."""
    frames = []
    filled_boxes = []

    # Cycle through each row and fill it with one color
    for row in range(GRID_SIZE):
        color = FILL_COLORS[row % len(FILL_COLORS)]  # Cycle through colors per row
        for col in range(GRID_SIZE):
            filled_boxes.append(color)
            frame = create_frame(filled_boxes)
            frames.append(frame)

    # Flash random boxes on and off
    for _ in range(5):  # Number of flashes
        flash_boxes = filled_boxes.copy()
        for _ in range(GRID_SIZE):  # Number of boxes to flash
            index = random.randint(0, GRID_SIZE * GRID_SIZE - 1)
            flash_boxes[index] = GRID_COLOR if flash_boxes[index] != GRID_COLOR else FILL_COLORS[index // GRID_SIZE]
        frame = create_frame(flash_boxes)
        frames.append(frame)

    # Randomly erase multiple boxes at a time until they are all gone
    erase_boxes = filled_boxes.copy()
    indices = list(range(len(erase_boxes)))
    random.shuffle(indices)
    while indices:
        # Determine the number of boxes to erase in this step
        num_to_erase = min(3, len(indices))  # Erase 3 or all remaining boxes
        for _ in range(num_to_erase):
            index = indices.pop()
            erase_boxes[index] = GRID_COLOR
        frame = create_frame(erase_boxes)
        frames.append(frame)

    # Save as GIF
    frames[0].save(
        output_filename,
        save_all=True,
        append_images=frames[1:],
        duration=duration,
        loop=0,
    )

def main():
    # Create the output directory if it doesn't exist
    output_dir = os.path.join("output", os.path.splitext(os.path.basename(__file__))[0])
    os.makedirs(output_dir, exist_ok=True)

    # Define the output file path
    output_file = os.path.join(output_dir, os.path.basename(output_dir) + ".gif")
    duration = 150  # Set the duration for the GIF
    generate_gif(output_file, duration)
    print(f"GIF created: {output_file}")

if __name__ == "__main__":
    main()
