conda create -n jerex python=3.7
conda activate jerex
pip install torch==1.8.0+cu111 torchvision==0.9.0+cu111 torchaudio==0.8.0 torchtext==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html
yes | pip install -r requirements.txt