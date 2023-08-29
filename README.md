Minimal example to launch ultralytics training + wandb callbacks on COCO128 with 2 GPUs.

# Setup

> **Required configuration**: 2 GPUs + conda

```bash
sh setup.sh
```

To install the PR:

```bash
BRANCH=...
pip install git+https://github.com/geoffrey-g-delhomme/wandb.git@${BRANCH} --ignore-installed
```

# Run

```bash
conda activate ./.venv
TASK=... # classify, detect, pose, segment
python train-${TASK}.py
```