
#from RegGen import *
from datetime import datetime
from math import ceil
import os
from RegGen import clog2, Access, __version__
from .PortEntry import PortEntry
from .AddrMapEntry import AddrMapEntry

class AddrMap:
  def __init__(self, name, description, access_width=32, protocol="reg", addr_len=32):
    self.access_width = access_width
    self.name = name
    self.description = description
    self.addrmap = []
    self.ports = []
    self.protocol = protocol
    self.addr_len = addr_len

  def newRegPort(self, name, baseaddr, width, access : Access, description, replication=0, replication_offset=1):
    self.ports.append(PortEntry(name, replication, width, access))
    reg_cuts = ceil(width / self.access_width)
    for cut_entry in range(0, reg_cuts):
      entry_offset = cut_entry*self.access_width
      entry_width  = width - entry_offset if (width - entry_offset) < self.access_width else self.access_width
      entry_baseaddr = baseaddr + cut_entry*(clog2(self.access_width) - 1)
      if replication == 0 :
        self.addrmap.append(AddrMapEntry(addr=entry_baseaddr, name=name, description=description, access=access, width=entry_width, index=None, offset=entry_offset, addr_len=self.addr_len))
      else:
        assert replication_offset >= 1, "cannot replicate register entry less than once"
        for replica in range(0, replication):
          replica_baseaddr = entry_baseaddr + replica*replication_offset
          self.addrmap.append(AddrMapEntry(addr=replica_baseaddr, name=name, description=description, access=access, width=entry_width, index=replica, offset=entry_offset, addr_len=self.addr_len))


  def gen_verilog_portlist(self):
    out_string  = "(\n"
    for port in self.ports:
        out_string += port.gen_port()
        out_string += "\n"
    out_string += self.gen_verilog_bus_port()
    out_string += ");\n"
    return out_string

  def gen_verilog_bus_port(self):
    out_string  = "\n"
    ## APB3 interface
    if self.protocol == "apb3":
      out_string += "  // APB3 interface\n"
      out_string += "  input  logic [31:0] paddr_i,\n"
      out_string += "  input  logic        psel_i,\n"
      out_string += "  input  logic        penable_i,\n"
      out_string += "  input  logic        pwrite_i,\n"
      out_string += "  input  logic [31:0] pwdata_i,\n"
      out_string += "  output logic [31:0] prdata_o,\n"
      out_string += "  output logic        pready_o,\n"
      out_string += "  output logic        pslverr_o\n"
    ## old reg interface
    if self.protocol == "reg":
      out_string += "  // Bus Interface\n"
      out_string += "  input  reg_intf::reg_intf_req_a32_d32 req_i,\n"
      out_string += "  output reg_intf::reg_intf_resp_d32    resp_o\n"
    return out_string

  def gen_verilog_bus_defaults(self):
    out_string = "    // {} bus defaults\n".format(self.protocol)
    if self.protocol == "apb3":
      out_string += "    pready_o  = 1'b1; // slave is always ready\n"
      out_string += "    prdata_o  =   '0;\n"
      out_string += "    pslverr_o =   '0;\n"
    if self.protocol == "reg":
      out_string += "    resp_o.ready = 1'b1; // slave is always ready\n"
      out_string += "    resp_o.rdata =   '0;\n"
      out_string += "    resp_o.error =   '0;\n"
    out_string += "    // reg ports defaults\n"
    for entry in self.ports:
      out_string += entry.gen_defaults()
    return out_string

  def gen_verilog_bus_logic(self):
    out_string = "    // {} bus write logic\n".format(self.protocol)
    bus_out_signal = ""
    if self.protocol == "apb3":
      bus_out_signal = "pwdata_i"
      out_string += "    if (psel_i & penable_i) begin\n"
      out_string += "      if (pwrite_i) begin\n"
      out_string += "        unique case(paddr_i)\n"
    if self.protocol == "reg":
      bus_out_signal = "req_i.wdata"
      out_string += "    if (req_i.valid) begin\n"
      out_string += "      if (req_i.write) begin\n"
      out_string += "        unique case(req_i.addr)\n"

    for entry in self.addrmap:
      out_string += entry.gen_write_logic(bus_out_signal)

    bus_err_signal  = ""
    if self.protocol == "apb3":
      bus_err_signal = "pslverr_o"
    if self.protocol == "reg":
      bus_err_signal = "resp_o.error"

    out_string += "          default: begin \n"
    out_string += "            {} = 1'b1;\n".format(bus_err_signal)
    out_string += "          end\n"

    out_string += "        endcase\n"
    out_string += "      end else begin\n"

    bus_in_signal = ""
    if self.protocol == "apb3":
      bus_in_signal = "prdata_o"
      out_string += "        unique case(paddr_i)\n"
    if self.protocol == "reg":
      bus_in_signal = "resp_o.rdata"
      out_string += "        unique case(req_i.addr)\n"

    for entry in self.addrmap:
      out_string += entry.gen_read_logic(bus_in_signal)

    out_string += "          default: begin \n"
    out_string += "            {} = 1'b1;\n".format(bus_err_signal)
    out_string += "          end\n"

    out_string += "        endcase\n"
    out_string += "      end\n"
    out_string += "    end\n"
    return out_string

  def gen_verilog_regmapping(self):
    out_string  = "  // combinatorial register mux\n"
    out_string += "  always_comb begin : begin_gen_reg_mux_{}\n".format(self.name)
    out_string += self.gen_verilog_bus_defaults()
    out_string += self.gen_verilog_bus_logic()
    out_string += "  end : end_gen_reg_mux_{}".format(self.name)
    return out_string

  def gen_verilog_header(self):
    out_string  = "/*------------------------------------------------------------\n"
    out_string += "  modulename : {}\n".format(self.name)
    out_string += "  generated by {} on {} with {}\n\n".format(os.getlogin(), datetime.now().strftime("%d/%m/%Y %H:%M:%S"), __version__)
    out_string += "  description: {}\n".format(self.description)
    out_string += "------------------------------------------------------------*/\n\n"
    return out_string

  def gen_verilog_module(self):
    out_string  = "// !! Do not edit - auto-generated !!\n\n"
    out_string += self.gen_verilog_header()
    out_string += "module {}\n".format(self.name)
    out_string += self.gen_verilog_portlist()
    out_string += "\n"
    out_string += self.gen_verilog_regmapping()
    out_string += "\n"
    out_string += "endmodule\n"
    return out_string