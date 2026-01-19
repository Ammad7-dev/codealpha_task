import os
import shutil

def organize_files():
    # Get the current directory where this script is saved
    current_dir = os.getcwd()
    target_folder = "Organized_Images"
    target_path = os.path.join(current_dir, target_folder)

    print(f"Scanning directory: {current_dir}")

    # --- STEP 1: CREATE THE FOLDER ---
    if not os.path.exists(target_path):
        os.makedirs(target_path)
        print(f"Created folder: {target_folder}")

    # --- STEP 2: TEST DATA (Optional) ---
    # This creates 3 empty .jpg files just so you can see the code work!
    for i in range(1, 4):
        test_file = f"test_image_{i}.jpg"
        if not os.path.exists(test_file):
            with open(test_file, 'w') as f:
                f.write("test data")
            print(f"Created test file: {test_file}")

    # --- STEP 3: AUTOMATION LOGIC ---
    files_moved = 0
    
    # List all files in the current directory
    for filename in os.listdir(current_dir):
        # We only want files (not folders) and specifically .jpg or .png
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            source_file = os.path.join(current_dir, filename)
            destination_file = os.path.join(target_path, filename)

            # Move the file
            try:
                shutil.move(source_file, destination_file)
                print(f"SUCCESS: Moved {filename} to {target_folder}/")
                files_moved += 1
            except Exception as e:
                print(f"ERROR: Could not move {filename}: {e}")

    # --- STEP 4: SUMMARY ---
    print("-" * 30)
    if files_moved > 0:
        print(f"Task Complete! {files_moved} files were organized.")
    else:
        print("No image files found to move.")

if __name__ == "__main__":
    organize_files()