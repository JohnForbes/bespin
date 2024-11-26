from k.n01.object.o.string import String

class Spaceless(String):
  def __new__(cls, o: object):
    if ' ' in o: raise ValueError(f'{o=} contains a space character.')
    return super().__new__(cls, o)

def t():
  from f.n02.str_callable.s_p.print_and_return_false import f as pf
  from f.n03.object_object_object.x_y_z.pxyz import f as pxyz

  def t_space_present() -> bool:
    x = {'o': 'abc ghi'} 
    y = "o='abc ghi' contains a space character."
    try: z = Spaceless(**x)
    except ValueError as e: z = str(e)
    return pxyz(x, y, z)
  if not t_space_present(): return pf('!t_space_present')

  def t_b() -> bool:
    x = {'o': 'jklmno'} 
    y = 'jklmno' 
    z = str(Spaceless(**x)) 
    return pxyz(x, y, z)
  if not t_b(): return pf('!t_b')
  return True
