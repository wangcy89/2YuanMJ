# encoding:utf-8
while 1 == 1:
    jiesuan = int(input("输入结算方式（1.单人结算 2.双人结算）："))
    gtf = "给他发："
    gwf = "给我发："
    if jiesuan == 1:
        qian = int(input("请输入钱数（正数为赢，负数为输）："))
        if qian > 0:
            d_jgz = qian * 2 - 5
            if d_jgz > 0:
                print(gtf + str(d_jgz))
            else:
                print(gwf + str(-d_jgz))
        else:
            d_jgf = -qian * 2 + 5
            print(gwf + str(d_jgf))
    elif jiesuan == 2:
        d1 = int(input("请输入第一个人的数："))
        d2 = int(input("请输入第二个人的数："))
        zs = d1 + d2
        if zs > 0:
            s_jgz = zs * 2 - 10
            if s_jgz > 0:
                print(gtf + str(s_jgz))
            else:
                print(gwf + str(-s_jgz))
        else:
            s_jgf = -zs * 2 + 10
            print(gwf + str(s_jgf))
    else:
        print('输入错误')
