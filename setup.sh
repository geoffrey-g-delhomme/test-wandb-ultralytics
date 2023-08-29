conda create -p ./.venv -y python=3.10 pytorch torchvision pytorch-cuda=11.8 -c pytorch -c nvidia
. $(conda info --base)/etc/profile.d/conda.sh && conda activate ./.venv && pip install --upgrade pip
. $(conda info --base)/etc/profile.d/conda.sh && conda activate ./.venv && pip install -r requirements.txt