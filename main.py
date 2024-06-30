def euclideanDistance(nokta1, nokta2):
  mesafe = ((nokta1[0]-nokta2[0])**2 + (nokta1[1]-nokta2[1])**2)**(1/2)
  return mesafe
list1 = [(1,2),(2,5),(9,12)]
mesafeler = []
for i in range(len(list1)):
  j=i+1
  while j<len(list1):
    mesafeler.append(euclideanDistance(list1[i],list1[j]))
    j+=1
print(min(mesafeler))
    
            

