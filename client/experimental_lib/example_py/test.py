#!/usr/bin/env python3

import pm3
p=pm3.pm3("/dev/ttyACM0")
p.console("hw status")
print("Device:", p.name)
