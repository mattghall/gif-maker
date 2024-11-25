# GIF Maker

This project generates GIFs based on different input configurations. There are two main scripts in this project: `connections.py` and `main.py`.

## Features

- Convert a series of images to a GIF
- Convert a video file to a GIF
- Customize frame rate and resolution

## Installation

To use this project, clone the repository and install the required dependencies:

```bash
git clone git@github.com:mattghall/gif-maker.git
cd gif-maker
pip install -r requirements.txt
```

## Usage

### Convert Images to GIF

To convert a series of images to a GIF, use the following command:

```bash
python gif_maker.py --images path/to/images --output output.gif --fps 10
```

### Convert Video to GIF

To convert a video file to a GIF, use the following command:

```bash
python gif_maker.py --video path/to/video.mp4 --output output.gif --fps 10
```

### Options

- `--images`: Path to the directory containing images
- `--video`: Path to the video file
- `--output`: Path to save the output GIF
- `--fps`: Frames per second for the GIF

## `connections.py`

The `connections.py` script generates a GIF by filling in boxes one by one, flashing random boxes, and then erasing them. It uses a grid of boxes with predefined colors.

### How to Run

1. Ensure you have the required dependencies installed:
    ```sh
    pip install -r requirements.txt
    ```

2. Run the script:
    ```sh
    python src/connections.py
    ```

3. The generated GIF will be saved in the `output/connections/` directory.

### Example Output
![Example GIF](example/connections.gif)

### Main Functions

- `create_frame(filled_boxes)`: Creates a single frame of the grid with the given filled boxes.
- `generate_gif(output_filename, duration=100)`: Generates the GIF by filling in boxes one by one, flashing random boxes, and then erasing them.
- `main()`: Sets up the output directory and calls `generate_gif` to create the GIF.

## `main.py`

The `main.py` script generates a GIF based on an input file that specifies a color map and ASCII art. This allows for more customizable and complex GIFs compared to the `connections.py` script.

### How to Run

1. Ensure you have the required dependencies installed:
    ```sh
    pip install -r requirements.txt
    ```

2. Prepare an input file (e.g., `input/connections.txt`) with the desired configuration.

3. Run the script with the input file and specify the output GIF file:
    ```sh
    python src/main.py <input_file> <output_gif>
    ```

    Example:
    ```sh
    python src/main.py ./input/connections.txt output.gif
    ```

4. The generated GIF will be saved in the specified output file.
### Example Output
![Example GIF](example/m-output.gif)

### Main Functions

- `convert_to_rgb(color)`: Converts a color to RGB format.
- `parse_input_file(file_path)`: Parses the input file to extract the speed, color map, and ASCII art.
- `create_gif(color_map, ascii_art, output_path, box_size=20, fps=10, transparent_key=None)`: Creates a GIF based on the provided color map and ASCII art.

### Debugging

You can use the provided launch configuration in `launch.json` to debug `main.py` with arguments:
```json
{
    "name": "Python Debugger: Current File with Arguments",
    "type": "debugpy",
    "request": "launch",
    "program": "C:\\git\\gif-maker\\src\\main.py",
    "console": "integratedTerminal",
    "args": [
        "./input/connections.txt",
        "output.gif"
    ]
}
```

## Contact

[trailmatt.com](https://trailmatt.com).
