class Car(object):
 # create an instance of attributes number of door, wheels and speed
  num_of_doors = 4
  num_of_wheels = 4
  speed = 0
  # special methods that assigns attributes to the class car
  def __init__(self, name = 'General', model = 'GM',car_type = 'saloon'):
    self.name = name
    self.model = model
    self.car_type = car_type
    self.speed = 0
    # condition for name attribute
    if self.name == 'Porshe' or self.name == 'Koenigsegg':
      self.num_of_doors = 2
    # condition for car_type attribute
    if self.car_type == 'trailer':
      self.num_of_wheels = 8
# method that inherits the main method
  def is_saloon(self):
    return self.car_type
  # drive method that checks speed condition
  def drive(self,drive_speed):
    if drive_speed:
      if drive_speed == 7 and self.car_type == 'trailer':
        self.speed = 77
      elif drive_speed == 3 and self.name == 'Mercedes':
        self.speed = 1000
      return self
