


import math


class World:
  def __init__(self):
    print("World created")
    self.setdt()
    self.setStartTime()

    self.objects = [] # this is probably not a good way to store object but we'll try this for now :shrug:

  def setDomain(self, x, y):
    """
      Assuming origin is always at 0,0 and x,y define a rectangle around it.
    """
    self.x_lim = x
    self.y_lim = y

  def addObject(self, newObject):
    # Gonna assume all object are just points
    self.objects.append(newObject)

  def setdt(self, dt = 0.1):
    self.dt = 0.1

  def setStartTime(self, t0 = 0):
    self.t = t0

  def updatetime(self):
    self.t = self.t + self.dt

  def stepTime(self):
    # REVISIT ned to rework how we calculate acceleration

    w = 0.5
    r = 1
    # v0 = w/r
    a_mag = w**2/r

    for object in self.objects:
      ax = -a_mag * (object.x/r) # cos(theta)
      ay = -a_mag * (object.y/r) # cos(theta)
      a = (ax , ay) # eh we'll figure out how to represent acceleration later
      object.objectUpdate(self.dt, a)

    self.updatetime()


class object:
  def __init__(self, x, y, vx = 0, vy = 0, ax = 0, ay = 0):
    self.x, self.y = x, y # sets initial position
    self.vx = vx
    self.vy = vy

  def objectUpdate(self, dt, a: tuple):
    self.updatePosition(dt)
    self.updateVelocity(dt, a)

  def updateVelocity(self, dt, a: tuple):
    self.vx = a[0]*dt + self.vx
    self.vy = a[1]*dt + self.vy

  def updatePosition(self, dt):
    self.x = self.vx*dt + self.x
    self.y = self.vy*dt + self.y



if __name__=="__main__":
  print("hello world")

  world = World()
  world.setDomain(10, 10)

  world.addObject(object(1,0, vy=0.5))

  while world.t < 10:
    world.stepTime()
    print(world.objects[0].x, world.objects[0].y)
    # print(world.objects[0].vx,world.objects[0].vy)



