import json

# json.dumps() - преобразует объект в формате json
# json.dump() -- преобразует объект в формате json и записывает в файл
#
# json.loads() - преобразует json-строку в питоновский объект
# json.load() -- преобразует json-файл в питоновский объект

# json_file = """
#     {
#         "key1": 1,
#         "key2": 2
#     }
# """
#
# json_file1 = json.loads(json_file)
# print(type(json_file1))

# dct = {
#     "name": "Julia",
#     "occupation": "AQA",
#     "age": 20
# }
#
# json_file = json.dumps(dct)
# print(type(dct))
# print(dct)
# print("********************************************")
# print(type(json_file))
# print(json_file)

file_name = "json.json"
# with open(file_name, "w") as f:
#     json.dump(dct, f)

with open(file_name, 'r') as f:
    a = json.load(f)
# print(a)
# print(type(a))
for key, value in a.items():
    print(key, value)