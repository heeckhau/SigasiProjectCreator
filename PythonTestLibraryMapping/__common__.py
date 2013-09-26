#


"""

"""

class Model_base:
  """
  Model_base is the base class of all elements in the model module.
  """ 
  def __init__(self):
    #Start of user code for Model_base initialization
    pass
    #End of user code
    self.__internal_resource__ = None
   
  def __eResource__(self):
    pass 

class ModelRelationBase(list):
  """
  Base class for relations
  """
  pass
  
class Model_resource:
  """
   The Model_resource is responsible for model serialization.
  """
  def __init__(self,uri):
    #Start of user code for Model_resource initialization
    # type here your specific code
    #End of user code
    self.__content__ = []
    self.__uri__ = uri

  def load(self,options=dict()):
    pass
    
  def save(self,options=dict()):
    pass
    
    
 
class Model_resource_factory:
  """
   The Model_resource_factory is responsible for creating resource.
  """
  def __init__(self):
    #Start of user code for Model_resource_factory initialization
    # type here your specific code
    pass
    #End of user code

  def create(self,uri,options=dict()):
    pass
