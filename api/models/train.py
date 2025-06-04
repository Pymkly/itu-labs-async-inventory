from ultralytics import YOLO

def train(_yml_file):
    model = YOLO("yolov8n.pt")
    result = model.train(
        data = _yml_file,
        name='version',  # Nom du dossier de sauvegarde des résultats
        device='cpu'
    )
    print("vita")