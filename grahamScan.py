import matplotlib.pyplot as plt
from random import randrange, randint
import math
import time
from matplotlib import collections  as mc

#a is anchor
def polarAngle(p, a = None):
  if(a == None): a = anchor
  deltaX = p[0] - a[0]
  deltaY = p[1] - a[1]
  angle = math.atan2(deltaY, deltaX)
  return angle

def distance(p1, p2 = None):
  if(p2 == None): p2 = anchor
  return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def det(p1,p2,p3):
  return   (p2[0]-p1[0])*(p3[1]-p1[1]) \
      -(p2[1]-p1[1])*(p3[0]-p1[0])

def quicksort(a):
  if len(a)<=1: return a
  smaller,equal,larger=[],[],[]
  piv_ang=polarAngle(a[randint(0,len(a)-1)]) # select random pivot
  for pt in a:
    pt_ang=polarAngle(pt) # calculate current point angle
    if   pt_ang<piv_ang:  smaller.append(pt)
    elif pt_ang==piv_ang: equal.append(pt)
    else: larger.append(pt)
  return   quicksort(smaller) \
      +sorted(equal,key=distance) \
      +quicksort(larger)

def draw_line():
    pointAngles = list();
    points = list();
    for i in range(0,10):      
      x = randrange(3, 97)/100
      y = randrange(3, 97)/100
      points.append((x, y))
    

    lowestY = 1;
    lowestYIndex = 0;
    for i in range (0, len(points)):
      if(points[i][1] < lowestY):
        lowestY = points[i][1];
        lowestYIndex = i;

    print(lowestYIndex)
    global anchor;
    anchor = points[lowestYIndex];

    #plt.plot(anchor[0], anchor[1], linestyle="None", marker="o", color="r")
    points.pop(lowestYIndex)

    points = quicksort(points)

    hull = [anchor, points[0]]
    edges = []
    edges.append([anchor, points[0]])

    #remove the first element, since it's included above
    for it in range(2, len(points)):
      #for s in points[1:]:
        s = points[it]
        print(hull)
        edges.append([points[-1], s])
        edges.append([s, anchor])
        while( det(hull[-2], hull[-1], s) <= 0):        
          del hull[-1]
        hull.append(s)

    print(edges)

    hull.append(anchor)

    for hullPoint in hull:
      if(hullPoint in points):
        points.remove(hullPoint)

    hullCoordsX = list();
    for hullPoint in hull:
      hullCoordsX.append(hullPoint[0])

    hullCoordsY = list();
    for hullPoint in hull:
      hullCoordsY.append(hullPoint[1])

    pointsCoordsX = list();
    for point in points:
      pointsCoordsX.append(point[0])

    pointsCoordsY = list();
    for point in points:
      pointsCoordsY.append(point[1])

    #for edge in edges:
    #  plt.axline((edge[0][0], edge[0][1]), (edge[1][0], edge[1][1]))
    #plt.axline((0, 0), (.5, .5))

    lc = mc.LineCollection(edges, linewidths = 2)
    fix, ax = plt.subplots()
    ax.add_collection(lc)
    plt.plot(hullCoordsX, hullCoordsY, marker="o", color="r")
    plt.plot(pointsCoordsX, pointsCoordsY, linestyle="None", marker="o", color="b")
    plt.title("Graham Scan", fontsize=19)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()    
    plt.savefig('lissajous.png', bbox_inches='tight')

    

if __name__ == '__main__':
    draw_line()