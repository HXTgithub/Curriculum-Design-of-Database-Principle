#!/user/bin/env python3
# -*- coding: utf-8 -*-
import pymssql
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


# 主函数
def mainui():
    global mainwin
    mainwin = tk.Tk()
    mainwin.geometry("600x450")
    mainwin.resizable(0, 0)
    selectgoods()
    mainwin.mainloop()


def gchangeid2(e):
    global id2
    itm = tree2.set(tree2.focus())
    id2 = itm['会员卡号']
    print(id2)


def delmenber():
    if not tree2.set(tree2.focus()):
        msg = messagebox.showwarning(title="消息警告", message="请选择一位会员")
        print(msg)
        selectmenber()
        return
    sql = "delete from Menber where  Mnum='%s'" % id2
    con = pymssql.connect(host="127.0.0.1", port="1433", database="d1", user="sa", password="123", charset="cp936")
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    con.close()
    selectmenber()


def selectmenber():
    global tree2
    frame1 = tk.Frame(mainwin, bd=3, width=500, height=450, relief="groove")
    selectgbtn = tk.Button(mainwin, text="查看商品信息", command=selectgoods)
    addgbtn = tk.Button(mainwin, text="添加商品信息", command=addgoods)
    addmbtn = tk.Button(mainwin, text="添加会员信息", command=addmenber)
    pselectmbtn = tk.Button(mainwin, text="查看会员信息", relief="sunken")
    btn = tk.Button(frame1, text='删除', command=delmenber, relief="groove")
    sql1 = "select * from Menber"
    con = pymssql.connect(host="127.0.0.1", port="1433", database="d1", user="sa", password="123", charset="cp936")
    cursor = con.cursor()
    cursor.execute(sql1)
    cnt1 = cursor.fetchall()
    print(cnt1)
    tree2 = ttk.Treeview(frame1, height=16)
    tree2["selectmode"] = 'browse'
    tree2["show"] = 'headings'
    tree2["columns"] = ("会员卡号", "会员姓名", "会员电话", "注册日期", "充值金额")
    tree2.column("会员卡号", width=99)
    tree2.column("会员姓名", width=98)
    tree2.column("会员电话", width=98)
    tree2.column("注册日期", width=98)
    tree2.column("充值金额", width=99)
    tree2.heading("会员卡号", text="会员卡号")
    tree2.heading("会员姓名", text="会员姓名")
    tree2.heading("会员电话", text="会员电话")
    tree2.heading("注册日期", text="注册日期")
    tree2.heading("充值金额", text="充值金额")
    tree2.bind("<<TreeviewSelect>>", gchangeid2)
    index = 0
    for item in cnt1:
        tree2.insert("", index, values=(item[0], item[1], item[2], item[3], item[5]))
        index = index + 1
    tree2.place(x=0, y=45)
    selectgbtn.place(x=10, y=100)
    addgbtn.place(x=10, y=150)
    addmbtn.place(x=10, y=200)
    pselectmbtn.place(x=10, y=250)
    btn.place(x=200, y=400)
    frame1.place(x=100, y=0)


def add_huiyuan():
    # 连接数据库
    connect = pymssql.connect(server="localhost:1433", database='d1', user='sa', password='123', charset='utf8')
    cursor = connect.cursor()
    if cursor:
        print("连接成功!")
    # 创建光标
    cursor = connect.cursor()
    # 编写SQL语句
    sql = "insert into Menber(Mnum,Mname,Mphone,Mdate,Mcip,Mbalance) values('%s','%s','%s','%s','%s','%s')" % (
        e1.get(),
        e2.get(),
        e3.get(),
        e4.get(),
        e5.get(),
        e6.get())
    # 执行SQL语句，并且输出完成提示信息，否则回滚
    cursor.execute(sql)
    connect.commit()
    tk.messagebox.showinfo("提示", "数据添加成功！")
    # 关闭数据库连接，防止泄露
    connect.close()


