pay = int(input())

fivehundred = (1000-pay)//500
hundred = (1000-pay-(fivehundred*500))//100
fifty = (1000-pay-(fivehundred*500)-(hundred*100))//50
ten = (1000-pay-(fivehundred*500)-(hundred*100)-(fifty*50))//10
five = (1000-pay-(fivehundred*500)-(hundred*100)-(fifty*50)-(ten*10))//5
one = (1000-pay-(fivehundred*500)-(hundred*100)-(fifty*50)-(ten*10)-(five*5))%10

s = str()

if(fivehundred > 0):
	s += "500, "+ str(fivehundred) +"; "
if(hundred > 0):
	s += "100, "+ str(hundred) +"; "
if(fifty > 0):
	s += "50, "+ str(fifty) +"; "
if(ten > 0):
	s += "10, "+ str(ten) +"; "
if(five > 0):
	s += "5, "+ str(five) +"; "
if(one > 0):
	s += "1, "+ str(one) +"; "

print(s.rstrip('; '))  #刪掉最後的;號