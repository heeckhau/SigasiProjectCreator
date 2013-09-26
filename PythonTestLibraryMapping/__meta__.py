#


"""
Meta level for reflective accesses.
"""

class EClass:
  """
  Define a class-like type
  """
  def __init__(self,name):
    self.name = name
  
class EStructuralFeature:
  """
  A structural feature is contained in a class and does not define behavior. 
  """
  def __init__(self,name,lower_bound=0,upper_bound=1):
    self.name = name
    self.lower_bound = lower_bound
    self.upper_bound = upper_bound  
        
class EAttribute(EStructuralFeature):
  """ 
  A meta attribute.
  """
  def __init__(self,name,lower_bound=0,upper_bound=1):  
     EStructuralFeature.__init__(self,name,lower_bound,upper_bound)
     
class EReference(EStructuralFeature):
  """ 
  A meta reference.
  """
  def __init__(self,name,lower_bound=0,upper_bound=1):  
     EStructuralFeature.__init__(self,name,lower_bound,upper_bound)