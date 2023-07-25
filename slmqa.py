import json

class Benchmark:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.data = json.load(f)
        self.score = 0
        self.total = 0

    def questions(self):
        return [item['question'] for item in self.data]

    def submit_answer(self, idx, answer):
        answer = answer.lower()
        correct_answer = self.data[idx]['answer']
        self.total += 1
        if correct_answer in answer:
            self.score += 1
            return True
        return False

    def score(self):
        if self.total == 0:
            return 0
        return (self.score * 100) / self.total
