from k.n00.cn import ClassNameProperty

class Line(int, ClassNameProperty):
  def __new__(cls, line: int):
    from f.n02.type_object.c_o.to_k_if_not_k import f as to_k_if_not_k
    line = to_k_if_not_k(c=int, o=line)
    if not isinstance(line, int):
      raise TypeError(
        '; '.join([
          f'line must be of type int; observed: {type(line)}',
          f'object: {line}'
        ])
      )
    return super().__new__(cls, line)

def t():
  from f.n02.str_callable.s_p.print_and_return_false import f as pf
  from f.n03.object_object_object.x_y_z.pxyz import f as pxyz

  def t_class_name() -> bool:
    x = '1'
    return pxyz(x, 'Line', Line(x)._cn)
  if not t_class_name(): return pf('!t_class_name')

  def t_new() -> bool:
    x = 2
    return pxyz(x, 2, int(Line(x)))
  if not t_new(): return pf(f'!t_new')
  return True
