# -*- coding: utf-8 -

from sys import argv
#   to get the argv feature(modules or libraries) from that sys package.
#從sys包中引入功能模塊argv

script, filename = argv
#從argv中unpack兩個變量名values

print "Type the filename:",
txt_name = raw_input("> ")
#在filename:"後面加上, 展示時就不會換行 
#so 也可以這樣寫 print "Type the filename:" txt_name = raw_input("> ")

txt = open(txt_name)
#txt = open(filename) 直接打開filename
#定義variable變量 txt為 open()打開檔案

print "Here's your file %r:" % filename
print txt.read()
print txt.close()
#展示這是你的檔案名稱
#展示 執行txt本身的read命令
#執行關閉檔案 Terminal會展示None


print "Type the filename again:"
file_again = raw_input("> ")
#展示在輸入一次檔案名稱
#定義file_again 等於raw_input()可輸入並展示> 

txt_again = open(file_again)
#定義txt_again 等於 open()讀取檔案名file_again
#txt_again = open(filename)

print txt_again.read()
print txt_again.close()
#展示並執行txt_again本身的read命令

#筆記
#不只能讀取ex15_sample.txt 也能讀取ex14.py ex3.py...etc

#以下是在Terminal執行讀取檔案的指令
#>>> txtname = "ex15_sample.txt"
#>>> txt = open(txtname)
#>>> print txt.read()