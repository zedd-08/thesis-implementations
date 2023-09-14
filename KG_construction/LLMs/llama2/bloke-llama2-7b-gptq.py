from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch

available_models = ['7B-GPTQ', '13B-GPTQ', '70B-GPTQ']
model_name = ''

while model_name not in available_models:
    print(f"Choose from: {available_models}")
    model_name = input("Which model do you want to run? ")

model_name_or_path = f"TheBloke/Llama-2-{model_name}"
# To use a different branch, change revision
# For example: revision="gptq-4bit-32g-actorder_True"
model = AutoModelForCausalLM.from_pretrained(model_name_or_path,
                                             torch_dtype=torch.float16,
                                             device_map="auto",
                                             revision="main")

tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, use_fast=True)

prompt = "Tell me about AI"
prompt_template=f'''{prompt}

'''

print("\n\n*** Generate:")

input_ids = tokenizer(prompt_template, return_tensors='pt').input_ids.cuda()
output = model.generate(inputs=input_ids, temperature=0.7, max_new_tokens=512)
print(tokenizer.decode(output[0]))

# Inference can also be done using transformers' pipeline

print("*** Pipeline:")
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=512,
    temperature=0.7,
    top_p=0.95,
    repetition_penalty=1.15
)

print(pipe(prompt_template)[0]['generated_text'])
