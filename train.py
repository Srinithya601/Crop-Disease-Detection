import os
from src.dataset import load_data
from src.model import build_model

if __name__ == "__main__":
    data_dir = "./data/plantvillage"
    train, val = load_data(data_dir)

    model = build_model(num_classes=train.num_classes)
    model.fit(train, validation_data=val, epochs=5)
    model.save("models/model.h5")