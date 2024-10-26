import os
import torch
import pandas as pd
from pdfminer.high_level import extract_text
from transformers import BertTokenizer, BertModel
from tqdm import tqdm


# we used this file to generate embeddings for all of the resumes
# within the 24 classes (job professions)
# this was ran locally, iterating thru all folders in a data/ directory

# referenced Hugging Face on creating pre trained bert class
# https://huggingface.co/docs/transformers/en/model_doc/bert
class PretrainedBertEmbedder:
    # model_name specifies which pretrained model we'd like to use
    # we can test out a few if we'd like
    def __init__(self, name='bert-base-uncased'):
        # pretrained bert embedding
        # if embedding takes too long locally, we can switch to colab and use gpu runtime
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = BertTokenizer.from_pretrained(name)
        self.model = BertModel.from_pretrained(name)
        self.model.to(self.device)

    def gen_embedding(self, text):
        # generate an embedding (single vector) for input text
        rows = self.tokenizer(text, return_tensors='pt', max_length=512, truncation=True, padding='max_length')
        rows = {key: value.to(self.device) for key, value in rows.items()}

        with torch.no_grad():
            outputs = self.model(**rows)
        # referenced Hugging Face on shaping the emebedding correctly
        # https://discuss.huggingface.co/t/run-pre-trained-llm-model-on-cpu-valueerror-expected-a-cuda-device-but-got-cpu/82144
        embeddings = outputs.last_hidden_state.mean(dim=1).squeeze().cpu().numpy()
        return embeddings


def convertcsv(dir, file):
    embedder = PretrainedBertEmbedder()
    embeddings = []
    files = []

    for file in tqdm(os.listdir(dir)):
        if file.endswith(".pdf"):
            path = os.path.join(dir, file)
            # referenced PDFMiner documentation to easily extract text from pdf file
            # https://pypi.org/project/pdfminer/
            embeddings.append(embedder.gen_embedding(extract_text(path)))
            files.append(file)

    df = pd.DataFrame(embeddings, index=files)
    df.to_csv(file)


def main(base):
    for sub in os.listdir(base):
        # consisent csv names so we can automate access
        convertcsv(os.path.join(base, sub), f"{sub.lower()}-embeddings.csv") 

if __name__ == "__main__":
    main("data/")