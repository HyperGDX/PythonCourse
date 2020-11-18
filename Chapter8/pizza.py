def make_pizza(*toppings):      #用*收集位置实参，构建空元组
    for topping in toppings:
        print(topping)