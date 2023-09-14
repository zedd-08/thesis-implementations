echo "Creating venv for llama2 and GPTQ"
conda create -n llama2 python=3.10
conda activate llama2
conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
pip install 'transformers>=4.32.0' 'optimum>=1.12.0' cchardet
pip install auto-gptq --extra-index-url https://huggingface.github.io/autogptq-index/whl/cu117/

# Install LLAMA
read -p "Download LLAMA 2 full model? (requires token to download from facebookresearch/llama) [y/n]: " install
if [ "$install" != "${install#[Yy]}" ] ;then
	echo "Installing LLAMA"
	git clone git@github.com:facebookresearch/llama.git
	cd llama && . ./download.sh
	pip install -e .
	cd ..
else
	echo "Skipping LLAMA installation"
	exit 0
fi