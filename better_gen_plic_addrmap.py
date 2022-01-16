#!/usr/bin/env python3
# Copyright 2019 ETH Zurich and University of Bologna.
# SPDX-License-Identifier: Apache-2.0
import argparse
from RegGen import clog2, AddrMap, Access

MAX_DEVICES = 1023

#
# Generate PLIC address map
#
if __name__ == "__main__":
  # Parse the command line arguments.
  parser = argparse.ArgumentParser()
  parser.add_argument("-t", "--nr_targets", metavar="NrTargets", help="number of targets (default 2)", default=2)
  parser.add_argument("-s", "--nr_sources", metavar="NrSources", help="number of sources (default 30)", default=30)
  parser.add_argument("-p", "--max_priority", metavar="MaxPriority", help="maximum number of priority (default 7)", default=7)
  parser.add_argument("--apb3", help="generate reg map with apb3 interface instead", default=False, action='store_true')
  args = parser.parse_args()

  plic_base = 0xC000000

  if args.nr_targets:
    nr_target = int(args.nr_targets)

  if args.nr_sources:
    nr_src = int(args.nr_sources)

  if args.max_priority:
    max_prio = int(args.max_priority)

  modulename = "plic_regs"
  bustype = "reg" # default bus type is left reg to not break compatibility
  if args.apb3:
    bustype = "apb3"
    modulename = "apb_plic_regs"


  priority_width = clog2(max_prio + 1)
  # interrupt source 0 is reserved, so add another source
  nr_src_eff = nr_src + 1
  source_width = clog2(nr_src_eff)
  addrmap = AddrMap(modulename, "PLIC Address Map", protocol=bustype)

  #assert nr_src <= 31, "Not more than 31 interrupt sources are supported at the moment"
  assert nr_target <= MAX_DEVICES, "Maximum allowed targets are {}".format(MAX_DEVICES)

  priorityBase = plic_base + 0x0
  enableBase = plic_base + 0x2000
  hartBase = plic_base + 0x200000

  def pendingAddr(i):
    return plic_base + 0x1000

  def enableOffset(i):
   return i * int(((MAX_DEVICES+7)/8))

  def hartOffset(i):
    return i * 0x1000

  def priorityAddr(i):
    return priorityBase + i * 4

  def enableAddr(i):
    return enableOffset(i) + enableBase

  def hartAddr(i):
    return hartOffset(i) + hartBase

  def hartCC(i):
    return hartAddr(i) + 4

  # add priority fields
  #addrmap.addEntries(nr_src_eff, priorityAddr, "prio", "source {} priority", Access.RW, priority_width)
  addrmap.newRegPort("prio", priorityAddr(0), priority_width, Access.RW, "source priority", nr_src_eff, 4)
  # pending array
  #addrmap.addEntry(pendingAddr, "ip", "pending array", Access.RO, nr_src_eff)
  addrmap.newRegPort("ip", pendingAddr(0), nr_src_eff, Access.RO, "pending array")
  # # generate per target interrupt enables
  #addrmap.addEntries(nr_target, enableAddr,  "Target {} interrupt enable", Access.RW, nr_src_eff)
  addrmap.newRegPort("ie", enableAddr(0), nr_src_eff, Access.RW, "Target interrupt enable", nr_target, enableOffset(1))
  # # generate claim/complete registers + thresholds
  #addrmap.addEntries(nr_target, hartAddr, "threshold", "Hart {}  priority threshold", Access.RW, priority_width)
  addrmap.newRegPort("threshold", hartAddr(0), priority_width, Access.RW, "Hart priority threshold", nr_target, hartOffset(1))
  #addrmap.addEntries(nr_target, hartCC, "cc", "Hart {} claim/complete", Access.RW, source_width)
  addrmap.newRegPort("cc", hartCC(0), source_width, Access.RW, "Hart claim/complete", nr_target, 4)

  print(addrmap.gen_verilog_module())
