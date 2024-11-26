from k.n01.object.o.string import String

_codes_to_verbose = {
  '??': 'untracked',
  'A': 'added',
  'M': 'modified',
  'D': 'deleted',
  'R': 'renamed',
  'C': 'copied',
  'U': 'unmerged',
  ' ': 'unmodified',
  '': 'unmodified'
}

_codes_to_prefixes = {
  ' ?': 'Added',
  '??': 'Added',
  'A': 'Added',
  'A ': 'Added',
  ' M': 'Modified',
  'M ': 'Modified',
  'MM': 'Modified',
  'M': 'Modified',
  ' D': 'Removed',
  'D': 'Removed',
  'R': 'Renamed',
  'C': 'Copied',
  'U': 'Unmerged',
}

class GitStatusCode(String):
  verbose = property(lambda self: self._verbose())

  def _verbose(self) -> str: return _codes_to_verbose[self]

  def __new__(cls, code: str):
    if code not in _codes_to_verbose:
      raise ValueError(f'"{repr(code)}" is not a valid Git status code.')
    return super().__new__(cls, code)

  def to_commit_message_prefix(self) -> str: return _codes_to_prefixes[self]

def t():
  from f.n02.str_callable.s_p.print_and_return_false import f as pf
  from f.n03.object_object_object.x_y_z.pxyz import f as pxyz

  def t_class_name() -> bool:
    x = ''
    return pxyz(x, 'GitStatusCode', GitStatusCode(x)._cn)
  if not t_class_name(): return pf('!t_class_name')

  def t_verbose() -> bool:
    x = '??'
    return pxyz(x, 'untracked', GitStatusCode(x).verbose)
  if not t_verbose(): return pf(f'!t_verbose')

  def t_to_commit_message_prefix() -> bool:
    x = '??'
    return pxyz(x, 'Added', GitStatusCode(x).to_commit_message_prefix())
  if not t_to_commit_message_prefix(): return pf(f'!t_to_commit_message_prefix')
  return True
