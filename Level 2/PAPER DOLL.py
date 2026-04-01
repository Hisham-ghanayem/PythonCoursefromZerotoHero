
text = "Hello"
def paper_doll(text):
    results = ''
    for char in text:
        results += char*3
    return results
print(paper_doll(text))
