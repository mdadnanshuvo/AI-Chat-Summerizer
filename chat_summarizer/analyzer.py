import re
from collections import Counter
from typing import Dict, List, Tuple

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

# Download required NLTK data
nltk.download("punkt")
nltk.download("stopwords")


def get_message_counts(user_msgs: List[str], ai_msgs: List[str]) -> Dict[str, int]:
    """
     Returns a dictionary containing counts of total, user, and AI messages.

    Args:
        user_msgs: List of user message strings.
        ai_msgs: List of AI message strings.

    Returns:
        Dictionary with total, user, and AI message counts.
    """
    return {
        "total_messages": len(user_msgs) + len(ai_msgs),
        "user_messages": len(user_msgs),
        "ai_messages": len(ai_msgs),
    }


def extract_keywords_freq(messages: List[str], top_n: int = 5) -> List[str]:
    """
    Extracts top N frequent keywords from a list of messages using simple word frequency.

    Args:
        messages: List of text messages.
        top_n: Number of top keywords to return.

    Returns:
        List of top N keywords based on frequency.
    """
    text = " ".join(messages).lower()
    words = word_tokenize(text)
    words = [re.sub(r"\W+", "", w) for w in words]
    words = [w for w in words if w.isalpha()]
    words = [w for w in words if w not in stopwords.words("english")]
    frequency = Counter(words)
    return [word for word, _ in frequency.most_common(top_n)]


def extract_keywords_tfidf(messages: List[str], top_n: int = 5) -> List[str]:
    """
    Extracts top N keywords using TF-IDF scoring from a list of messages.

    Args:
        messages: List of text messages.
        top_n: Number of top keywords to return.

    Returns:
        List of top N keywords based on TF-IDF scores.
    """
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform([" ".join(messages)])
    feature_array = vectorizer.get_feature_names_out()
    scores = tfidf_matrix.toarray().flatten()

    top_indices = scores.argsort()[::-1][:top_n]
    return [feature_array[i] for i in top_indices]
