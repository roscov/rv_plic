
__all__ = ['AddrMapEntry']

from .utils import Access

class AddrMapEntry:

  """Represents an Entry in an Address Map"""
  def __init__(self, addr, name, description, access, width, index=None, offset=0, addr_len=32):
    self.addr = addr
    self.description = description
    self.access = access
    self.width = width
    self.name = name
    self.addr_len = addr_len
    self.indexer = ""
    if index != None:
        self.indexer = "[{}]".format(index)
    assert offset >= 0, "register offset cannot be negative !"
    self.offsetter = "[{}:{}]".format( self.width-1+offset, offset)

  def __str__(self):
    return '| {} | {:>8} | {} | {} | {} | {}'.format(self.name, hex(self.addr), self.width, self.access, self.description)

  def gen_read_accessor(self):
    return "{}_i{}{}".format(self.name, self.indexer, self.offsetter)

  def gen_write_accessor(self):
    return "{}_o{}{}".format(self.name, self.indexer, self.offsetter)

  def gen_read_logic(self, signal):
    out_string = ""
    if self.access != ( Access.WO or Access.RESERVED ):
      out_string += "          // read logic for {}\n".format(self.name)
      out_string += "          {}'h{:<8}: begin\n".format(self.addr_len, hex(self.addr)[2:])
      out_string += "            {}[{}:0] = {};\n".format( signal, self.width-1, self.gen_read_accessor())
      out_string += "            {}_re_o{} = 1'b1;\n".format(self.name, self.indexer)
      out_string += "          end\n"
    return out_string

  def gen_write_logic(self, signal):
    out_string = ""
    if self.access !=  ( Access.RO or Access.RESERVED ):
      out_string  = "          // write logic for {}\n".format(self.name)
      out_string += "          {}'h{:<8}: begin\n".format(self.addr_len, hex(self.addr)[2:])
      out_string += "            {} = {}[{}:0];\n".format(self.gen_write_accessor(), signal, self.width-1)
      out_string += "            {}_we_o{} = 1'b1;\n".format(self.name, self.indexer)
      out_string += "          end\n"
    return out_string

