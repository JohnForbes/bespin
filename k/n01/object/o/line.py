from k.n01.object.o.string import String

class Line(String):
  indentation = property(lambda self: len(self) - len(self.lstrip()))
  trimmed = property(lambda self: self.lstrip())

  def __new__(cls, o: object):
    if '\n' in o: raise ValueError(f"{o=} contains a newline character.")
    return super().__new__(cls, o)

def t():
  from f.n02.str_callable.s_p.print_and_return_false import f as pf
  from f.n03.object_object_object.x_y_z.pxyz import f as pxyz

  def t_nl_present() -> bool:
    x = {'o': 'abc\nghi'} 
    y = "o='abc\\nghi' contains a newline character."
    try:
      z = Line(**x) 
    except ValueError as e:
      z = str(e)
    return pxyz(x, y, z)
  if not t_nl_present(): return pf('!t_nl_present')

  def t_nl_absent() -> bool:
    x = {'o': 'jklmno'} 
    y = 'jklmno' 
    z = str(Line(**x)) 
    return pxyz(x, y, z)
  if not t_nl_absent(): return pf('!t_nl_absent')
  return True
