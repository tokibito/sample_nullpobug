from bpmappers import Mapper, RawField

class ResouceMapper(Mapper):
    resource_uri = RawField()

class ItemMapper(ResouceMapper):
    item_id = RawField('id')
    item_name = RawField('name')
