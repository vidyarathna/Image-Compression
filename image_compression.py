import cv2
from PIL import Image
import argparse

def lossy_compression(input_image_path, output_image_path, quality=90):
    # Read the image
    image = cv2.imread(input_image_path)

    # Save the image with specified compression quality
    cv2.imwrite(output_image_path, image, [int(cv2.IMWRITE_JPEG_QUALITY), quality])

    print(f"Lossy compression saved to {output_image_path} with quality {quality}")

def lossless_compression(input_image_path, output_image_path, compression_level=9):
    # Open the image using PIL
    image = Image.open(input_image_path)

    # Save the image with specified compression level
    image.save(output_image_path, format='PNG', compress_level=compression_level)

    print(f"Lossless compression saved to {output_image_path} with compression level {compression_level}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Image Compression Script')
    parser.add_argument('--input_image', type=str, required=True, help='Path to the input image')
    parser.add_argument('--output_image_lossy', type=str, required=True, help='Path to the output lossy compressed image')
    parser.add_argument('--output_image_lossless', type=str, required=True, help='Path to the output lossless compressed image')
    parser.add_argument('--quality', type=int, default=90, help='Quality for lossy compression (1-100)')
    parser.add_argument('--compression_level', type=int, default=9, help='Compression level for lossless compression (0-9)')

    args = parser.parse_args()

    # Perform lossy compression
    lossy_compression(args.input_image, args.output_image_lossy, args.quality)

    # Perform lossless compression
    lossless_compression(args.input_image, args.output_image_lossless, args.compression_level)


