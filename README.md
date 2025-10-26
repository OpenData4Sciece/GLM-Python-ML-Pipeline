# 🚀 Python GML ML Pipeline

[![HowTo Data Science: Logistic Regression model churn probability](https://i1.ytimg.com/vi/JbmfmgPlpXc/sddefault.jpg)](https://www.youtube.com/watch?v=JbmfmgPlpXc)

[→ Watch it directly on YouTube](https://www.youtube.com/watch?v=JbmfmgPlpXc)

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
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d '{
  "age": 45.0,
  "tenure": 24.0,
  "monthly_charges": 79.85,
  "total_charges": 1800.0,
  "contract_type": "Month-to-month",
  "payment_method": "Electronic check"
}'
```

---

## 🔑 Environment Setup

**Set your OpenAI API key:**

```bash
export OPENAI_API_KEY="your_actual_openai_api_key"
```


## 📂 Project Structure

```
Python_GML_ML_Pipeline/
├── app.py                  # FastAPI application
├── requirements.txt        # Python dependencies
├── logistic_model.pkl     # Trained ML model (placeholder)
├── scaler.pkl            # Feature scaler (placeholder)
├── Dockerfile            # Container configuration
├── .gitignore           # Git ignore rules
└── README.md           # This file
```


## 🐳 Run with Docker

1. **Build the Docker image:**

```bash
docker build -t python-gml-ml-pipeline .
```

2. **Run the Docker container:**

```bash
docker run -p 8000:8000 -e OPENAI_API_KEY="your_actual_openai_api_key" python-gml-ml-pipeline
```

3. **Access the FastAPI app:**

- **API**: [http://localhost:8000](http://localhost:8000)
- **Health Check**: [http://localhost:8000/health](http://localhost:8000/health)
- **Interactive Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **OpenAPI Schema**: [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json)


## 🧑‍🎓 Learn More - How does this pipeline run?
**Execution Flow:**

1. **Load trained model and scaler** (using `joblib`).
2. **API endpoint receives JSON data** (new user or input data).
3. **Dataframe creation & scaling** for consistency with training.
4. **Model predicts** churn probability (or other target).
5. **Returns JSON response** with prediction for integration into apps or dashboards.


✅ Run locally:
```console
uvicorn app:app --reload
```

✅ Run in Docker:
```console
docker build -t python-gml-ml-pipeline .
docker run -p 8000:8000 -e OPENAI_API_KEY="your_actual_openai_api_key" python-gml-ml-pipeline
```

**Key reasons to use FastAPI:**
1. Modern async Python framework
2. Automatic **OpenAPI schema & Swagger docs**
3. Production-grade performance
4. Can be integrated into **microservices/SaaS**


## ✨ Author

[![Pierre-Henry Soria](https://avatars0.githubusercontent.com/u/1325411?s=200)](https://ph7.me "Pierre-Henry Soria, Software Developer")

Made with ❤️ by **[Pierre-Henry Soria](https://pierrehenry.be)**. A super passionate & enthusiastic Problem-Solver / Senior Software Engineer. Also a true cheese 🧀, ristretto ☕️, and dark chocolate lover! 😋

[![@phenrysay](https://img.shields.io/badge/x-000000?style=for-the-badge&logo=x)](https://x.com/phenrysay "Follow Me on X") [![pH-7](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/pH-7 "My GitHub") [![YouTube Video](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@pH7Programming/videos "My Tech YouTube Channel") [![BlueSky](https://img.shields.io/badge/BlueSky-00A8E8?style=for-the-badge&logo=bluesky&logoColor=white)](https://bsky.app/profile/ph7s.bsky.social "Follow Me on BlueSky")


## 📌 Notes

- `logistic_model.pkl` and `scaler.pkl` are **placeholders**. Train and export your own models using `joblib.dump`.
- This project is a **modern, production-ready ML pipeline**, showcasing deployment and explainability best practices for 2025 and beyond.


### 🧠 Final Wise Principle

> **“AI models become valuable when they’re deployable, explainable, and integrated into real products that create business value.”**
