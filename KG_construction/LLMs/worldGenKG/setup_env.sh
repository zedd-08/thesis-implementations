conda env create -f environment.yml 
conda activate askBert 
conda install pytorch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 cudatoolkit=11.0 -c pytorch
yes | pip install -r requirements.txt
export SQUAD_DIR=`pwd`/SQuAD-2.0