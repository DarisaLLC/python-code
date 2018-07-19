#!/usr/bin/env python3

# The special variable __slots__ explicitly states which members the object is
# expected to have, which results in 1) faster memory access, 2) less memory.
# This prevents objects of the class from having arbirtarily defined attributes
# as an underlying __dict__ is no longer used.
