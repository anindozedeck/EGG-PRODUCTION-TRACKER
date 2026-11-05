# pip install flask-cors
from collections import Counter
import math
import re

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable cross-origin requests in development

# For production, restrict to your frontend domain only:
# CORS(app, origins=["https://yoursite.com"])

STOP_WORDS = {
    "a", "an", "and", "are", "as", "at", "be", "been", "by", "for",
    "from", "has", "have", "in", "is", "it", "its", "of", "on", "or",
    "that", "the", "their", "this", "to", "was", "were", "will", "with",
}


def summarize_text(text):
    """Return an extractive summary containing the most relevant sentences."""
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    sentences = [sentence for sentence in sentences if sentence]
    if len(sentences) <= 3:
        return " ".join(sentences)

    words_by_sentence = [
        re.findall(r"\b[a-zA-Z0-9']+\b", sentence.lower())
        for sentence in sentences
    ]
    word_frequencies = Counter(
        word
        for words in words_by_sentence
        for word in words
        if word not in STOP_WORDS and len(word) > 2
    )
    if not word_frequencies:
        return " ".join(sentences[:3])

    sentence_scores = []
    for index, words in enumerate(words_by_sentence):
        keywords = [word for word in words if word in word_frequencies]
        score = sum(word_frequencies[word] for word in keywords) / math.sqrt(
            max(len(words), 1)
        )
        sentence_scores.append((score, index))

    summary_count = max(1, math.ceil(len(sentences) * 0.3))
    selected_indices = {
        index
        for _, index in sorted(sentence_scores, reverse=True)[:summary_count]
    }
    return " ".join(
        sentence
        for index, sentence in enumerate(sentences)
        if index in selected_indices
    )


@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json(silent=True)
    if not isinstance(data, dict) or not isinstance(data.get("text", ""), str):
        return jsonify({"error": "Request must contain a string 'text' field."}), 400

    text = data.get("text", "")
    result = summarize_text(text)
    return jsonify({"summary": result})


if __name__ == "__main__":
    app.run(port=5000, debug=True)