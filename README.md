# 🚀 Python GML ML Pipeline

✅ Logistic Regression churn prediction  
✅ FastAPI REST endpoint  
✅ OpenAI summarisation for human-readable explanations


## 🔧 How to run

1. **Install requirements:**

```bash
pip install -r requirements.txt
```

2. **Run locally:**

```bash
uvicorn app:app --reload
```

- `app:app` loads the FastAPI app from `app.py`.
- `--reload` enables auto-reload for development (useful for code changes, not for production).

3. **Test with:**

```bash
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d '{"feature1": value, "feature2": value, ...}'
```

> Replace `YOUR_API_KEY` in `app.py` with your actual OpenAI key.


## 📂 Project Structure

```
Python_GML_ML_Pipeline/
├── app.py
├── requirements.txt
├── logistic_model.pkl
├── scaler.pkl
└── README.md
```


## 🐳 Run with Docker

1. **Build the Docker image:**

```bash
docker build -t python-gml-ml-pipeline .
```

2. **Run the Docker container:**

```bash
docker run -p 8000:8000 python-gml-ml-pipeline
```

3. **Access the FastAPI app:**

Open [http://localhost:8000](http://localhost:8000) in your browser.


## ✨ Author

[![Pierre-Henry Soria](https://avatars0.githubusercontent.com/u/1325411?s=200)](https://ph7.me "Pierre-Henry Soria, Software Developer")

Made with ❤️ by **[Pierre-Henry Soria](https://pierrehenry.be)**. A super passionate & enthusiastic Problem-Solver / Senior Software Engineer. Also a true cheese 🧀, ristretto ☕️, and dark chocolate lover! 😋

[![@phenrysay](https://img.shields.io/badge/x-000000?style=for-the-badge&logo=x)](https://x.com/phenrysay "Follow Me on X") [![pH-7](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/pH-7 "My GitHub") [![YouTube Video](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtu.be/cWBuZ4DXGK4 "YouTube SucceedAI Video") [![Bluesky](https://img.shields.io/badge/bluesky-1e90ff?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjMDAwMDAwIiBoZWlnaHQ9IjI0cHgiIHZpZXdCb3g9IjAgMCAzMiAzMiIgd2lkdGg9IjI0cHgiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTMwIDZsLTIuOTk5LTEuNjY2TDMyIDMuMzQgMjMuMTg5IDAgMTYuMDA2IDUuMzQgOC44MTMgMCAwIDMuMzQgNC45OTkgNC4zMzQgMCA2bDUuMDAxIDQuODAzTDQgMjAuODFWMjRsNS4wMDEtMS42NjZMMTYgMjhMMjIuOTk5IDIyLjM0IDMyIDI0di0zLjE4OUwyNy4wMDIgMTIgMzAgNiIgLz48L3N2Zz4=)](https://bsky.app/profile/ph7s.bsky.social "Bluesky Profile")


## 📌 Notes

- `logistic_model.pkl` and `scaler.pkl` are **placeholders**. Train and export your own models using `joblib.dump`.
- This project is a **modern, production-ready ML pipeline**, showcasing deployment and explainability best practices for 2025 and beyond.


### 🧠 Final Wise Principle

> **“AI models become valuable when they’re deployable, explainable, and integrated into real products that create business value.”**
