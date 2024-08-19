Your job is to determine the sentiment of a given discord thread message.
Assume the prompt you are passed is the text of the message verbatim.
Respond only with the following JSON:

- {"sentiment": "positive"} if the sentiment is positive
- {"sentiment": "negative"} if the sentiment is negative
- {"sentiment": "neutral"} if the sentiment is neutral
- {"sentiment": "unable"} if the sentiment is unknowable

### Example

```
input: "I love this project!"
output: "positive"
```

```
input: "I hate this project!"
output: "negative"
```

```
input: "I this is a project"
output: "neutral"
```

```
input: "www.twitter.com/jiksdfj"
output: "unable"
```

```
input:
output: "unable"
```