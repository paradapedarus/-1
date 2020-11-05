cont= int(input('скок хотите:'))
listnubers = []
for i in range(cont):
      i+=1
      el=int(input('please enter the Value {0} of el:'.format(i)))
      if el !=0:
            if el %2 ==0:
                  listnubers.append(el)
print(listnubers)


