conda create -y -n scrape_fandom python=3.7
conda activate scrape_fandom
echo 'y' | pip install -r requirements.txt
git clone https://github.com/JOHW85/wikiextractor.git
cd wikiextractor
rm -rf .git .github
python setup.py install
cd ..