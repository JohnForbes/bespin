class ClassNameProperty:
  cn = class_name = property(lambda self: self.__class__.__name__)

def t():
  class K(ClassNameProperty): pass
  y = 'K'
  z = K().cn
  if y == z: return True
  print(f'{y=}, {z=}')
  return False
