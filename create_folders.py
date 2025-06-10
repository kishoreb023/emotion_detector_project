import os

# Base project directory
base_dir = "emotion_detector_project"

# Folders to create
folders = [
    "emotion_detector",
    "tests",
    "static_code_analysis",
    "app"
]

# Create base directory
os.makedirs(base_dir, exist_ok=True)

# Create subdirectories
for folder in folders:
    path = os.path.join(base_dir, folder)
    os.makedirs(path, exist_ok=True)

# Create empty __init__.py file inside emotion_detector
init_file = os.path.join(base_dir, "emotion_detector", "__init__.py")
with open(init_file, "w") as f:
    f.write("")

print("📁 Folder structure created successfully!")
