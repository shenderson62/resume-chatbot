# Resume Chatbot
Evaluating the effectiveness of pretrained BERT models versus our own trained model on generating embeddings which deliver contextually relevant results when compared with an embedded user query.
To generate embeddings, utilize the following command:
`python embedder.py [path-to-data-folder] [name-of-output-file].csv`
For example: `python embedder.py data/ACCOUNTANT accountant-embeddings.csv`

Project structure represented as file tree:

project_root/
│
├── data/
│   ├── ACCOUNTANT/
│   ├── ADVOCATE/
│   │   ... (other directories for different professions)
│   └── TEACHER/
│
├── bert-base-uncased-embeddings/
│   ├── accountant-embeddings.csv
|   ├── advocate-embeddings.csv
│   │   ... (other directories for embeddings corresponding to other professions)
|   └── teacher-embeddings.csv
│
└── embedder.py
