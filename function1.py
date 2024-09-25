# arbitary arguments

def arb_func(*args):
  print(f"age is {args[0]}, name is {args[1]}")

age = 28
name = "Juhyeon"

arb_func(age, name)


# keyword arguments
def key_func(**kwargs):
  print(f"age is {kwargs["age"]}, name is {kwargs["name"]}")

key_func(age = 28, name = "sonjuhyeon")