my_list = ["a", "b", "c", "d", "e", "f", "g"]
my_tuple = ("a", "b", "c", "d")
my_set ={"a", "b", "c", "d"}

for x in my_list:
  if x == "b":
    # break # 반복문을 해당 조건에서 중단한다.
    # continue # 반복문이 해당 조건을 넘어간다.
    pass
  # print(x)

for x in range(3, 10, 2): # range(시작, 끝, 증가값)
  print(x)
else:
  print("Done")

for i in range(2, 10):
  print(f"---- {i}단 ----")
  for j in range(1, 10):
    print(f"{i} X {j} = {i * j}")
  