# GIF Maker

Welcome to the GIF Maker project! This tool allows you to create GIFs from a series of images or a video file.

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

## Contact

[trailmatt.com](https://trailmatt.com).
