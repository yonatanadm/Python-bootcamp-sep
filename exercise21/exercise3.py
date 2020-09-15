class Widget:

    def __init__(self, name):
        self.name = name
        self._dependencies = []
        self.flag = False

    def add_dependency(self, *list_d):
        self._dependencies = list_d

    def build(self):
        self.flag = True
        for d in self._dependencies:
            if not d.built:
                d.build()
                print(d.name)


luke = Widget("Luke")
hansolo = Widget("Han Solo")
leia = Widget("Leia")
yoda = Widget("Yoda")
padme = Widget("Padme Amidala")
anakin = Widget("Anakin Skywalker")
obi = Widget("Obi-Wan")
darth = Widget("Darth Vader")
_all = Widget("")

luke.add_dependency(hansolo, leia, yoda)
leia.add_dependency(padme, anakin)
obi.add_dependency(yoda)
darth.add_dependency(anakin)

_all.add_dependency(luke, hansolo, leia, yoda, padme, anakin, obi, darth)
_all.build()
# code should print: Han Solo, Padme Amidala, Anakin Skywalker, Leia, Yoda, Luke, Obi-Wan, Darth Vader
# (can print with newlines in between modules)

"""
Uri's comments:
==============

* I tried to run your code, but I got this exception:

Traceback (most recent call last):
  File ".../yonatanadm___python-bootcamp-september-2020/exercise21/exercise3.py", line 35, in <module>
    _all.build()
  File ".../yonatanadm___python-bootcamp-september-2020/exercise21/exercise3.py", line 14, in build
    if not d.built:
AttributeError: 'Widget' object has no attribute 'built'

It's better to always run your code locally before you commit.

"""
