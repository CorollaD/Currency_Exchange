print("****欢迎使用货币转换服务系统****")
# 定义字典
service_menu = { 1:"人民币转换美元", 2:"美元转换人民币", 3:"人民币转换欧元",0:"结束程序",}
# 字典内容遍历输出
for k,v in service_menu.items():
    print(k,v)
# 获取用户选择
your_choice = int(input("请您选择需要的服务："))
# 进入人民币转换美元服务
if your_choice == 1:
    print("欢迎使用人民币转换美元服务")
    your_money = int(input("请输入您要兑换的人民币:"))
    print("您需要转换的人民币为:{}".format(your_money))
    RMB_to_US = your_money/6.72
    print("兑换成美元为:{:0,.2f}$".format(RMB_to_US, "0,.2f"))
# 进入美元转换人民币服务
elif your_choice == 2:
    print("欢迎使用美元转换人民币服务")
    your_money = int(input("请输入您要兑换的美元:"))
    print("您需要转换的人民币为:{}".format(your_money))
    US_to_RMB = float(your_money * 6.72)
    print("兑换成人民币为:{:0,.2f}￥".format(US_to_RMB, "0,.2f"))
# 进入人民币转换欧元服务
elif your_choice == 3:
    print("欢迎使用人民币转换欧元服务")
    your_money = int(input("请输入您要兑换的人民币:"))
    print("您需要转换的人民币为:{}".format(your_money))
    RMB_to_EUR = float(your_money * 0.13)
    print("兑换成欧元为:{:0,.2f}欧元".format(RMB_to_EUR, "0,.2f"))
# 退出循环
elif your_choice == 0:
    print("感谢您的使用，祝您生活愉快，再见！")
# 输入错误提醒
else:
    print("您输入的选择有误,请重新输入")
    

