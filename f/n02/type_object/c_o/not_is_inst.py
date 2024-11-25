def f(c: type, o: object):
  if not isinstance(c, type):
    raise TypeError(f"expected type, observed: {type(c)}")
  return not isinstance(o, c)

def t():
  from f.n02.str_callable.s_p.print_and_return_false import f as pf
  from k.n03.object_object_object.input_expectation_observation.xyz import XYZ

  def t_0():
    class K: pass
    class C: pass
    x = {'c': K, 'o': C()}
    return XYZ(x, True, f(**x))()
  if not t_0(): return pf('!t_0')

  def t_1():
    class K: pass
    x = {'c': K, 'o': K()}
    return XYZ(x, False, f(**x))()
  if not t_1(): return pf('!t_1')
  return 1
