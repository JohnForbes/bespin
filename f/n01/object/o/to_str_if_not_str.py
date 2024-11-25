def f(o: object):
  from f.n02.type_object.c_o.to_k_if_not_k import f as to_k_if_not_k
  return to_k_if_not_k(c=str, o=o)

def t():
  x = {'o': 123}
  from f.n03.object_object_object.x_y_z.pxyz import f as pxyz
  return pxyz(x, '123', f(**x))