# 增加会员选项
def addmenber():
    global e1, e2, e3, e4, e5, e6
    selectgbtn = tk.Button(mainwin, text="查看商品信息", command=selectgoods)
    addgbtn = tk.Button(mainwin, text="添加商品信息", command=addgoods)
    selectmbtn = tk.Button(mainwin, text="添加会员信息", relief="sunken")
    paddmbtn = tk.Button(mainwin, text="查看会员信息", command=selectmenber)
    frame1 = tk.Frame(mainwin, bd=3, width=500, height=450, relief="groove")
    l0 = tk.Label(frame1, text="会员注册系统", font=('Arial', 22), width=10, height=1)
    l0.place(x=150, y=25)
    l1 = tk.Label(frame1, text="会员卡号", font=('Arial', 12), width=8, height=1)
    l1.place(x=50, y=100)
    l2 = tk.Label(frame1, text="会员姓名", font=('Arial', 12), width=8, height=1)
    l2.place(x=50, y=150)
    l3 = tk.Label(frame1, text="会员电话", font=('Arial', 12), width=8, height=1)
    l3.place(x=50, y=200)
    l4 = tk.Label(frame1, text="注册日期", font=('Arial', 12), width=8, height=1)
    l4.place(x=50, y=250)
    l5 = tk.Label(frame1, text="会员密码", font=('Arial', 12), width=8, height=1)
    l5.place(x=50, y=300)
    l6 = tk.Label(frame1, text="充值金额", font=('Arial', 12), width=8, height=1)
    l6.place(x=50, y=350)
    e1 = tk.Entry(frame1, show=None, width=40)
    e1.place(x=150, y=100)
    e2 = tk.Entry(frame1, show=None, width=40)
    e2.place(x=150, y=150)
    e3 = tk.Entry(frame1, show=None, width=40)
    e3.place(x=150, y=200)
    e4 = tk.Entry(frame1, show=None, width=40)
    e4.place(x=150, y=250)
    e5 = tk.Entry(frame1, show=None, width=40)
    e5.place(x=150, y=300)
    e6 = tk.Entry(frame1, show=None, width=40)
    e6.place(x=150, y=350)
    # B1是添加按钮
    B1 = tk.Button(frame1, text="添加", font=('Arial', 12), width=8, height=1, command=add_huiyuan)
    B1.place(x=100, y=400)
    # B2是返回按钮
    B2 = tk.Button(frame1, text="返回", font=('Arial', 12), width=8, height=1)
    B2.place(x=270, y=400)
    # 窗口刷新
    frame1.place(x=100, y=0)
    selectgbtn.place(x=10, y=100)
    addgbtn.place(x=10, y=150)
    selectmbtn.place(x=10, y=200)
    paddmbtn.place(x=10, y=250)


# 添加商品操作
def addg():
    con = pymssql.connect(host="127.0.0.1", port="1433", database="d1", user="sa", password="123")
    cursor = con.cursor()
    sql = "insert into Goods (Gnum,Gname,Gtype,Gprice,Gbid,Vnum) values (%s,'%s','%s',%s,%s,'%s')" % \
          (idEntry.get(), nameEntry.get(), typeEntry.get(), priceEntry.get(), bidEntry.get(), vendorEntry.get())
    cursor.execute(sql)
    con.commit()
    con.close()


# 增加商品选项
def addgoods():
    global idEntry
    global nameEntry
    global typeEntry
    global priceEntry
    global bidEntry
    global vendorEntry
    selectgbtn = tk.Button(mainwin, text="查看商品信息", command=selectgoods)
    paddgbtn = tk.Button(mainwin, text="添加商品信息", relief="sunken", )
    addmbtn = tk.Button(mainwin, text="添加会员信息", command=addmenber)
    selectmbtn = tk.Button(mainwin, text="查看会员信息", command=selectmenber)
    frame1 = tk.Frame(mainwin, bd=3, width=500, height=450, relief="groove")
    idlabel = tk.Label(frame1, text="商品编号：")
    namelabel = tk.Label(frame1, text="商品名称：")
    typelabel = tk.Label(frame1, text="商品类别：")
    pricelabel = tk.Label(frame1, text="商品单价：")
    bidlabel = tk.Label(frame1, text="商品成本：")
    vendorlabel = tk.Label(frame1, text="供 应 商 ：")
    idEntry = tk.Entry(frame1, bd=2)
    nameEntry = tk.Entry(frame1, bd=2)
    typeEntry = tk.Entry(frame1, bd=2)
    priceEntry = tk.Entry(frame1, bd=2)
    bidEntry = tk.Entry(frame1, bd=2)
    vendorEntry = tk.Entry(frame1, bd=2)
    addbtn = tk.Button(frame1, text="添  加", width="10", command=addg)
    selectgbtn.place(x=10, y=100)
    paddgbtn.place(x=10, y=150)
    addmbtn.place(x=10, y=200)
    selectmbtn.place(x=10, y=250)
    idlabel.place(x=125, y=50)
    namelabel.place(x=125, y=90)
    typelabel.place(x=125, y=130)
    pricelabel.place(x=125, y=170)
    bidlabel.place(x=125, y=210)
    vendorlabel.place(x=125, y=250)
    idEntry.place(x=200, y=50)
    nameEntry.place(x=200, y=90)
    typeEntry.place(x=200, y=130)
    priceEntry.place(x=200, y=170)
    bidEntry.place(x=200, y=210)
    vendorEntry.place(x=200, y=250)
    addbtn.place(x=200, y=325)
    frame1.place(x=100, y=0)


