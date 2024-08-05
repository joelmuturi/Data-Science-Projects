import zipfile
import os

# Specify the paths
zip_file_path = "C:\\Users\\Joel\\kaggle_datasets\\weather-data-set-for-beginners.zip"
extract_dir = "C:\\Users\\Joel\\kaggle_datasets\\weather_dataset"

# Create the extraction directory if it doesn't exist
os.makedirs(extract_dir, exist_ok=True)

# Extract the dataset
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

# List extracted files
print("Extracted files:", os.listdir(extract_dir))
