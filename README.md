# 🖼️ Digital Image Processing: Sampling & Quantization

## 📌 Project Overview

This project explores two fundamental concepts of **Digital Image Processing (DIP)**: spatial sampling and color quantization. Using Python, it demonstrates how reducing image resolution and color depth affects image quality and visual appearance.

## 🧠 Methodology

The project is divided into two parts:

**1. Spatial Sampling (`sampling.py`)**
- Reduce image resolution to different sizes (1024×1024 down to 32×32).
- Upscale the reduced images to their original dimensions.
- Visualize pixelation and information loss.

**2. Color Quantization (`quantization.py`)**
- Reduce color bit depth from 8 bits to 1 bit per channel.
- Compare the number of available color levels.
- Visualize color degradation using images and histograms.

## 🛠️ Technologies Used

- Python
- OpenCV
- NumPy
- Matplotlib

## 📊 Results & Visualization

The project generates comparison figures showing the effects of different sampling resolutions and quantization levels, making image quality degradation and information loss easier to understand.

## 🚀 Getting Started

1. Install the required libraries:
   `pip install opencv-python numpy matplotlib`
2. Place the input image (`powder.jpg`) in the same directory as the scripts.
3. Run the scripts:

   `python sampling.py`

   `python quantization.py`

## 🎯 Objective

To understand how spatial resolution and color depth influence digital image representation, storage, and visual quality.
