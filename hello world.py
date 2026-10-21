from os import name

print("Hello, World!dsgdgdddshsajhd")
name = "小明"
age = 21
height = 1.8
is_student = True
if age >= 18:
    print("你是一个成年人")
else:
    print("你是一个未成年人")
    # //列表与循环
    fruits = ["苹果", "香蕉", "橙子"]
    for fruit in fruits:
        print(f"我喜欢吃{fruit}")

        person = {"name": "小明", "age": 21}
        print(person["name"])


        # 函数
        def shuanshu(length, width):
            """
            计算矩形的面积
            """
            area = length * width
            return

            # 调用函数


        order_no = "1234567890"
        time_str = "2023-08-01 10:00:00"

        # 定义商品列表
        item = [
            {"name": "苹果", "price": 10, "num": 2},
            {"name": "shdgg", "price": 20, "num": 1},
            {"name": "橙子", "price": 6, "num": 1}
        ]
        # 计算总数量和总金额
        total_num = sum(item["price"] for item in item)
        total_amount = sum(item["price"] for item in item)

        # 定义分割线
        separator = "-----------------" * 3
        # 打印小票

        print(separator)
        print(f"订单号：{order_no}")
        print(f"时间：{time_str}")

        print(separator)
        print(f"单号： {order_no}")
        print(f"时间：{time_str}")
        for item in item:
            # 计算单行金额
            row_amount = item["qty"] * item["price"]
            # 注意：中文字符在终端占用的宽度通常比英文字符大，这里设置固定宽度尽量对齐
            print(f"{item['name']:<12} {item['qty']:>4} {item['price']:>8.2f} {row_amount:>8.2f}")

        print(separator)
        # 打印底部结算信息
        print(f"总数: {total_num:<20} 总额: {total_amount:.2f}")
        print(f"折后总额: {total_amount:.2f}")
        print(f"实收: {total_amount:.2f}{'找零:':>12} 0.00")
        print("收银: 管理员")
        print(separator)

