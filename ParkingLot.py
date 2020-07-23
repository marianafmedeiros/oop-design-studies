from abc import ABC, abstractmethod
from enum import Enum, IntEnum

class VehicleSize(IntEnum):
  SMALL = 1
  COMPACT = 2
  LARGE = 3

class Vehicle(ABC):
  def __init__(self, vehicle_size, license_plate, model):
    self.vehicle_size = vehicle_size
    self.license_plate = license_plate
    self.model = model
    self.spot_taken = None

  def take_spot(self, available_spot):
    self.spot_taken = available_spot
  
  def clear_spot(self):
    self.spots_taken = None

  @abstractmethod
  def can_fit_in_spot(self,spot):
    pass

class Car(Vehicle):

  def __init__(self, license_plate, model):
    super().__init__(VehicleSize.COMPACT, license_plate, model)
  
  def can_fit_in_spot(self,spot):
    if spot.size >= self.vehicle_size:
      return True
    else:
      raise Exception("The spot does not fit this car")

class Motorcycle(Vehicle):

  def __init__(self, license_plate, model):
    super().__init__(VehicleSize.SMALL, license_plate, model)
  
  def can_fit_in_spot(self,spot):
    return True

class Bus(Vehicle):

  def __init__(self, license_plate, model):
    super().__init__(VehicleSize.LARGE, license_plate, model)
  
  def can_fit_in_spot(self,spot):
    if spot.size >= self.vehicle_size:
      return True
    else:
      raise Exception("The spot does not fit this bus")

class ParkingSpots(object):
  def __init__(self, spot_size, spot_number, vehicle = None):
    self.size = spot_size
    self.number = spot_number
    self.vehicle = vehicle

  def take_spot(self, vehicle):
    self.vehicle = vehicle
    vehicle.take_spot(self)
  
  def clear_spot(self):
    if self.vehicle:
      self.vehicle = None
    else:
      raise Exception("This spot is already available")
  

