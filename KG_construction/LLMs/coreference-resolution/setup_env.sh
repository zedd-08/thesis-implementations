conda create --name coref-res python=3.7.4
conda activate coref-res
echo 'y'| conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 cudatoolkit=11.3 -c pytorch
pip install spacy==2.1.0
python -m spacy download en_core_web_sm
git clone https://github.com/huggingface/neuralcoref.git
cd neuralcoref && rm -rf .git
pip install -r requirements.txt
pip install neuralcoref --no-binary neuralcoref
python setup.py build_ext --inplace
pip install -e .
cd .. && rm -rf neuralcoref
pip install allennlp chardet
pip install --pre allennlp-models
pip install jupyter
ipython kernel install --name "coref-res" --user