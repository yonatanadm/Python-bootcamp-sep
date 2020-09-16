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
            if not d.flag:
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

* Very good! This code works.
* Notice that add_dependency() may be called more than once on the same object,
  therefore you should add the dependencies and not replace them.
* `def __init__(self, name):` there is no need for an empty line above it
  and below `class Widget:`.
* It might be useful to define the __str__ method in class Widget.
  This method is used when converting the object to a string 
  (for example by `print(luke)`).
  For example:
  
    def __str__(self):
        return str(self.name)

"""
