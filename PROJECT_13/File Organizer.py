import os
import shutil

# You can change this to any directory path
folder_path = input("Enter the path to the folder you want to organize: ")

# Define file type folders
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
    "Scripts": [".py", ".js", ".html", ".css", ".cpp", ".c", ".java"]
}

def organize_files(path):
    if not os.path.isdir(path):
        print("❌ Invalid folder path!")
        return

    for file in os.listdir(path):
        file_path = os.path.join(path, file)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file)
            moved = False

            for folder, extensions in file_types.items():
                if ext.lower() in extensions:
                    folder_path = os.path.join(path, folder)
                    os.makedirs(folder_path, exist_ok=True)
                    shutil.move(file_path, os.path.join(folder_path, file))
                    moved = True
                    break

            if not moved:
                others_path = os.path.join(path, "Others")
                os.makedirs(others_path, exist_ok=True)
                shutil.move(file_path, os.path.join(others_path, file))

    print("✅ Files organized successfully!")

organize_files(folder_path)