def ticket(table, type, dish):
    answer = 'T' + table + ' '
    if(type=='a'):
        answer = answer + 'APP '+ dish
    elif(type=='m'):
        answer = answer + 'MAIN '+ dish
        if len(dish) > 10:
            answer = answer + ' 15 min'
        else:
            answer = answer + ' 8 min'
    elif(type=='d'):
        answer = answer + 'DES' + dish + ' BIRTHDAY'
    elif(type=='f'):
        result = result + 'OTF' + dish.upper()
    return result
      

def process(order):
    split1 - order.split('*')
    table = split1[0]
    split2 = split1[1].split('-')
    dishType = split2[0]
    dishName = split2[1]
    answer = ticket(table, dishType, dishName)
    print(answer)
    return

orders = []
print("HELLO WONDERFUL MARIA'S KITCHEN WAIT STAFF")
print('Enter orders one at a time or type x to quit')

while 1:
  order = input('Order: ')
  if order=='x':
      break
  orders.append(order)

for order in orders:
    process(order)
print()
print("Hey TA, what is Peter Pan's favorite restaurant? Wendy's! :D")