# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: .venv
#     language: python
#     name: python3
# ---

# %%
import json
from pathlib import Path

import polars as pl

# %%
data = json.loads(Path("output.json").read_text())

# %%
(df := pl.DataFrame(data["messages"]))

# %%
(df := df.with_columns(pl.col("created_at").str.to_datetime()))

# %%
(df := df.with_columns(hour=pl.col("created_at").dt.hour()))

# %%
import seaborn.objects as so

# %%
so.Plot(df, x="author").add(so.Bar(), so.Hist())

# %%
so.Plot(df, x="hour").add(so.Bar(), so.Hist(discrete=True))

# %%
from discord_analysis.sentiment import classify_sentiment

# %%
system_prompt = Path("prompt.md").read_text()

# %%
sentiments = [classify_sentiment(m, system_prompt) for m in df.get_column("content")]

# %%
sentiments

# %%
df.get_column("content")

# %%
