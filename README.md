# Data Engineering Toolkit  

A lightweight practice repository designed to demonstrate **data engineering fundamentals** using a simple **ETL pipeline**:  

- **cleaning.py** → Handles raw data preprocessing (missing values, duplicates, formatting).  
- **transform.py** → Applies business logic, enriches data, and prepares it for loading.  
- **load.py** → Persists the processed data into storage formats (CSV/Parquet) or databases.  

This project also serves as a sandbox for learning **Git & GitHub workflows**, including branching, commits, and pull requests.  

---

## 🚀 Getting Started  

### Prerequisites  
- Python 3.8+  
- Install dependencies from `requirements.txt`:  

```bash
pip install -r requirements.txt
Running the Scripts
Run the scripts sequentially to simulate the ETL pipeline:

bash
Copy code
python cleaning.py
python transform.py
python load.py
Outputs will be saved in the project folder as CSV and Parquet files.
```

# 📖 Documentation
Each script includes inline comments explaining:

The purpose of the script

Key steps performed

Example outputs

# 🤝 Contribution Guide
We follow a feature-branch workflow:

Create a branch from develop:

bash
Copy code
git checkout develop
git pull
git checkout -b feature/<your-feature-name>
Commit small, meaningful changes:

bash
Copy code
git commit -m "Add transformation for age grouping"
Push and open a Pull Request into develop.
