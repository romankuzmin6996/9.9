list = []
n = int(input("Cik atzīmes  viņa saņema?"))
for i in range(n):
  ele = int(input())
  list.append(ele)
list1=sum(list)/len(list)
print(list1)