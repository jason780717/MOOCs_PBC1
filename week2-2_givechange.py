pay = int(input())

fivehundred=(1000-pay)//500
hundred=(1000-pay-(fivehundred*500))//100
fifty=(1000-pay-(fivehundred*500)-(hundred*100))//50
ten=(1000-pay-(fivehundred*500)-(hundred*100)-(fifty*50))//10
five=(1000-pay-(fivehundred*500)-(hundred*100)-(fifty*50)-(ten*10))//5
one=(1000-pay-(fivehundred*500)-(hundred*100)-(fifty*50)-(ten*10)-(five*5))%10

print(fivehundred,hundred,fifty,ten,five,one)