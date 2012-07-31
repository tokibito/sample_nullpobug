# coding: utf-8
import sys
from zope.interface import Interface
from zope.interface.registry import Components


class ICalculator(Interface):
    pass


class AddCalculator(object):
    def calculate(self, val1, val2):
        return val1 + val2


class SubCalculator(object):
    def calculate(self, val1, val2):
        return val1 - val2


class MulCalculator(object):
    def calculate(self, val1, val2):
        return val1 * val2


class DivCalculator(object):
    def calculate(self, val1, val2):
        return val1 / val2


def main():
    registry = Components()
    registry.utilities.register([], ICalculator, "add", AddCalculator())
    registry.utilities.register([], ICalculator, "sub", SubCalculator())
    registry.utilities.register([], ICalculator, "mul", MulCalculator())
    registry.utilities.register([], ICalculator, "div", DivCalculator())
    if len(sys.argv) > 3:
        calc_name = sys.argv[1]
        val1 = int(sys.argv[2])
        val2 = int(sys.argv[3])
    else:
        print("Usage: %s calc_name val1 val2" % __file__)
        sys.exit()
    calc = registry.utilities.lookup([], ICalculator, calc_name)
    if calc is None:
        print("There is not matching calculator: %s" % calc_name)
        sys.exit()
    print(calc.calculate(val1, val2))


if __name__ == '__main__':
    main()
