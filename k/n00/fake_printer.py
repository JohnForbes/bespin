class FakePrinter:
  __call__ = lambda self, x: self._history.append(x)
  h = history = property(lambda self: self._history)
  r = reset = lambda self: self._reset()
  def __init__(self): self._history = []
  def _reset(self): self._history = []

def t():
  fake_printer = FakePrinter()
  if fake_printer.history != []:
    print("FAILED: fake_printer.history != []")
    return 0

  fake_printer('boo')
  if fake_printer.history != ['boo']:
    print("FAILED: fake_printer.history != ['boo']")
    return 0

  fake_printer('bang')
  if fake_printer.history != ['boo', 'bang']:
    print("FAILED: fake_printer.history != ['boo', 'bang']")
    return 0

  fake_printer.reset()
  if fake_printer.history != []:
    print("FAILED: fake_printer.history != []")
    return 0
  return 1