# 获取选择的编号
def gchangeid(e):
    global id
    itm = tree.set(tree.focus())
    id = itm['商品编号']
    print(id)


# 修改操作
def modify():
    con = pymssql.connect(host="127.0.0.1", port="1433", database="d1", user="sa", password="123", charset="cp936")
    cursor = con.cursor()
    cursor.execute("select * from Vendor")
    temp = cursor.fetchall()
    stats = ''
    for item in temp:
        if item[1] == vendorEntry.get():
            stats = item[0]
    sql = "update Goods set Gname = '%s',Gtype = '%s', Gprice = %s,Gbid = %s, Vnum = %s where Gnum = %s " % \
          (nameEntry.get(), typeEntry.get(), priceEntry.get(), bidEntry.get(), stats, id)
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    con.close()
    msg = messagebox.showinfo(title="消息提示", message="修改成功")
    print(msg)
    selectgoods()


# 修改商品界面
def modgood():
    if not tree.set(tree.focus()):
        msg = messagebox.showwarning(title="消息警告", message="请选择一项商品")
        print(msg)
        selectgoods()
        return
    global nameEntry
    global typeEntry
    global priceEntry
    global bidEntry
    global vendorEntry
    print(tree.set(tree.focus()))
    frame1 = tk.Frame(mainwin, bd=3, width=500, height=450, relief="groove")
    namelabel = tk.Label(frame1, text="商品名称：")
    typelabel = tk.Label(frame1, text="商品类别：")
    pricelabel = tk.Label(frame1, text="商品单价：")
    bidlabel = tk.Label(frame1, text="商品成本：")
    vendorlabel = tk.Label(frame1, text="供 应 商 ：")
    nameEntry = tk.Entry(frame1, bd=2)
    typeEntry = tk.Entry(frame1, bd=2)
    priceEntry = tk.Entry(frame1, bd=2)
    bidEntry = tk.Entry(frame1, bd=2)
    vendorEntry = tk.Entry(frame1, bd=2)
    btn1 = tk.Button(frame1, text="修改", width="10", relief='groove', command=modify)
    btn2 = tk.Button(frame1, text="返回", width="10", relief='groove', command=selectgoods)
    namelabel.place(x=125, y=90)
    typelabel.place(x=125, y=130)
    pricelabel.place(x=125, y=170)
    bidlabel.place(x=125, y=210)
    vendorlabel.place(x=125, y=250)
    nameEntry.place(x=200, y=90)
    typeEntry.place(x=200, y=130)
    priceEntry.place(x=200, y=170)
    bidEntry.place(x=200, y=210)
    vendorEntry.place(x=200, y=250)
    btn1.place(x=125, y=325)
    btn2.place(x=275, y=325)
    frame1.place(x=100, y=0)


# 删除商品
def delgood():
    if not tree.set(tree.focus()):
        msg = messagebox.showwarning(title="消息警告", message="请选择一项商品")
        print(msg)
        selectgoods()
        return
    sql = "delete from Goods where  Gnum='%s'" % id
    con = pymssql.connect(host="127.0.0.1", port="1433", database="d1", user="sa", password="123", charset="cp936")
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    con.close()
    selectgoods()


