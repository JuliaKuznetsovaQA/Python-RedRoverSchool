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
    # result = set()
    # for line in file:
    #     word = file.readline().upper()
    #     c = word[-2:]
    #     if c == 'ЕЯ':
    #         print(word)
    #     else:
    #         continue
    # res = sorted(words)
    # print(result)
    lst = set()
    for word in file:
        a = word.strip().split()
        for i in a:
            c = i[-2:]
            if c.upper() == 'ЕЯ':
                lst.add(i.upper())
    for i in sorted(lst, key=lambda x: (len(x), x)):
        print(i)

