# Parking Spot Detection System

This repository contains a project for detecting empty parking spots in an image. The system uses a trained Convolutional Neural Network (CNN) model to classify parking spots as empty or occupied based on the provided training data. 

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Step 1: Annotate Parking Spots](#step-1-annotate-parking-spots)
  - [Step 2: Train the Model](#step-2-train-the-model)
  - [Step 3: Detect Empty Parking Spots](#step-3-detect-empty-parking-spots)
- [Files](#files)
- [Acknowledgments](#acknowledgments)

## Requirements

- Python 3.6 or higher
- OpenCV
- Keras
- TensorFlow
- NumPy
- scikit-learn

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/AniBirage/Empty-Parking-Spot-Detection.git
    cd Empty-Parking-Spot-Detection\Empty_Parking_Spot_Detection
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Step 1: Annotate Parking Spots

Run `ParkingSpotCoordinates.py` to manually annotate the parking spots in the image. Click and drag to draw rectangles around each parking spot.

```sh
python ParkingSpotCoordinates.py
```

### Step 2: Train the Model

Run `EmptyParkingSpotDetectionModel.py` to train the CNN model using the provided training data (folders `empty` and `occupied`).

```sh
python EmptyParkingSpotDetectionModel.py
```

### Step 3: Detect Empty Parking Spots

Run `EmptyParkingSpotDetectionSystem.py` to detect empty parking spots in the given image.

```sh
python EmptyParkingSpotDetectionSystem.py
```

## Files

- `ParkingSpotCoordinates.py`: Script to annotate parking spots in an image.
- `EmptyParkingSpotDetectionModel.py`: Script to train the CNN model.
- `EmptyParkingSpotDetectionSystem.py`: Script to detect empty parking spots using the trained model.
- `Coordinates.txt`: Text file containing the coordinates of the annotated parking spots.
- `empty/`: Folder containing images of empty parking spots (training data).
- `occupied/`: Folder containing images of occupied parking spots (training data).
- `image.jpg`: Image used for testing the system.

## Acknowledgments

This project uses the following libraries and resources:

- [OpenCV](https://opencv.org/)
- [Keras](https://keras.io/)
- [TensorFlow](https://www.tensorflow.org/)
- [NumPy](https://numpy.org/)
- [scikit-learn](https://scikit-learn.org/)

Feel free to contribute to this project by creating pull requests or reporting issues.
```
