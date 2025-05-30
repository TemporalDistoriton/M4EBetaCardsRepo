import os
from PIL import Image

def convert_jpg_to_png(root_folder):
    jpg_extensions = ('.jpg', '.jpeg', '.JPG', '.JPEG')
    converted_count = 0
    skipped_count = 0

    # Only go one level deep into subfolders
    for subfolder in os.listdir(root_folder):
        subfolder_path = os.path.join(root_folder, subfolder)
        if os.path.isdir(subfolder_path):
            for file in os.listdir(subfolder_path):
                if file.endswith(jpg_extensions):
                    jpg_file = os.path.join(subfolder_path, file)
                    png_file = os.path.splitext(jpg_file)[0] + '.png'

                    if os.path.exists(png_file):
                        print(f"Skipping (already exists): {png_file}")
                        skipped_count += 1
                        continue

                    try:
                        with Image.open(jpg_file) as img:
                            img.save(png_file, 'PNG')
                        print(f"Converted: {jpg_file} -> {png_file}")
                        # os.remove(jpg_file)  # Optional
                        converted_count += 1
                    except Exception as e:
                        print(f"Error converting {jpg_file}: {e}")

    print(f"\nConversion complete! {converted_count} files converted, {skipped_count} skipped.")

if __name__ == "__main__":
    current_dir = os.getcwd()
    print(f"Starting conversion in: {current_dir}")
    convert_jpg_to_png(current_dir)
