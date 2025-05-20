from collections import Counter

def count_letters(text):
    text = text.lower()
    return dict(Counter(char for char in text if char.isalpha()))

text = "Programming is fun!"
result = count_letters(text)
print(result)
''''''

from collections import defaultdict

student_groups = defaultdict(list)
students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]
for collections, name in students: student_groups[collections].append(name)
print({k: v for k, v in student_groups.items()})