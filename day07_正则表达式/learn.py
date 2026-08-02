import re
# match 从头开始匹配
# s = 'suo zi xuan zuo zi xuan '
# s1 = 'lsuo zi xuan zuo zi xuan '
# result = re. match('suo',s)
# result1 = re. match('suo',s1)
# print(result1)
# print(result1.group())
# print(result1.span())

# s = 'suo zi xuan zuo zi xuan '
# result = re.search('zi', s)
# print(result)
#
# result1 = re.findall('xu', s)
# print(result1)

# s = 'itheimal@@python2!!666##itcast3'
# num = re.findall(r'\d',s) # 字符串前面带上r的标记，表示字符串中转义字符无效，就是普通字符的意思
# print(num)
# dyte = re.findall(r'\D',s)
# print(dyte)
# words = re.findall(r'\w',s)
# print(words)
# empty = re.findall(r'',s)
# print(empty)
# no_words = re.findall(r'\W',s)
# print(no_words)
# eglish = re.findall(r'[a-zA-Z]',s)
# print(eglish)
# num1 = re.findall(r'[0-9]',s)
# print(num1)


# 案例练习
# 匹配账号，只能由数字和字母组成，长度限制到6-10
r = r'^[0-9a-zA-Z]{6,10}$'
s = '1234567AB'
print(re.findall(r, s))
# 匹配QQ号，要求纯数字，长度5-11，第一位不为0
r = r'^[1-9]\d{4,10}$'
s = '736874'
print(re.findall(r, s))
# 匹配邮箱地址，只允许QQ、163、Gmail这三种邮箱格式
# {内容}. {内容}. {内容}@{内容}. {内容}. {内容}
r = r'(^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+$)'
s = '767315448@qq.com'
print(re.findall(r,s))