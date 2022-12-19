import time
import random
import matplotlib.pyplot as plt


def calcHist(data):
  hist = [0] * 10

  for num in data:
    num_hist = num // 100

    hist[num_hist] += 1

  plotting(hist)
  return #hist

def plotting(hist):
  
  x = [i for i in range (10)]
  fig, ax = plt.subplots()
  
  ax.bar(x, hist)

  fig.set_figwidth(12) 
  fig.set_figheight(6)    

  plt.show()
  return
  
def initListWithRandomNumbers():

  rand_list = []
  n = 1000000

  for i in range(n):
      rand_list.append(random.randint(0,999))

  return rand_list

def body():
  a = initListWithRandomNumbers()
# starting time
  start = time.time()
  #hist = calcHist(a)
  calcHist(a)
# end time
  end = time.time()
# total time taken
  t = end - start
  return t


t_min = 1000000
t_max = 0
t_mid = 0

times = 100
for i in range(times):
  t = body()

  if (t > t_max):
    t_max = t
  
  if (t < t_min):
    t_min = t

  t_mid += t

t_mid /= times
print('Наименьшее время: {} \nНаибольшее время: {} \nСреднее время: {}'.format(t_min, t_max, t_mid))