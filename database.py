import json
# import random
class Database:
    def __init__(self, filename):
        self.filename = filename
        self.data = None
        self.load()
    
    def load(self):
        try:
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
        except Exception as e:
            print(e)
    
    def save(self):
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.data, file)
        except Exception as e:
            print(e)
    
    def add_word(self, German, English):
        if self.data:
            self.data.append({
                "id": len(self.data),
                "German": German,
                "English": English,
                "score": 0
            })
        else:
            raise Exception("Data is empty")
    def remove_word(self, word_id):
        if self.data:
            for word in self.data:
                if word['id'] == word_id:
                    self.data.remove(word)
                    break
        else:
            raise Exception("Data is empty")
        

    def fetch_word(self, word_id):
        if self.data:
            for word in self.data:
                if word['id'] == word_id:
                    return word
        else:
            raise Exception("Data is empty")
        

    def update_score(self, word_id, score):
        if self.data:
            for word in self.data:
                if word['id'] == word_id:
                    word['score'] = score
                    break
        else:
            raise Exception("Data is empty")
    
    def fetch_all(self):
        if self.data:
            return self.data
        else:
            raise Exception("Data is empty")
    
    def fetch_sorted(self):
        if self.data:
            return sorted(self.data, key=lambda x: x['score'])[::-1]
        else:
            raise Exception("Data is empty")