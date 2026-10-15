d = {}

old = input("Enter word to replace: ")
new = input("Enter new word: ")

d[old] = new

sentence = input("Enter a sentence: ")

words = sentence.split()

for i in range(len(words)):
    if words[i] in d:
        words[i] = d[words[i]]

result = " ".join(words)

print("Original Sentence:", sentence)
print("Modified Sentence:", result)