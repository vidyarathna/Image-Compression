### Image Compression

This repository contains a Python script (`image_compression.py`) that provides functionality for both lossy and lossless compression of images using OpenCV and PIL libraries.

### Features

- **Lossy Compression**: Uses OpenCV to compress an image with specified JPEG quality.
- **Lossless Compression**: Utilizes PIL to compress an image with specified PNG compression level.

### Requirements

- Python 3.x
- OpenCV (`pip install opencv-python`)
- Pillow (`pip install pillow`)

### Usage

To compress an image, run the script with the following command:

```bash
python image_compression.py --input_image /path/to/your/input_image.jpg --output_image_lossy /path/to/output_lossy_compressed.jpg --output_image_lossless /path/to/output_lossless_compressed.png --quality 85 --compression_level 6
```

#### Arguments

- `--input_image`: Path to the input image (required).
- `--output_image_lossy`: Path to save the output lossy compressed image (required).
- `--output_image_lossless`: Path to save the output lossless compressed image (required).
- `--quality`: Quality for lossy compression (1-100, default: 90).
- `--compression_level`: Compression level for lossless compression (0-9, default: 9).

### Example

```bash
python image_compression.py --input_image /path/to/your/input_image.jpg --output_image_lossy /path/to/output_lossy_compressed.jpg --output_image_lossless /path/to/output_lossless_compressed.png --quality 85 --compression_level 6
```

### Notes

- Adjust paths (`/path/to/your/`) according to your specific file locations.
- Ensure that both OpenCV (`cv2`) and Pillow (`PIL`) libraries are installed before running the script.
- Experiment with different quality levels (`--quality`) and compression levels (`--compression_level`) to achieve desired image sizes and quality.
