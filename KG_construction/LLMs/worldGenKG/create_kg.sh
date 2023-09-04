conda activate askBert
cd KG-extraction
python kg-extraction.py --input_text $1
parent="$(dirname "$1")"
basename=`echo $(basename "$1")|cut -f '1' -d '.'`
cp graph.dot ${parent}/${basename}.dot
cd ../flavortext-generation
python flavortext.py --input_text $1 --run_name run1
cp graph.dot ../${basename}.dot
cp graph.gml ../${basename}.gml
cd ../