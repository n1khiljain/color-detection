# Real-Time Color Detection

A Python application that detects and tracks specific colors in real-time using your webcam. The program draws a bounding box around detected colored objects.

## Features

- Real-time webcam color detection
- Automatic HSV color range calculation
- Bounding box visualization around detected objects
- Support for any BGR color

## Requirements

- Python 3.9+
- Webcam

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/n1khiljain/color-detection.git
   cd color-detection
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main script:

```bash
python main.py
```

Press `q` to quit the application.

### Detecting Different Colors

To detect a different color, modify the `color` parameter in `main.py`:

```python
# Colors are defined in BGR format
YELLOW = [0, 255, 255]
BLUE = [255, 0, 0]
RED = [0, 0, 255]
GREEN = [0, 255, 0]

# Change the color passed to detect_color()
detect_color(color=YELLOW)
```

## How It Works

1. Captures video frames from the webcam
2. Converts each frame from BGR to HSV color space
3. Creates a mask for pixels within the target color range
4. Finds the bounding box of the masked region
5. Draws a rectangle around the detected color

## Project Structure

```
color-detection/
├── main.py          # Main application with color detection logic
├── util.py          # Utility functions for HSV limit calculation
├── requirements.txt # Python dependencies
└── README.md        # This file
```

