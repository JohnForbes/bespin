from os.path import exists as _exists

from k.n00.cn import ClassNameProperty
from k.n01.object.o.line import Line

class Path(Line, ClassNameProperty):
  exists = property(lambda self: _exists(self))

def t():
  from f.n02.str_callable.s_p.print_and_return_false import f as pf
  from f.n03.object_object_object.x_y_z.pxyz import f as pxyz

  def t_class_name() -> bool:
    x = ''
    return pxyz(x, 'Path', Path(x)._cn)
  if not t_class_name(): return pf('!t_class_name')

  def t_exists() -> bool:
    x = {'o': '.'}
    return pxyz(x, True, Path(**x).exists)
  if not t_exists(): return pf(f'!t_exists')
  return True
