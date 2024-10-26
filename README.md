# Relevant Resume Retrieval Using NLP Approaches
Assessing basic Natural Language Processing (NLP) approaches towards building
resume screening pipelines for relevant candidate recruitment <br />  <br />
To generate embeddings, utilize the following command: <br />
`python embedder.py [path-to-data-folder] [name-of-output-file].csv` <br />
For example: `python embedder.py data/ACCOUNTANT accountant-embeddings.csv` <br /> <br />

Link to Kaggle Resume dataset used: https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset?resource=download <br /> <br />
![project-diagram](https://github.com/user-attachments/assets/0366e54c-a542-4b18-bdbd-17ce6a533199)

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
└── model.py <br />

