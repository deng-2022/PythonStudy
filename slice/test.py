my_str = "万过薪月,员序程马黑来,nohtyP学"

temp = my_str[::-1]
temp = temp.replace(",", " ")
temp = temp.replace("来", "")

print(temp)
print(type(temp))
