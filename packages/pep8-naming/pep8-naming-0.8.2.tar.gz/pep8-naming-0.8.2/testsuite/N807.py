#: Okay
class C1:
    def __str__(self):
        return ''
#: Okay
class C2:
    if True:
        def __str__(self):
            return ''
#: N807
if True:
    def __bad__():
        pass
#: Okay
class C3:
    try:
        if True:
            while True:
                def __str__(self):
                    return ''
                break
    except:
        pass
#: N807
def __bad():
    pass
#: N807:1:5
def bad__():
    pass
#: N807
def __bad__():
    pass
#: N807
class ClassName(object):
    def method(self):
        def __bad():
            pass
#: Okay(--ignore-names=__bad)
def __bad():
    pass
#: Okay
def __dir__():
    pass
#: Okay
def __getattr__(name):
    pass
