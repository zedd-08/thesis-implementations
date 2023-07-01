conda create -n scrape_fandom python=3.7
conda activate scrape_fandom
pip install -r requirements.txt
git clone https://github.com/JOHW85/wikiextractor.git
cd wikiextractor
rm -rf .git .github
python setup.py install
cd ..