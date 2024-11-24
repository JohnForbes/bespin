
def f(x: object, y: object, z: object, p: callable=print, new_line=False) -> bool:
  if y != z or type(y) != type(z):
    p(f'{x=}')
    p(f'{type(x)=}')
    p(f'{y=}')
    p(f'{type(y)=}')
    p(f'{z=}')
    p(f'{type(z)=}')
  return y == z

def t():
  from k.n00.fake_printer import FakePrinter
  from f.n02.str_callable.s_p.print_and_return_false import f as pf
  def t_true():
    _fake_printer = FakePrinter()
    x = {'x': 1, 'y': 1, 'z': 1, 'p': _fake_printer}
    return all([f(**x), _fake_printer.history == []])
  if not t_true(): return pf('!t_true')

  def t_false():
    p = FakePrinter()
    x = {'x': 1, 'y': 1, 'z': 2}
    if f(**x, p=p): return pf('!A')
    y = [
      'x=1', "type(x)=<class 'int'>",
      'y=1', "type(y)=<class 'int'>",
      'z=2', "type(z)=<class 'int'>"
    ]
    z = p.h
    if z != y:
      print(f'{y=}')
      print(f'{z=}')
      return pf('!B')
    return True
  if not t_false(): return pf('!t_false')
  return 1
