# Resume Chatbot
Evaluating the effectiveness of pretrained BERT models versus our own trained model on generating embeddings which deliver contextually relevant results when compared with an embedded user query. <br />  <br />
To generate embeddings, utilize the following command: <br />
`python embedder.py [path-to-data-folder] [name-of-output-file].csv` <br />
For example: `python embedder.py data/ACCOUNTANT accountant-embeddings.csv` <br /> <br />

Project structure represented as file tree: <br />

project_root/ <br />
│
├── data/ <br />
│   ├── ACCOUNTANT/ <br />
│   ├── ADVOCATE/ <br />
│   │   ... (other directories for different professions) <br />
│   └── TEACHER/ <br />
│ <br />
├── embeddings/ <br />
│   ├── bert-base-uncased-embeddings/ <br />
│   │   ├── accountant-embeddings.csv <br />
│   │   ├── advocate-embeddings.csv <br />
│   │   │   ... (other CSV files for other professions) <br />
│   │   └── teacher-embeddings.csv <br />
│ <br />
└── embedder.py <br />

