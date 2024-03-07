# file_name = "answer.txt"
# with open(file_name, "r", encoding="utf-8") as f:
#     content = [i.strip() for i in f.readlines()]
# for i in content:
#     print(i)
# file_name = 'goats.txt'
# file = open(file_name, "w", encoding="utf-8")
# file.write('Hello')
# file.close()

file_name = 'words.txt'
with open(file_name, 'r', encoding='utf-8') as file:
    lst = set()
    for word in file:
        if word.upper().strip()[-2:] == 'ЕЯ':
            lst.add(word.upper().strip())
    for i in sorted(lst, key=lambda x: (len(x), x)):
        print(i)

