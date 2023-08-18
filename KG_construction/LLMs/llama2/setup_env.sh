conda create -n llama python
conda activate llama
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia

git clone git@github.com:facebookresearch/llama.git
cd llama && . ./download.sh
pip install -e .
cd ..