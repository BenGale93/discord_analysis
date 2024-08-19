import typing as t

import ollama
from pydantic import BaseModel


class Sentiment(BaseModel):
    sentiment: t.Literal["positive", "negative", "neutral", "unable"]


def classify_sentiment(text: str, system_prompt: str) -> Sentiment:
    response = ollama.generate(
        model="llama3.1:8b", prompt=text, system=system_prompt, format="json"
    )
    resp = response["response"]
    if resp == "":
        return Sentiment(sentiment="unable")
    return Sentiment.model_validate_json(resp)
