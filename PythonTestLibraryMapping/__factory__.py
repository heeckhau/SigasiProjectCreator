#

"""

"""

from model	import LibraryMappings
from model	import Mapping


class Model_factory:  
  """ Factory to create elements from model
  """  
  
  def create(self,name):
    """ generic method to create elements.
        This method is able to create:
			LibraryMappings
			Mapping
        
    """
    f = getattr(self,"create%s" % name)
    return f()
    
  def createLibraryMappings(self):
    """
    Create an instance of LibraryMappings.
    """
    instance = LibraryMappings()
    #Start of user code LibraryMappings create
    # type here special initialization code
    #End of user code
    return instance
  	  	
  def createMapping(self):
    """
    Create an instance of Mapping.
    """
    instance = Mapping()
    #Start of user code Mapping create
    # type here special initialization code
    #End of user code
    return instance
  	  	
    
  #Start of user code model factory methods
  #End of user code


  


import unittest

class Test_model_factory(unittest.TestCase):  
  def testLibraryMappingsCreation(self):
    """
    Test the direct instanciation of a LibraryMappings.
    """ 
    d = LibraryMappings()
    self.assertTrue(d!=None)
    
  def testLibraryMappingsCreationFactory(self):
    """
    Test the instanciation of a LibraryMappings through the factory.
    """
    factory = Model_factory()
    d = factory.create("LibraryMappings")
    self.assertTrue(d != None)
    self.assertTrue(isinstance(d, LibraryMappings))

  def testMappingCreation(self):
    """
    Test the direct instanciation of a Mapping.
    """ 
    d = Mapping()
    self.assertTrue(d!=None)
    
  def testMappingCreationFactory(self):
    """
    Test the instanciation of a Mapping through the factory.
    """
    factory = Model_factory()
    d = factory.create("Mapping")
    self.assertTrue(d != None)
    self.assertTrue(isinstance(d, Mapping))

    
if __name__ == '__main__':
    unittest.main()

