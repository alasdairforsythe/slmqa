import json

class Benchmark:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.data = json.load(f)
        self._score = 0
        self._total = 0

    def questions(self):
        return [item['question'] for item in self.data]

    def submit_answer(self, idx, answer):
        answer = answer.lower()
        correct_answer = self.data[idx]['answer']
        self._total += 1
        if correct_answer in answer:
            self._score += 1
            return True
        return False

    def score(self):
        if self._total == 0:
            return 0
        return (self._score * 100) / self._total
