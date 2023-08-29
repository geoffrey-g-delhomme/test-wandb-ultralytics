from dotenv import load_dotenv

load_dotenv('./.env')

import numpy as np
from ultralytics import YOLO
from wandb.yolov8 import add_wandb_callback

if __name__ == "__main__":

    model = YOLO('yolov8n-seg.yaml')

    add_wandb_callback(
        model,
        enable_model_checkpointing=True,
        enable_train_validation_logging=True,
        enable_validation_logging=True,
        enable_prediction_logging=True,
        max_validation_batches=1,
        visualize_skeleton=True
    )

    results = model.train(
        data='coco128-seg.yaml',
        device=None,
        epochs=2,
        batch=2*2,
        workers=2
    )

    print(results)