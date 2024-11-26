from k.n00.cn import ClassNameProperty

class Column(int, ClassNameProperty):
  def __new__(cls, column: int):
    from f.n02.type_object.c_o.to_k_if_not_k import f as to_k_if_not_k
    column = to_k_if_not_k(c=int, o=column)
    if not isinstance(column, int):
      raise TypeError(
        '; '.join([
          f'column must be of type int; observed: {type(column)}',
          f'object: {column}'
        ])
      )
    return super().__new__(cls, column)

def t():
  from f.n02.str_callable.s_p.print_and_return_false import f as pf
  from f.n03.object_object_object.x_y_z.pxyz import f as pxyz

  def t_class_name() -> bool:
    x = '1'
    return pxyz(x, 'Column', Column(x)._cn)
  if not t_class_name(): return pf('!t_class_name')

  def t___new__() -> bool:
    x = 2
    y = 2
    z = int(Column(x))
    return pxyz(x, y, z)
  if not t___new__(): return pf(f'!t___new__')
  return True
