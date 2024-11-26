from k.n00.cn import ClassNameProperty

class Age(int, ClassNameProperty): pass

def t():
  from f.n02.str_callable.s_p.print_and_return_false import f as pf
  from f.n03.object_object_object.x_y_z.pxyz import f as pxyz

  def t_class_name() -> bool:
    x = 0
    return pxyz(x, 'Age', Age(x)._cn)
  if not t_class_name(): return pf('!t_class_name')

  def t_int():
    x = 2
    from f.n03.object_object_object.x_y_z.pxyz import f as pxyz
    return pxyz(x, 2, int(Age(x)))
  if not t_int(): return pf('!t_int')
  return True
