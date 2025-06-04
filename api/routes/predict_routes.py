from fastapi import APIRouter, UploadFile, File
from typing import List

from api.detector.detector import InventoryModel
from api.utils.save_files import save_files

router = APIRouter()
inventory_model = InventoryModel()

@router.post('/inventory')
async def inventory(files: List[UploadFile] = File(...)):
    image_names = await save_files(files)
    _result = inventory_model.predict(image_names)
    return _result