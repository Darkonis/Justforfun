from math import *
x=0
y=0
z=0
theta=0
wayIndex = 0
numPoints =3 
curWay=[]
distTol=.5;
waypoints = []
while 1:
  curWay= getCurrWay(wayIndex,waypoints,curWay)
  if sqrt(pow(x-curWay[0],2)+pow(z-curWay[2],2))<.5:
    wayIndex+=1
  elif abs(theta - tarTheta(curWay)>3.1415/18):
    turnBotToTar(curWay)
  else:
    straight()
    











def getCurrWay(wayIn,wayPoints,curway):
    curway=wayPoints[wayIn]
    return curway
def tarTheta(curway):
  return tan((curway[0]-x)/curway[2]-z)
def turnBotToTar(curway):
  if tarTheta(curway)<180 :
    turnLeft()
  else:
    turnRight()
    return