# 按条件查询
def seltgood():
    stats = selentry.get()
    if combobox.get() == '商品编号':  # '查看全部', '商品编号', '商品名称', '商品类别', '商品单价', '商品成本', '供应商'
        sql1 = "select * from Goods where Gnum = %s" % stats
        sql2 = "select * from Vendor"
    else:
        if combobox.get() == '商品名称':
            sql1 = "select * from Goods where Gname = %s" % stats
            sql2 = "select * from Vendor"
        else:
            if combobox.get() == '商品类别':
                sql1 = "select * from Goods where Gtype = %s" % stats
                sql2 = "select * from Vendor"
            else:
                if combobox.get() == '商品单价':
                    sql1 = "select * from Goods where Gprice = %s" % stats
                    sql2 = "select * from Vendor"
                else:
                    if combobox.get() == '商品成本':
                        sql1 = "select * from Goods where Gbid = %s" % stats
                        sql2 = "select * from Vendor"
                    else:
                        if combobox.get() == '供应商':
                            con = pymssql.connect(host="127.0.0.1", port="1433", database="d1", user="sa",
                                                  password="123", charset="cp936")
                            cursor = con.cursor()
                            cursor.execute("select * from Vendor")
                            temp = cursor.fetchall()
                            for item in temp:
                                if item[1] == stats:
                                    stats = item[0]
                            con.close()
                            sql1 = "select * from Goods where Vnum = %s" % stats
                            sql2 = "select * from Vendor"
                        else:
                            sql1 = "select * from Goods"
                            sql2 = "select * from Vendor"
    con = pymssql.connect(host="127.0.0.1", port="1433", database="d1", user="sa", password="123", charset="cp936")
    cursor = con.cursor()
    cursor.execute(sql1)
    cnt1 = cursor.fetchall()
    cursor.execute(sql2)
    cnt2 = cursor.fetchall()
    con.close()
    cnt1 = list(cnt1)
    index = 0
    for item in cnt1:
        cnt1[index] = list(item)
        index = index + 1
    for item1 in cnt1:
        for item2 in cnt2:
            if item1[5] == item2[0]:
                item1[5] = item2[1]
                break
    print("商品查询结果：")
    print(cnt1)
    print("--------------")

    for child in tree.get_children():
        tree.delete(child)
    index = 0
    for item in cnt1:
        tree.insert("", index, values=(item[0], item[1],
                                       item[2], format(item[3], '.2f'), format(item[4], '.2f'), item[5]))
        index = index + 1


def takeFirst(elem):
    return int(elem[0])


# 查询修改删除商品选项
def selectgoods():
    global frame1
    global tree
    global combobox
    global selentry
    pselectgbtn = tk.Button(mainwin, text="查看商品信息", relief="sunken")
    addgbtn = tk.Button(mainwin, text="添加商品信息", command=addgoods)
    addmbtn = tk.Button(mainwin, text="添加会员信息", command=addmenber)
    selectmbtn = tk.Button(mainwin, text="查看会员信息", command=selectmenber)
    frame1 = tk.Frame(mainwin, bd=3, width=500, height=450, relief="groove")
    combobox = ttk.Combobox(frame1,
                            values=['查看全部', '商品编号', '商品名称', '商品类别', '商品单价', '商品成本', '供应商'],
                            width=10)
    lable1 = tk.Label(frame1, text='查询筛选：')
    lable2 = tk.Label(frame1, text='筛选条件：')
    btn1 = tk.Button(frame1, text='查询', command=seltgood, relief='groove')
    selentry = ttk.Entry(frame1)
    btn2 = tk.Button(frame1, text='删除', command=delgood, relief="groove")
    btn3 = tk.Button(frame1, text='修改', command=modgood, relief="groove")
    combobox.current(0)
    sql1 = "select * from Goods"
    sql2 = "select * from Vendor"
    con = pymssql.connect(host="127.0.0.1", port="1433", database="d1", user="sa", password="123", charset="cp936")
    cursor = con.cursor()
    cursor.execute(sql1)
    cnt1 = cursor.fetchall()
    cursor.execute(sql2)
    cnt2 = cursor.fetchall()
    cnt1 = list(cnt1)
    index = 0
    for item in cnt1:
        cnt1[index] = list(item)
        index = index + 1
    con.close()
    for item1 in cnt1:
        for item2 in cnt2:
            if item1[5] == item2[0]:
                item1[5] = item2[1]
                break
    print("商品查询结果：")
    print(cnt1)
    print("--------------")
    # 表结构建立
    tree = ttk.Treeview(frame1, height=16)
    tree["selectmode"] = 'browse'
    tree["show"] = 'headings'
    tree["columns"] = ("商品编号", "商品名称", "商品类别", "商品单价", "商品成本", "供应商")
    tree.column("商品编号", width=82)
    tree.column("商品名称", width=82)
    tree.column("商品类别", width=82)
    tree.column("商品单价", width=82)
    tree.column("商品成本", width=82)
    tree.column("供应商", width=82)
    tree.heading("商品编号", text="商品编号")
    tree.heading("商品名称", text="商品名称")
    tree.heading("商品类别", text="商品类别")
    tree.heading("商品单价", text="商品单价")
    tree.heading("商品成本", text="商品成本")
    tree.heading("供应商", text="供应商")
    tree.bind("<<TreeviewSelect>>", gchangeid)
    index = 0
    cnt1.sort(key=takeFirst)
    for item in cnt1:
        tree.insert("", index, values=(item[0], item[1],
                                       item[2], format(item[3], '.2f'), format(item[4], '.2f'), item[5]))
        index = index + 1
    pselectgbtn.place(x=10, y=100)
    addgbtn.place(x=10, y=150)
    addmbtn.place(x=10, y=200)
    selectmbtn.place(x=10, y=250)
    frame1.place(x=100, y=0)
    tree.place(x=0, y=45)
    combobox.place(x=75, y=10)
    lable1.place(x=0, y=10)
    lable2.place(x=200, y=10)
    selentry.place(x=275, y=10)
    btn1.place(x=425, y=6)
    btn2.place(x=100, y=400)
    btn3.place(x=300, y=400)


