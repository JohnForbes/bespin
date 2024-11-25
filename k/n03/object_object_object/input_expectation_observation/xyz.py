from f.n02.str_callable.s_p.print_and_return_false import f as pf

class XYZ:
  __call__ = lambda self: self._pxyz()
  __repr__ = lambda self: f'{self.__class__.__name__}({self.tu})'
  __str__ = lambda self: f'{self.tu}'
  di = dict = property(lambda self: self._to_dict())
  par = print_and_return_y_eq_z = lambda self: self._pxyz()
  tu = tuple = property(lambda self: self._to_tuple())
  x = input = property(lambda self: self._x)
  y = expectation = property(lambda self: self._y)
  z = observation = property(lambda self: self._z)

  _to_dict = lambda self: {'x': self.x, 'y': self.y, 'z': self.z}
  _to_tuple = lambda self: (self.x, self.y, self.z)

  def _pxyz(self):
    from f.n03.object_object_object.x_y_z.pxyz import f as pxyz
    return pxyz(x=self.x, y=self.y, z=self.z, p=self._p, new_line=self._new_line)

  def __init__(
    self,
    input: object,
    expectation: object,
    observation: object,
    p=print,
    new_line=False
  ):
    self._x = input
    self._y = expectation
    self._z = observation
    self._p = p
    self._new_line = new_line

InputExpectationObservation = XYZ

def t():
  from k.n00.fake_printer import FakePrinter

  def t_true():
    _fake_printer = FakePrinter()
    x = {'input': 1, 'expectation': 1, 'observation': 1, 'p': _fake_printer}
    z = XYZ(**x)()
    if not z: return pf('!a')
    if not _fake_printer.history == []: return pf('!b')
    return True
  if not t_true(): return pf('!t_true')

  def t_false():
    _fake_printer = FakePrinter()
    x = {'input': 1, 'expectation': 1, 'observation': 2, 'p': _fake_printer}
    observation_history = XYZ(**x)()
    if observation_history: return pf('!a')
    expectation_history = [
      'x=1', "type(x)=<class 'int'>",
      'y=1', "type(y)=<class 'int'>",
      'z=2', "type(z)=<class 'int'>"
    ]
    observation_history = _fake_printer.h
    if expectation_history != observation_history:
      return pf('\n'.join([
        f'{expectation_history=}',
        f'{observation_history=}'
      ]))
    return True
  if not t_false(): return pf('!t_false')
  return 1
