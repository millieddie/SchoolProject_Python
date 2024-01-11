import math

def bmi(weight,height):
  return weight / height / height

weight = float(input("体重を入力してください。（例）50kgの場合は『50』と入力>>"))
height = float(input("あなたの身長を入力してください。（例）161cmの場合は『1.61』と入力>>"))

result = math.floor((bmi(weight, height)) * 10) / 10
print("あなたのBMI指数は"+str(result)+"です")