# 登录操作
def login():
    con = pymssql.connect(host="127.0.0.1", port="1433", database="d1", user="sa", password="123", charset="cp936")
    cursor = con.cursor()
    cursor.execute("select * from adminUsers")
    cnt = cursor.fetchone()
    print(luser.get() + lpassword.get())
    while cnt:
        print(cnt)
        if cnt[1] == luser.get() and cnt[2] == lpassword.get():
            con.close()
            loginwin.destroy()
            mainui()
            return
        cnt = cursor.fetchone()
    con.close()
    msg = messagebox.showwarning(title="消息警告", message="用户名或密码错误，请重新输入")
    print(msg)


# 注册界面的返回选项
def resreturnlogin():
    registerwin.destroy()
    loginui()


# 注册操作
def register():
    if 0 < len(ruser.get()) < 10 and 0 < len(rpassword.get()) < 20:
        con = pymssql.connect(host="127.0.0.1", port="1433", database="d1", user="sa", password="123", charset="UTF-8")
        cursor = con.cursor()
        print(ruser.get())
        sql = "insert into adminUsers (username,userpassword) values('%s','%s')" % (ruser.get(), rpassword.get())
        cursor.execute(sql)
        con.commit()
        con.close()
        msg = messagebox.showinfo(title="消息提示", message="注册成功，请登录")
        print(msg)
        registerwin.destroy()
        loginui()
    else:
        msg = messagebox.showwarning(title="消息警告", message="输入非法请重新输入")
        print(msg)


# 注册界面
def registerui():
    global registerwin
    global ruser
    global rpassword
    loginwin.destroy()
    registerwin = tk.Tk()

    registerwin.geometry("300x200")
    rlabel1 = tk.Label(registerwin, text="用户名:")
    rlabel2 = tk.Label(registerwin, text="密  码:")
    ruser = tk.Entry(registerwin)
    rpassword = tk.Entry(registerwin, show="*")
    resgisterbtn = tk.Button(registerwin, text="注册", command=register)
    backbtn = tk.Button(registerwin, text="返回", command=resreturnlogin)

    rlabel1.place(x=65, y=20)
    rlabel2.place(x=65, y=75)
    ruser.place(x=115, y=20)
    rpassword.place(x=115, y=75)
    resgisterbtn.place(x=85, y=125)
    backbtn.place(x=185, y=125)
    loginwin.mainloop()


# 登陆界面
def loginui():
    global loginwin
    global luser
    global lpassword
    loginwin = tk.Tk()
    loginwin.geometry("300x200")
    llabel1 = tk.Label(loginwin, text="用户名:")
    llabel2 = tk.Label(loginwin, text="密  码:")
    luser = tk.Entry(loginwin)
    lpassword = tk.Entry(loginwin, show="*")
    loginbtn = tk.Button(loginwin, text="登录", command=login)
    resgisterbtn = tk.Button(loginwin, text="注册", command=registerui)

    llabel1.place(x=65, y=20)
    llabel2.place(x=65, y=75)
    luser.place(x=115, y=20)
    lpassword.place(x=115, y=75)
    loginbtn.place(x=85, y=125)
    resgisterbtn.place(x=185, y=125)
    loginwin.mainloop()


if __name__ == '__main__':
    mainui()
