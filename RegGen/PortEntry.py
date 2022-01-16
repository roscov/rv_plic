
from RegGen.utils import Access

__all__ = ['PortEntry']

class PortEntry:

  """Represents an Entry in a port map"""
  def __init__(self, name, replication, width, access):
    self.name = name
    self.replication = replication
    self.replicator = ""
    if self.replication > 0:
      self.replicator = "[{}:0]".format(self.replication-1)
    assert width > 0, "pot shall be at least > 0 to exist!"
    self.width = width
    self.portwidth = ""
    if self.width > 1:
      self.portwidth = "[{}:0]".format(self.width-1)
    self.access = access

  def __str__(self):
    return '| {} | {:^4} | {} |'.format( self.name, self.width, self.access)

  def gen_read_port(self):
    out_string  = "  input  logic {1}{2} {0}_i,".format(self.name, self.replicator, self.portwidth)
    out_string += "\n"
    out_string += "  output logic {1} {0}_re_o".format(self.name, self.replicator)
    return out_string

  def gen_write_port(self):
    out_string  = "  output logic {1}{2} {0}_o,".format(self.name, self.replicator, self.portwidth)
    out_string += "\n"
    out_string += "  output logic {1} {0}_we_o".format(self.name, self.replicator)
    return out_string

  def gen_port(self):
    out_string  = "  // port {} ({})\n".format(self.name, self.access.__str__())
    if self.access != Access.WO:
      out_string += self.gen_read_port()
      out_string += ",\n"
    if self.access != Access.RO:
      out_string += self.gen_write_port()
      out_string += ",\n"
    return out_string

  def gen_defaults(self):
    out_string = "    // reg {} defaults\n".format(self.name)
    if self.access != Access.RO:
      out_string += "    {}_o    = '0;\n".format(self.name)
      out_string += "    {}_we_o = '0;\n".format(self.name)
    if self.access != Access.WO:
      out_string += "    {}_re_o = '0;\n".format(self.name)
    return out_string
