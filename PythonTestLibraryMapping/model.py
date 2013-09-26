#

""" 
No documentation found for this module.

"""
# importing the relations
from __rels__ import _LibraryMappingsMappingsMapping 

# Import common base class
from __common__ import Model_base

class LibraryMappings(Model_base):
    """ 
    
      Container(s)  : 
      >>> librarymappings = LibraryMappings()  
      >>> librarymappings.Version = None
      >>> librarymappings.LastModified = None
      >>> librarymappings.Mappings.append(Mapping())
      >>> mapping  = librarymappings.Mappings[0]
    
    """

    def __init__(self):
        Model_base.__init__(self)
        self._parent_ = None
        self._meta_ = self.__class__
        self.Version = None
        self.LastModified = None
    
        self.Mappings = _LibraryMappingsMappingsMapping(parent=self)
        self.Mappings._parent_ = self


class Mapping(Model_base):
    """ 
    
     Container(s)  : LibraryMappings
      >>> mapping = Mapping()  
      >>> mapping.Location = None
      >>> mapping.Library = None
    
    
    """

    def __init__(self):
        Model_base.__init__(self)
        self._parent_ = None
        self._meta_ = self.__class__
        self.Location = None
        self.Library = None


# Enumerations


import unittest

class Testmodel(unittest.TestCase):

    def testLibraryMappingsAttributes(self):
        librarymappings = LibraryMappings()  
        librarymappings.Version = None
        self.assertEquals(librarymappings.Version, None)
        librarymappings.LastModified = None
        self.assertEquals(librarymappings.LastModified, None)
    
    def testMappingAttributes(self):
        mapping = Mapping()
        mapping.Location = None
        self.assertEquals(mapping.Location, None)
        mapping.Library = None
        self.assertEquals(mapping.Library, None)
    
    
    def testLibraryMappingsRelationsMappings(self):
        librarymappings = LibraryMappings()  
        # testing Mappings      
        # checking unicity support
        mapping1 = Mapping()
        librarymappings.Mappings.append(mapping1)
        self.assertRaises(Exception, librarymappings.Mappings.append, mapping1)
        # checking upper_bound limit


if __name__ == '__main__':
    unittest.main()
