Minimal example to launch ultralytics training + wandb callbacks on COCO128 with 2 GPUs.

# Setup

> **Required configuration**: 2 GPUs + conda

```bash
sh setup.sh
```

To install the PR:

```bash
pip install -R requirements-pr.txt
```

# Run

```bash
conda activate ./.venv
python train.py
```