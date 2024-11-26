from f.n03.str_bool_int.s_b_c.to_coloured_str import f as to_coloured_str
from k.n00.cn import ClassNameProperty

class String(str, ClassNameProperty):
  __repr__ = lambda self: self.cn + f'({super().__repr__()})'
  bbla = bright_black = property(lambda self: f'{to_coloured_str(self, 1, 0)}')
  bblu = bright_blue = property(lambda self: f'{to_coloured_str(self, 1, 4)}')
  bc = bright_cyan = property(lambda self: f'{to_coloured_str(self, 1, 6)}')
  bg = bright_green = property(lambda self: f'{to_coloured_str(self, 1, 2)}')
  bm = bright_magenta = property(lambda self: f'{to_coloured_str(self, 1, 5)}')
  br = bright_red = property(lambda self: f'{to_coloured_str(self, 1, 1)}')
  bw = bright_white = property(lambda self: f'{to_coloured_str(self, 1, 7)}')
  by = bright_yellow = property(lambda self: f'{to_coloured_str(self, 1, 3)}')
  dbla = dark_black = property(lambda self: f'{to_coloured_str(self, 0, 0)}')
  dblu = dark_blue = property(lambda self: f'{to_coloured_str(self, 0, 4)}')
  dc = dark_cyan = property(lambda self: f'{to_coloured_str(self, 0, 6)}')
  dg = dark_green = property(lambda self: f'{to_coloured_str(self, 0, 2)}')
  dm = dark_magenta = property(lambda self: f'{to_coloured_str(self, 0, 5)}')
  dr = dark_red = property(lambda self: f'{to_coloured_str(self, 0, 1)}')
  dw = dark_white = property(lambda self: f'{to_coloured_str(self, 0, 7)}')
  dy = dark_yellow = property(lambda self: f'{to_coloured_str(self, 0, 3)}')

def t():
  from f.n02.str_callable.s_p.print_and_return_false import f as pf
  from f.n03.object_object_object.x_y_z.pxyz import f as pxyz

  def t_class_name() -> bool:
    x = ''
    return pxyz(x, 'String', String(x).cn)
  if not t_class_name(): return pf('!t_class_name')

  def t_repr() -> bool:
    x = 't_repr'
    return pxyz(x, "String('t_repr')", repr(String(x)))
  if not t_repr(): return pf('!t_repr')

  def t_bbla() -> bool:
    x = 't_bbla'
    return pxyz(x, '\x1b[1;30mt_bbla\x1b[0;0m', String(x).bbla)
  if not t_bbla(): return pf('!t_bbla')

  def t_bblu() -> bool:
    x = 't_bblu'
    return pxyz(x, '\x1b[1;34mt_bblu\x1b[0;0m', String(x).bblu)
  if not t_bblu(): return pf('!t_bblu')

  def t_bc() -> bool:
    x = 't_bc'
    return pxyz(x, '\x1b[1;36mt_bc\x1b[0;0m', String(x).bc)
  if not t_bc(): return pf('!t_bc')

  def t_bg() -> bool:
    x = 't_bg'
    return pxyz(x, '\x1b[1;32mt_bg\x1b[0;0m', String(x).bg)
  if not t_bg(): return pf('!t_bg')

  def t_bm() -> bool:
    x = 't_bm'
    return pxyz(x, '\x1b[1;35mt_bm\x1b[0;0m', String(x).bm)
  if not t_bm(): return pf('!t_bm')

  def t_br() -> bool:
    x = 't_br'
    return pxyz(x, '\x1b[1;31mt_br\x1b[0;0m', String(x).br)
  if not t_br(): return pf('!t_br')

  def t_bw() -> bool:
    x = 't_bw'
    return pxyz(x, '\x1b[1;37mt_bw\x1b[0;0m', String(x).bw)
  if not t_bw(): return pf('!t_bw')

  def t_by() -> bool:
    x = 't_by'
    return pxyz(x, '\x1b[1;33mt_by\x1b[0;0m', String(x).by)
  if not t_by(): return pf('!t_by')

  def t_dbla() -> bool:
    x = 't_dbla'
    return pxyz(x, '\x1b[0;30mt_dbla\x1b[0;0m', String(x).dbla)
  if not t_dbla(): return pf('!t_dbla')

  def t_dblu() -> bool:
    x = 't_dblu'
    return pxyz(x, '\x1b[0;34mt_dblu\x1b[0;0m', String(x).dblu)
  if not t_dblu(): return pf('!t_dblu')

  def t_dc() -> bool:
    x = 't_dc'
    return pxyz(x, '\x1b[0;36mt_dc\x1b[0;0m', String(x).dc)
  if not t_dc(): return pf('!t_dc')

  def t_dg() -> bool:
    x = 't_dg'
    return pxyz(x, '\x1b[0;32mt_dg\x1b[0;0m', String(x).dg)
  if not t_dg(): return pf('!t_dg')

  def t_dm() -> bool:
    x = 't_dm'
    return pxyz(x, '\x1b[0;35mt_dm\x1b[0;0m', String(x).dm)
  if not t_dm(): return pf('!t_dm')

  def t_dr() -> bool:
    x = 't_dr'
    return pxyz(x, '\x1b[0;31mt_dr\x1b[0;0m', String(x).dr)
  if not t_dr(): return pf('!t_dr')

  def t_dw() -> bool:
    x = 't_dw'
    return pxyz(x, '\x1b[0;37mt_dw\x1b[0;0m', String(x).dw)
  if not t_dw(): return pf('!t_dw')

  def t_dy() -> bool:
    x = 't_dy'
    return pxyz(x, '\x1b[0;33mt_dy\x1b[0;0m', String(x).dy)
  if not t_dy(): return pf('!t_dy')
  return True
