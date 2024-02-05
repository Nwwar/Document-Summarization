from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from transformers import T5Tokenizer, T5ForConditionalGeneration
from transformers import pipeline
import torch


checkpoint = 'MBZUAI/LaMini-Flan-T5-248M'
tokenizer = T5Tokenizer.from_pretrained(checkpoint)
model = T5ForConditionalGeneration.from_pretrained(checkpoint,
                                                   device_map='auto',
                                                   torch_dtype=torch.float32,
                                                   offload_folder="offload")


def file_preprocessing(file):
    loader = PyPDFLoader(file)
    pages = loader.load_and_split()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=200,
                                                   chunk_overlap=50)
    texts = text_splitter.split_documents(pages)
    final_text = ''
    for text in texts:
        final_text += text.page_content
    return final_text


def llm_pipeline(file_path):
    pipe_sum = pipeline('summarization',
                        model=model,
                        tokenizer=tokenizer,
                        max_length=350,
                        min_length=50)
    text = file_preprocessing(file_path)
    summary = pipe_sum(text)[0]['summary_text']
    return summary
