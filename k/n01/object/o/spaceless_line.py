from k.n01.object.o.spaceless import Spaceless
from k.n01.object.o.line import Line

class SpacelessLine(Spaceless, Line): pass

def t():
  from f.n02.str_callable.s_p.print_and_return_false import f as pf
  from f.n03.object_object_object.x_y_z.pxyz import f as pxyz

  def t_class_name() -> bool:
    x = ''
    return pxyz(x, 'SpacelessLine', SpacelessLine(x).cn)
  if not t_class_name(): return pf('!t_class_name')
  return True
