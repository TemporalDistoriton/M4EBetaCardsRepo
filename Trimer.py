import os
import re
import sys

def rename_folders():
    # Get the current directory (where the script is running)
    current_dir = os.getcwd()
    
    # Create a regular expression pattern that matches your actual folder format
    # M4E_Stat-Cards_<FOLDERNAME>_DRAFT_<DATE>
    pattern = r"M4E_Stat-Cards_(.+?)_DRAFT_[\d\.]+$"
    
    # Counter for tracking renamed folders
    renamed_count = 0
    
    # List all directories in the current folder
    for item in os.listdir(current_dir):
        # Check if it's a directory
        if os.path.isdir(os.path.join(current_dir, item)):
            # Check if it matches our pattern
            match = re.match(pattern, item)
            if match:
                # Extract the FOLDERNAME part
                new_name = match.group(1)
                
                # Create the full paths
                old_path = os.path.join(current_dir, item)
                new_path = os.path.join(current_dir, new_name)
                
                # Rename the folder
                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed: '{item}' -> '{new_name}'")
                    renamed_count += 1
                except Exception as e:
                    print(f"Error renaming '{item}': {e}")
    
    # Report results
    if renamed_count > 0:
        print(f"\nSuccessfully renamed {renamed_count} folder(s).")
    else:
        print("\nNo matching folders found to rename.")

if __name__ == "__main__":
    print("Starting folder rename operation...")
    rename_folders()
    print("Operation complete.")