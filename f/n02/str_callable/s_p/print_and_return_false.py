# print_and_return_false
# pf
def f(s: str, p: callable=print) -> bool:
  p(s)
  return False

def t():
  from k.n00.fake_printer import FakePrinter
  fake_printer = FakePrinter()
  x = {'s': 'hello', 'p': fake_printer}
  y = False
  z = f(**x)
  if fake_printer.history != [x['s']]:
    print("fake_printer.history != [x['s']]")
    return False 
  from f.n03.object_object_object.x_y_z.pxyz import f as pxyz
  return pxyz(x, y, z)
