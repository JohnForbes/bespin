def f(c: type, o: object):
  from f.n02.type_object.c_o.not_is_inst import f as nii
  return c(o) if nii(c=c, o=o) else o

def t():
  from f.n02.str_callable.s_p.print_and_return_false import f as pf
  def t_a():
    class K: pass
    x = {'c': K, 'o': K()}
    y = x['o']
    z = f(**x)
    from f.n03.object_object_object.x_y_z.pxyz import f as pxyz
    return pxyz(x, y, z)
  if not t_a(): return pf('!t_a')

  def t_b():
    class K(str): pass
    x = {'c': K, 'o': 'abc'}
    y = K('abc')
    z = f(**x)
    from f.n03.object_object_object.x_y_z.pxyz import f as pxyz
    return pxyz(x, y, z)
  if not t_b(): return pf('!t_b')
  return True
