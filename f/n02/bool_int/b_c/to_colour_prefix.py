def f(b: bool, c: int) -> str: return f'\033[{"1;" if b else "0;"}3{c}m'

def t():
  x = {'b': True, 'c': 1}
  y = '\x1b[1;31m'
  z = f(**x)
  from f.n03.object_object_object.x_y_z.pxyz import f as pxyz
  return pxyz(x, y, z)
