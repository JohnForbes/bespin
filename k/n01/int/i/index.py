class Index(int):
  def __new__(cls, i: int):
    from f.n02.type_object.c_o.to_k_if_not_k import f as to_k_if_not_k
    i = to_k_if_not_k(c=int, o=i)
    if i < 0: raise ValueError(f'{i} must be greater than or equal to 0.')
    return super().__new__(cls, i)

def t():
  x = 2
  from f.n03.object_object_object.x_y_z.pxyz import f as pxyz
  return pxyz(x, 2, int(Index(x)))
