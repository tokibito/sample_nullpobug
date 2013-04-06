# coding: utf-8
import json

DATA = """
{
  "attr1": "foo",
  "attr2": "bar",
  "_class": "Foo",
  "attr3": {
    "attr3_1": "spam",
    "attr3_2": "egg",
    "_class": "Bar"
  }
}
"""


class Base(object):
    def __init__(self, **kwargs):
        # 属性として値を持たせる
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        s = "<%s: %s>" % (
            self.__class__.__name__,
            ", ".join("%s=%s" %
            (key, value) for key, value in self.__dict__.items()))
        return s


class Foo(Base):
    pass


class Bar(Base):
    pass


def hook(dct):
    # _classの値から生成するインスタンスのクラスを判別
    class_name = dct.get('_class')
    if class_name == 'Foo':
        return Foo(**dct)
    elif class_name == 'Bar':
        return Bar(**dct)
    return dct


def main():
    """
    >>> main()
    <Foo: _class=Foo, attr2=bar, attr3=<Bar: attr3_2=egg, attr3_1=spam, _class=Bar>, attr1=foo>
    """
    # object_hookを使ってJSONデータをデコード
    result = json.loads(DATA, object_hook=hook)
    print result


if __name__ == '__main__':
    main()
