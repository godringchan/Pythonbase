import re


def func1():
    '''判断输入的内容是否可以作为一个变量'''
    input_name = input("输入一个变量:")

    name_ruler = r"[a-zA-Z_]\w*"

    name_match = re.match(name_ruler, input_name)

    try:
        print(f"{name_match.group()}可以作为一个变量名字")
    except Exception as e:
        print(f"{input_name}不能作为变量名")


def func2():
    '''判断输入的密码是否合法,需要有大小写字母,数字组成8-20位'''
    sn = input("请输入你的密码:")
    sn_ruler = r"[0-9a-zA-Z]{8,20}"
    # sn_match = re.match(sn_ruler, sn)
    sn_search = re.search(sn_ruler, sn)
    # print(sn_match)
    sn_long = len(sn)
    if sn_long < 8 or sn_long > 20:
        print("密码长度不正确")
    else:
        if sn_search.group() == sn:
            if re.match(r".*[0-9]+", sn):
                # print(re.match(r".*[0-9]+", sn))
                if re.match(r".*[a-z]+", sn):
                    # print(re.match(r".*[a-z]+", sn))
                    if not re.match(r".*[A-Z]+", sn):
                        print("密码需要大写字母")
                    else:
                        print("密码合法,可以使用")
                else:
                    print("密码中需要包含小写字母")
            else:
                print("密码中需要含有最少一个数字")
        else:
            print("密码含有非法,不能使用")
    # print(sn_match.group())


if __name__ == "__main__":
    func2()