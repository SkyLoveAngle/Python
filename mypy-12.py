#测试多分支选择结构

score = int (input ("请输入你的分数："))
grade =""

if score <60:
    grade = "不及格"
elif score<80:
    grade ="及格"
elif score <90:
    grade ="良好"
elif score<=100:
    grade ="优秀"

print("分数是{0}，等级是{1}".format(score,grade))