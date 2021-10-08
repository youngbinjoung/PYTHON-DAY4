#  1 ~ 10 까지 수 리스트 선언 
list1 = []

i = 0

while i < 10 :
  list1.append(i + 1)
  i += 1
  
list2 = [1,2,3,4,5,6,7,8,9,10]

# 리스트 값 짝수만 가져오기

i = 0

while i < len(list2) :

  if list1[i] % 2 == 0 :
    print(list1[i])

  i += 1


# 리스트에 11, 13, 15 추가하기

#list1 += [11, 13, 15]
list1.append(11)
list1.append(13)
list1.append(15)

print(list1)


# 리스트의 짝수번째 값 1증가시키기

i = 0

while i < len(list2) :

  if i % 2 != 0 :
    list1[i] += 1
  i += 1

print(list1)
