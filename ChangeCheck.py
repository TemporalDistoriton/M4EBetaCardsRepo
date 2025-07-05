import os
import sys
from pathlib import Path

def count_files_in_folder(folder_path):
    """
    Count the number of files in a given folder.
    Returns 0 if folder doesn't exist or is empty.
    """
    try:
        if not os.path.exists(folder_path):
            return 0
        
        # Count only files, not subdirectories
        file_count = len([f for f in os.listdir(folder_path) 
                         if os.path.isfile(os.path.join(folder_path, f))])
        return file_count
    except (PermissionError, OSError) as e:
        print(f"Error accessing {folder_path}: {e}")
        return 0

def compare_folder_counts(base_directory="."):
    """
    Compare file counts between current folders and their archived versions
    in ZZZ_Superceded/Previous/
    """
    # Convert to absolute path for clarity
    base_path = Path(base_directory).resolve()
    
    # Define folders to skip
    skip_folders = {"ZZZ_Superceded", "2d Model Art"}
    
    # Define the archive path
    archive_base = base_path / "ZZZ_Superceded" / "Previous"
    
    print(f"Scanning directory: {base_path}")
    print(f"Archive location: {archive_base}")
    print("-" * 50)
    
    # Check if archive directory exists
    if not archive_base.exists():
        print(f"Warning: Archive directory {archive_base} does not exist!")
        return
    
    # Get all subdirectories in the base path
    try:
        folders = [f for f in os.listdir(base_path) 
                  if os.path.isdir(os.path.join(base_path, f)) 
                  and f not in skip_folders]
    except (PermissionError, OSError) as e:
        print(f"Error reading base directory: {e}")
        return
    
    if not folders:
        print("No folders found to compare.")
        return
    
    print(f"Found {len(folders)} folders to compare:")
    
    # Process each folder
    results = []
    for folder_name in sorted(folders):
        current_folder = base_path / folder_name
        archive_folder = archive_base / folder_name
        
        # Count files in current folder
        current_count = count_files_in_folder(current_folder)
        
        # Count files in archive folder
        archive_count = count_files_in_folder(archive_folder)
        
        # Calculate difference
        difference = current_count - archive_count
        
        # Store result
        results.append({
            'folder': folder_name,
            'current': current_count,
            'archive': archive_count,
            'difference': difference
        })
        
        # Print result
        if difference > 0:
            print(f"{folder_name}: Increased by {difference} files (Current: {current_count}, Archive: {archive_count})")
        elif difference < 0:
            print(f"{folder_name}: Decreased by {abs(difference)} files (Current: {current_count}, Archive: {archive_count})")
        else:
            print(f"{folder_name}: No change ({current_count} files)")
    
    print("-" * 50)
    
    # Summary
    increased = sum(1 for r in results if r['difference'] > 0)
    decreased = sum(1 for r in results if r['difference'] < 0)
    unchanged = sum(1 for r in results if r['difference'] == 0)
    
    print(f"Summary:")
    print(f"  Folders with increased files: {increased}")
    print(f"  Folders with decreased files: {decreased}")
    print(f"  Folders with no change: {unchanged}")
    print(f"  Total folders compared: {len(results)}")

def main():
    """
    Main function to run the comparison.
    Can accept a directory path as command line argument.
    """
    # Check if a directory path was provided as argument
    if len(sys.argv) > 1:
        directory = sys.argv[1]
        if not os.path.exists(directory):
            print(f"Error: Directory '{directory}' does not exist.")
            sys.exit(1)
    else:
        # Use current directory by default
        directory = "."
    
    try:
        compare_folder_counts(directory)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()