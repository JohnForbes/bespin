def f(s: str, b: bool, c: int) -> str:
  _RESET = "\033[0;0m"
  from f.n02.bool_int.b_c.to_colour_prefix import f as to_prfx
  return f'{to_prfx(b, c)}{s}{_RESET}'

def t():
  x = {'s': 'hello', 'b': True, 'c': 1}
  y = '\x1b[1;31mhello\x1b[0;0m'
  z = f(**x)
  from f.n03.object_object_object.x_y_z.pxyz import f as pxyz
  return pxyz(x, y, z)
