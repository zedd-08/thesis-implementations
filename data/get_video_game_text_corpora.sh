echo "Fetching scraped WOWHead dataset, by Jakub Mysliwiec"
wget -O wow_quests_dataset.txt https://jakub.thebias.nl/GPT2_WOWHead_dataset.txt

echo "Fetching Video game text corpora by Judith van Stegeren et al."
git clone git@github.com:hmi-utwente/video-game-text-corpora.git
cd video-game-text-corpora && rm -rf .git && cd ../

echo "Fetching GPT2 Quest generation dataset by Sam Vartinen et al."
git clone git@github.com:svartinen/gpt2-quest-descriptions.git VartinenQuests
cd VartinenQuests && rm -rf .git && cd ../