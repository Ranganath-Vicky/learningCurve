#%% ## Libraries Required
# !pip install langchain-huggingface
# ## For API Calls
# !pip install huggingface_hub
# !pip install transformers
# !pip install accelerate
# !pip install  bitsandbytes
# !pip install langchain

# %%
import os 
sec_key = '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'
os.environ["HUGGINGFACE_TOKEN"] = sec_key
print(os.getenv('HUGGINGFACE_TOKEN'))

# %%
# TO ACCESS AND CALL HUGGINGFACE MODEL
# HUGGINGFACE ENDPOINT

from langchain_huggingface import HuggingFaceEndpoint

repo_id = "mistralai/Mistral-7B-Instruct-v0.3"
llm = HuggingFaceEndpoint(repo_id = repo_id, temperature=0.7, max_new_tokens=128,huggingfacehub_api_token = sec_key)
# llm.invoke("What is Machine Learning")

# %%
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

question = "Who won the cricket world cup in the year 2011?"
template = """Question:{question}
            Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=['question'])
print(prompt)

# %%
llm_chain = LLMChain(llm=llm, prompt = prompt)
print(llm_chain.invoke(question))

# %%
## HUGGINGFACE PIPELINE

from langchain_huggingface import HuggingFaceEndpoint
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

#%%
model_id = "gpt2"

model = AutoModelForCausalLM.from_pretrained(model_id)
tokenizer = AutoTokenizer.from_pretrained(model_id)

# %%
# TASK THAT NEEDS TO BE DONE

from langchain_huggingface.llms import HuggingFacePipeline

pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=100)
hf = HuggingFacePipeline(pipeline=pipe)

# %%

hf.invoke("What is MacBook")
# %%

## HuggingFace pipeline with GPUs 

gpu_llm = HuggingFacePipeline.from_model_id(
    model_id=model_id,
    task="text-generation",
    device=-1,
    pipeline_kwargs={"max_new_tokens": 128}
)
# %%
chain = prompt|gpu_llm
# %%
question = "What is GPU"
chain.invoke({"question":question})
# %%
