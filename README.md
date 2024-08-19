# discord_analysis

This library includes tools to analyse Discord thread messages.

## Pre-requisites

You will need `pdm` to install Python dependencies.

You wil need to follow [Run an AI Large Language Model (LLM) at home on your
GPU](https://www.youtube.com/watch?v=RejIVgfER-4&t=1s) and have a suitable GPU
to perform sentiment analysis.

## Setup

Clone the repository and run `pdm install` to install the Python dependencies.
Setting up the local LLM.

## Data extraction

To extract the Discord thread data, you with need to setup a Discord bot will
the "intent" to read messages.

For more on setting up a Discord bot [Building your first Discord
app](https://discord.com/developers/docs/quick-start/getting-started)

Then setup a `.env` file will the following keys:

```
APP_ID=
DISCORD_TOKEN=
PUBLIC_KEY=
GUILD_ID=
CHANNEL_ID=
THREAD_ID=
OUTPUT_PATH=
```

You can then run the data extraction using `python -m discord_analysis`

A nicer CLI interface is a todo.

## Analysis

Basic analysis is present in `notebooks/analysis.ipynb`. It starts with some
data prep, then moves onto charting, then finishes with sentiment analysis
using a local llm.