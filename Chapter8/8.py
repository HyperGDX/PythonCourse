def make_pizza(*toppings):      #用*收集位置实参，构建空元组
    for topping in toppings:
        print(topping)

make_pizza("pepperoni")
make_pizza("mushrooms","green peppers",'extra cheese')

def bulid_profile(first,last,**user_info):      #用**收集关键字实参，构建空字典
    user_info['first_name']=first
    user_info['last_name']=last
    return user_info

user_profile=bulid_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)
print('1')