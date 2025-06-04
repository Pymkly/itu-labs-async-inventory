from fastapi import UploadFile, File
from typing import List
import time

async def save_files(files: List[UploadFile] = File(...)):
    image_names = []
    for file in files:
        # Sauvegarder chaque image
        unique_filename = f"{int(time.time())}_{file.filename}"
        file_location = f"images/predict/{unique_filename}"
        with open(file_location, "wb") as f:
            content = await file.read()
            f.write(content)
        image_names.append(unique_filename)
    return image_names