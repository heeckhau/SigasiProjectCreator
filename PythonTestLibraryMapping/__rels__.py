""" This module is used to represents the relations between entities and 
their cardinalities
"""
from __common__ import ModelRelationBase

class _LibraryMappingsMappingsMapping(ModelRelationBase):
  """ Class used to represent the relation between LibraryMappings
      and Mapping"""
  def __init__(self,parent=None):
    ModelRelationBase.__init__(self)
    self.upper_bound = -1
    self.lower_bound = 0
    self.is_unique = True
    self._parent_ = parent

    
  def append(self,mapping,stopcycle=False):
    if mapping in self:
      raise Exception("Element is already in the set")
    mapping._parent_ = self._parent_
    list.append(self,mapping)
    
    
       
