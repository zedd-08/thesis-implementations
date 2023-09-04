conda create -n 'data_expl' python
conda activate 'data_expl'
pip install pandas numpy scipy xlrd
pip install jupyter
ipython kernel install --name "data_expl" --user