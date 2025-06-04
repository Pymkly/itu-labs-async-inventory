import os.path

from ultralytics import YOLO

def count(_list, result):
    for li in _list:
        try:
            _ = result[li]
            result[li] += 1
        except KeyError:
            result[li] = 1
    return result

class InventoryModel:
    def __init__(self):
        self.model = YOLO("runs/detect/version2/weights/best.pt")

    def predict(self, _paths):
        _paths_temp = []
        for _path in _paths:
            _path = os.path.join("images/predict", _path)
            _paths_temp.append(_path)
        _results = self.model(_paths_temp)
        _cls = {}
        for result in _results:
            _res = [int(i) for i in result.boxes.cls]
            _cls = count(_res, _cls)
        return _cls