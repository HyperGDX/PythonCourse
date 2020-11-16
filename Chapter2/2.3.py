message_1 = "Hello world!"
print(message_1)

message_2 = 'This is a "string".'
print(message_2)

print(message_2.title())  #title 首字母大写
print(message_2.upper())  #title 字母大写
print(message_2.lower())  #title 字母小写

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"  #在字符串中引用变量
print(full_name)
print(f"Hello, {first_name} {last_name}")
print("{} {}".format(first_name, last_name))  #老方法

print("\t\tpython\t\t")  #/t制表符
print("Languages:\nPython\nC\nJava")  #/n换行

message_3 = "88888python88888"
print(message_3.rstrip("8"))
print(message_3.lstrip("8"))
print(message_3.strip("8"))

message_4 = "this is string example....wow!!!"
print(message_4.rsplit())

message_5 = r"it's \n my book."
print(message_5)

message_6 = "\t\t\t\tsdfkljsdlkf\t\t\t\t"
print(message_6.strip())






