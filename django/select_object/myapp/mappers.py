# coding: utf-8
from bpmappers import Mapper, RawField


class PlayerMapper(Mapper):
    Name = RawField('name')
    Generation = RawField('generation')
    Level = RawField('level')
