import six
import struct

from .multiaddr import Multiaddr


if hasattr(int, 'from_bytes'):
    def packed_net_bytes_to_int(b):
        """Convert the given big-endian byte-string to an int."""
        return int.from_bytes(b, byteorder='big')
else:  # PY2
    def packed_net_bytes_to_int(b):
        """Convert the given big-endian byte-string to an int."""
        return int(b.encode('hex'), 16)