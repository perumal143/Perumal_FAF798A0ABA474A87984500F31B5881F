def isLeapyear(year):
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    return True
  else:
    return False
    year = 2012


year = (int(input("Enter a year:")))
if isLeapyear(year):
  print('{} is not a Leapyear'.format(year))
