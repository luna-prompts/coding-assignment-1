import agent_task as at

def test_summary_length():
    text = "OpenAI builds artificial-intelligence models."
    max_tokens = 10
    summary = at.generate_summary(text, max_tokens=max_tokens)
    assert len(summary.split()) <= max_tokens, f"FAILED: Summary too long.\nInput: {text}\nSummary: {summary}"

def test_sentiment_simple():
    texts = ["I love AI", "I hate bugs"]
    expected = ["positive", "negative"]
    output = at.classify_sentiment(texts)
    assert output == expected, f"FAILED: Wrong sentiment classification.\nInput: {texts}\nExpected: {expected}\nGot: {output}"
