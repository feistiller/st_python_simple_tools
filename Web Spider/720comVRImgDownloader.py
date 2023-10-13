# coding:utf8
import urllib2

# 你就改这个url就可以了，不同的图片就是之前的这部分url不同。
url="http://pano4.qncdn.720static.com/resource/prod/feci6585683/b3a2cwzgjcf/206332/imgs"
# 这个是那几个文件夹，方便起见我就直接让他们在这个脚本的目录里直接生成了，所以你要新建一个文件夹，之后运行这个脚本
word=["b","d","f","i","r","u"]

# 保存图片的方法，二进制写入
def savePic(name,picurl):
    print picurl;
    imgData = urllib2.urlopen(picurl).read()
    # 给定图片存放名称（文件的命名方式是（字母）+网页原名的方式）
    fileName = name + ".jpg"
    output = open(fileName, 'wb+')
    output.write(imgData)
    output.close()

#无尽的for循环(⊙﹏⊙)b
for m in range(0,len(word)):
    for i in range(1,4):
        if i ==1:
            picurl=url+"/"+word[m]+"/l1/1/l1_"+word[m]+"_1_1.jpg"
            name=word[m]+"l"+str(i)+"_b_1_1"
            savePic(name,picurl)
        else:
            for j in range(1,i+i-1):
                for n in range(1,i+i-1):
                    picurl=url+"/"+word[m]+"/l"+str(i)+"/"+str(j)+"/l"+str(i)+"_"+word[m]+"_"+str(j)+"_"+str(n)+".jpg"
                    name=word[m]+"l"+str(i)+"_"+str(j)+"_"+str(n)
                    savePic(name, picurl)


print "~\(≧▽≦)/~啦啦啦 \n"
print "运行完成"

