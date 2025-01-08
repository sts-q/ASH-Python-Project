from database import Database

db = Database("temp_dataset.json")
# print(db.fetch_word(1))
# db.update_score(1, 1)
# print(db.fetch_word(1))
# print(db.fetch_all())
# print(db.fetch_sorted())
# print(db.fetch_reverse_sorted(limit=5))
# db.save()
print(db.fetch_random(3))