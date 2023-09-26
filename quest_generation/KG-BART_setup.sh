git clone git@github.com:yeliu918/KG-BART.git
cd KG-BART/KGBART/KGBART_training
mv run_seq2seq.py ../
mv decode_seq2seq.py ../
cd ../../

echo "Creating venv for KG-BART"

conda create -n 'kgbart' python=3.7
conda activate kgbart
conda install pytorch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 pytorch-cuda=11.6 -c pytorch -c nvidia
git clone https://github.com/NVIDIA/apex && cd apex
pip install packaging
pip install -v --disable-pip-version-check --no-build-isolation --no-cache-dir ./
cd ../ && rm -rf apex/
pip install tqdm numpy tokenizers regex prefetch_generator
echo "To run training use the following commands:"
echo "cd KGBART"
echo "CUDA_VISIBLE_DEVICES=0 python run_seq2seq.py --data_dir dataset/commongen_data/commongen --output_dir output/KGBart --log_dir log/KGBart --model_recover_path output/Pretraining_KG/best_model/model.best.bin --fp16 True --max_seq_length 32 --max_position_embeddings 64 --max_len_a 32 --max_len_b 64 --max_pred 64 --train_batch_size 60 --eval_batch_size 48 --gradient_accumulation_steps 6 --learning_rate 0.00001 --warmup_proportion 0.1 --label_smoothing 0.1 --num_train_epochs 10"
echo "Training per epoch takes approximately 40 min"
echo ""
echo "To run inference use the following commands:"
echo "cd KGBART"
echo "python decode_seq2seq.py --data_dir /home/jovyan/manish-thesis/KG-BART/dataset/commongen_data/commongen --model_recover_path /home/jovyan/manish-thesis/KG-BART/output/KGBart/best_model/model.best.bin --input_file /home/jovyan/manish-thesis/KG-BART/dataset/commongen_data/commongen/commongen.dev.src_new.txt --output_dir /home/jovyan/manish-thesis/KG-BART/output/KGBart/best_model/Gen --output_file model.best --split dev --beam_size 5 --forbid_duplicate_ngrams True"