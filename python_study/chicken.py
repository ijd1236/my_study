age = 19
money = 20000
chicken = 20000
beer = 10000
drink = 5000
# if money >= chicken + beer + drink and age >= 20:
#     print("치킨과 맥주와 음료수를 먹는다")
# elif money >= chicken + beer and age>= 29:
#     print("치킨과 맥주와 음료수를 먹는다")
# elif money >= chicken + drink:
#     print("치킨과 음료수를 먹는다")
# elif money >= chicken:
#     print("치킨을 먹는다")

if money >= chicken + beer + drink and age >= 20:
    print("치킨, 맥주, 음료수 먹는다")
elif money >= chicken + beer and age >= 20:
    print("치킨, 맥주 먹는다")
elif money >= chicken + drink:
    print("치킨, 음료수 먹는다")
elif money >= chicken:
    print("치킨먹는다")
elif money >= beer + drink and age >= 20:
    print("맥주와 음료수를 먹는다")
elif money >= beer and age >= 20:
    print("맥주 먹는다")
elif money >= drink:
    print("음료수 먹는다")
