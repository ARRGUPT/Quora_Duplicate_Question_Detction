# Quora Duplicate Question Detection

This project is a **Streamlit web application(Quora_Duplicate_Question_Detction)** that detects whether two questions are duplicates, inspired by the Quora Question Pairs challenge. It uses NLP techniques and a machine learning model trained on question pairs to predict if two questions have the same meaning.

## Features

- Clean and modern Streamlit web interface
- Input two questions and get instant prediction
- Uses advanced NLP features (token, length, fuzzy, and word2vec)
- ML model for fast inference

## How to Use

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/quora_question_pair.git
   cd quora_question_pair
   ```

2. **Install dependencies**  
   Make sure you have Python 3.7+ installed.  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app locally**  
   ```bash
   streamlit run app.py
   ```

4. **Or try it online**  
   👉 [Live Streamlit App](https://quoraduplicatequestiondetction-94uzt2as8hmyp4ya4pm6xv.streamlit.app/)

## Project Structure

```
quora_question_pair/
│
├── app.py                # Streamlit web app
├── helper.py             # Feature engineering and preprocessing
├── model.pkl             # Trained ML model (not tracked in git)
├── w2v_model.pkl         # Word2Vec model (not tracked in git)
├── requirements.txt      # Python dependencies
├── .gitignore            # Files and folders to ignore in git
└── README.md             # Project documentation
```

## Requirements

- streamlit
- numpy
- pandas
- scikit-learn
- beautifulsoup4
- nltk
- distance
- rapidfuzz
- pickle (standard library)

Install all dependencies with:
```bash
pip install -r requirements.txt
```

## Model & Data

- The app uses a pre-trained ML model (`model.pkl`) and a Word2Vec model (`w2v_model.pkl`).
- These files are not included in the repository due to size.  
  Place them in the project root before running the app.

## Credits

- [Quora Question Pairs Kaggle Competition](https://www.kaggle.com/c/quora-question-pairs)
- Streamlit, NLTK, RapidFuzz, Gensim

---

**Try the app online:**  
[https://quoraduplicatequestiondetction-94uzt2as8hmyp4ya4pm6xv.streamlit.app/](https://quoraduplicatequestiondetction-94uzt2as8hmyp4ya4pm6xv.streamlit.app/)

---