import re
from typing import List, Dict, Tuple
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')


def get_message_counts(user_msgs: List[str], ai_msgs: List[str]) -> Dict[str, int]:
    return {
        "total_messages": len(user_msgs) + len(ai_msgs),
        "user_messages": len(user_msgs),
        "ai_messages": len(ai_msgs)
    }


def extract_keywords_freq(messages: List[str], top_n: int = 5) -> List[str]:
    text = " ".join(messages).lower()
    words = word_tokenize(text)
    words = [re.sub(r'\W+', '', w) for w in words]
    words = [w for w in words if w.isalpha()]
    words = [w for w in words if w not in stopwords.words('english')]
    frequency = Counter(words)
    return [word for word, _ in frequency.most_common(top_n)]


def extract_keywords_tfidf(messages: List[str], top_n: int = 5) -> List[str]:
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([" ".join(messages)])
    feature_array = vectorizer.get_feature_names_out()
    scores = tfidf_matrix.toarray().flatten()

    top_indices = scores.argsort()[::-1][:top_n]
    return [feature_array[i] for i in top_indices]
