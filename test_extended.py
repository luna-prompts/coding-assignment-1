
import agent_task as at

def test_summary_nonempty():
    assert at.generate_summary("Hello world") != ""

def test_summary_stability():
    txt = "ChatGPT can draft emails, write code, and explain concepts."
    s1 = at.generate_summary(txt, max_tokens=12)
    s2 = at.generate_summary(txt, max_tokens=12)
    assert s1 == s2  # determinism (allow seeding or caching)

def test_sentiment_neutral():
    assert at.classify_sentiment(["The sky is blue."]) == ["neutral"]

def test_sentiment_mixed_batch():
    data = ["Great job!", "Terrible outcome.", "Meh"]
    expected = ["positive", "negative", "neutral"]
    assert at.classify_sentiment(data) == expected


