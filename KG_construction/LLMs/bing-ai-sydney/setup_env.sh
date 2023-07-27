echo 'y' | conda env create -n sydney python
conda activate sydney 
echo 'y' | pip install sydney-py jupyter
ipython kernel install --name "askBert" --user