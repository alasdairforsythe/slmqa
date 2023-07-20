# slmqa

slmqa is a simple question-answer evaluation benchmark for small language models. It includes a dataset of 909 general knowledge question-answer pairs. The QA pairs were generated with gpt-3.5-turbo, stripped of duplicates and answers shorter than 5 characters, and cleaned by hand.

The score is the percentage of correct answers.

### Sample

```json
{
        "question": "What is the name of the highest mountain in the world?",
        "answer": "everest"
},
{
        "question": "What is the name of the famous Austrian composer who wrote the Ninth Symphony?",
        "answer": "beethoven"
},
{
        "question": "Which country is the largest by area?",
        "answer": "russia"
},
```

### Example Usage

```python
import slmqa

bench = slmqa.Benchmark("slmqa.json")
questions_list = bench.questions()

for question_index, question_string in enumerate(questions_list):
  # answer_string = generate_answer_from_your_model(question_string)
  bench.submit_answer(question_index, answer_string)

score = bench.score()
```

### Example Usage with TokenMonster (batch tokenize)

```python
import slmqa
import tokenmonster

vocab = tokenmonster.Load("your-vocab")
bench = slmqa.Benchmark("slmqa.json")

tokens_list = vocab.tokenize(bench.questions())

for question_index, question_tokens in enumerate(tokens_list):
  # answer_tokens = generate_answer_from_your_model(question_tokens)
  answer_string = vocab.decode(answer_tokens)
  bench.submit_answer(question_index, answer_string)

score = bench.score()
```
