import requests
from os import makedirs
from os.path import join
from shutil import unpack_archive
from glob import glob
source = 'https://www.ssa.gov/oact/babynames/names.zip'

Data_zip_place = join('tempdata', 'names.zip')

makedirs('tempdata', exist_ok=True)

print("Downloading", source)
resp = requests.get(source)

with open(Data_zip_place, 'wb') as f:
    
    f.write(resp.content)

unpack_archive(Data_zip_place, extract_dir='tempdata')