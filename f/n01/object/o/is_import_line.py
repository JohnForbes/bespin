def f(o: object) -> bool: return 'from ' in o and ' import ' in o

def t():
  from f.n02.str_callable.s_p.print_and_return_false import f as pf
  from f.n03.object_object_object.x_y_z.pxyz import f as pxyz

  def t_str_0() -> bool:
    x = ''
    return pxyz(x, False, f(x))
  if not t_str_0(): return pf(f'!t_str_0')

  def t_str_1() -> bool:
    x = 'from f.n03.object_object_object.x_y_z.pxyz imp''ort f as pxyz'
    return pxyz(x, True, f(x))
  if not t_str_1(): return pf(f'!t_str_1')
  return True
