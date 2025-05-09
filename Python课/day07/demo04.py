name1 = ["张三","李四","王五","赵六"]
name2 = name1.copy()
print(name1)
print(name2)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
name1 = ["张三","李四","王五","赵六"]
name2 = name1.copy()
name1[1] = "陈七"
print(name1)
print(name2)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
name1 = [["张三","李四"],"王五","赵六"]
name2 = name1.copy()
name1[0][0] = "陈七"
print(name1)
print(name2)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

import copy
name1 = [["张三","李四"],"王五","赵六"]
name2 = copy.deepcopy(name1)
name1[0][0]="陈七"
print(name1)
print(name2)




