#


"""

Module model

Sample usage :
  >>> from model import LibraryMappings
  >>> librarymappings = LibraryMappings()  
  >>> librarymappings.Version = None
  >>> librarymappings.LastModified = None
  >>> librarymappings.Mappings.append(Mapping())
  >>> mapping  = librarymappings.Mappings[0]


"""


from model import *

from __factory__ import Model_factory
"""
Initialize the default instances factory
"""
factory = Model_factory()
#Start of user code model __init__ 
# here you may redefine the module singletons or do some special tricks
#End of user code

from __common__ import Model_resource_factory
resourceFactory = Model_resource_factory()