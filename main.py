from api.detector.detector import InventoryModel

model = InventoryModel()
result = model.predict(["3.jpg", "1.jpg"])
print(result)