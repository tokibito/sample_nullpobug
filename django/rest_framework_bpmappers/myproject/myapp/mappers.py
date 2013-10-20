from bpmappers import Mapper, RawField


class ItemMapper(Mapper):
    item_id = RawField('id')
    item_name = RawField('name')
