import os
import glob
from PIL import Image

def convert_jpg_to_png(root_folder):
    # Find all jpg files recursively
    jpg_files = []
    for ext in ['*.jpg', '*.jpeg', '*.JPG', '*.JPEG']:
        pattern = os.path.join(root_folder, '**', ext)
        jpg_files.extend(glob.glob(pattern, recursive=True))
    
    print(f"Found {len(jpg_files)} JPG files to convert")
    
    # Convert each file
    for jpg_file in jpg_files:
        try:
            # Get the output filename (change extension to .png)
            png_file = os.path.splitext(jpg_file)[0] + '.png'
            
            # Open and convert the image
            with Image.open(jpg_file) as img:
                # Save as PNG
                img.save(png_file, 'PNG')
            
            print(f"Converted: {jpg_file} -> {png_file}")
            
            # Optional: remove the original jpg file
            # os.remove(jpg_file)
            
        except Exception as e:
            print(f"Error converting {jpg_file}: {e}")
    
    print("Conversion complete!")

# Use the current directory
if __name__ == "__main__":
    current_dir = os.getcwd()  # Gets the current working directory
    print(f"Starting conversion in: {current_dir}")
    convert_jpg_to_png(current_dir)