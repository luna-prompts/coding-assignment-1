"""
Gen-AI Mini-Challenge -- SOLUTION (OpenAI New SDK style)
"""

import os
from openai import OpenAI
from typing import List

client = OpenAI(
    api_key="")


_POSITIVE = {"love", "great", "good", "awesome", "fantastic", "amazing", "happy"}
_NEGATIVE = {"hate", "bad", "terrible", "awful", "horrible", "sad", "angry"}


def generate_summary(text: str, max_tokens: int = 50) -> str:
    """
    Use OpenAI chat model to summarize text within max_tokens limit.
    """
    if not text.strip():
        return ""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes text."},
            {"role": "user", "content": f"Summarize the following text in under {max_tokens} tokens:\n\n{text}"}
        ],
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content.strip()


def classify_sentiment(texts: List[str]) -> List[str]:
    """
    Simple keyword matching sentiment classifier.
    """
    results = []
    for text in texts:
        text_lower = text.lower()
        has_pos = any(word in text_lower for word in _POSITIVE)
        has_neg = any(word in text_lower for word in _NEGATIVE)

        if has_pos and not has_neg:
            results.append("positive")
        elif has_neg and not has_pos:
            results.append("negative")
        else:
            results.append("neutral")
    return results


if __name__ == "__main__":
    print(generate_summary("OpenAI builds AI models."))
    print(classify_sentiment(["I love AI", "I hate bugs", "The sky is blue."]))
