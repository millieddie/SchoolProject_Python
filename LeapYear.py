def is_leapyear(y) :
  return(y%400 == 0 or (y % 4 == 0 and y % 100 != 0))

current_year = int(input("今年は西暦何年ですか？(数字を入力)>>"))
if is_leapyear(current_year):
  print ("西暦{}年は、うるう年です".format(current_year))
else:
  print ("西暦{}年は、うるう年ではあリません".format(current_year))


month = int(input("今は何月ですか？(数字を入力)>>"))
if month < 13:
  if month in [1, 3, 5, 7, 8, 10, 12]:
    print("今月は31日まであリますね")
  else:
    if month != 2:
      print("今月は30日までですね")
    else:
      print("1年で一番寒い月ですね")
      #2月のこと
    print("年が明けてから")
    print("{}箇月が過ぎました。".format(month))
else:
    print("有効な数値ではありませんでした")
