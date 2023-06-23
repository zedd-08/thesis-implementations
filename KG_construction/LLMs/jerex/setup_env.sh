conda create -n jerex python=3.7
conda activate jerex
conda install -y pytorch==1.8.1 torchvision==0.9.1 torchaudio==0.8.1 cudatoolkit=11.3 -c pytorch -c conda-forge
yes | pip install -r requirements.txt