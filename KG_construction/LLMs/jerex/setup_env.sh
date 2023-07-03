conda create -y -n jerex python=3.7
conda activate jerex
echo 'y' | pip install torch==1.8.0+cu111 torchvision==0.9.0+cu111 torchaudio==0.8.0 torchtext==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html
echo 'y' | pip install -r requirements.txt