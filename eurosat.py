import tensorflow as tf
import os
import zipfile
import requests

# Download EuroSAT RGB dataset
data_url = 'http://madm.dfki.de/files/sentinel/EuroSAT.zip'
zip_file = './EuroSAT.zip'

if not os.path.exists(zip_file):
    print("Downloading dataset...")
    response = requests.get(data_url)
    with open(zip_file, 'wb') as f:
        f.write(response.content)

# Path to the extracted images
data_dir = '/scratch/skuma299/CEE598_20204/2750/'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
    
# Unzip the dataset
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(data_dir)

