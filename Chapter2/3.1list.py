message = "this is a string example. wow!"
print(message.rsplit())
#['this', 'is', 'a', 'string', 'example.', 'wow!']
#python中用 [] 表示列表

#访问列表元素
list_1 = message.rsplit()
print(list_1[0])  #输出元素不带方括号
print(list_1[0].upper())
print(list_1[-1])

message_1 = f"A {list_1[3].upper()} example"
print(message_1)

list_1[0] = "that"
print(list_1)

list_1.append("Amazing!")
print(list_1)

