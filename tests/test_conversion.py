from xeddsa.implementations import XEdDSA25519

montgomery_private_keys = [
    b"\x40\x51\x7b\x8e\xdd\xae\x10\x26\xff\xdf\x20\x5f\x9e\xda\x15\xda" +
    b"\xcc\x0e\xf9\xec\xaf\x59\x80\x87\x08\xf9\x42\x2d\x30\xb4\x57\x4c",

    b"\x38\xb1\xc1\x42\x43\x97\xce\x59\x91\x37\x0b\x31\x52\xee\xed\x15" +
    b"\x5a\x45\x00\x51\x33\xb5\xb1\x2d\x6e\xe8\x2f\x17\x2f\x5f\x6f\x61",

    b"\x10\x59\xbc\xa7\xa6\x9f\x42\xbb\xa0\x28\x23\x44\x93\x4f\x08\x17" +
    b"\x97\xad\x20\xb2\x40\x4d\x31\x24\xd8\xe5\x51\x2e\x6b\x34\x97\x7e",

    b"\xc0\x1f\x46\x06\xdd\x56\x74\x7a\x3f\x89\x19\xe5\x6b\x73\x0f\x3c" +
    b"\x9a\xcb\x1a\x84\x67\xcc\x7a\x36\xcc\x5c\x5a\x0e\x74\x73\x25\x58",

    b"\x88\x33\xcd\xb7\x1a\x03\x0b\x49\x81\x05\xe1\xef\xc5\x3d\x52\x03" +
    b"\x1b\x01\xd0\x57\x7d\xfe\x39\xcc\x3c\x03\x45\x4c\x66\xfb\xca\x4c",

    b"\x38\x49\x45\x15\xbc\xd3\x80\xb1\x6a\xf9\xb0\x59\x57\x7b\xdb\x61" +
    b"\x84\x31\x01\xe1\x02\xea\x5e\xc6\xf1\xfa\x42\xf5\x72\x71\xfa\x51",

    b"\x68\x31\x02\x80\x25\x81\x63\xd7\x11\xf3\x72\xed\x6a\x9e\x2f\x69" +
    b"\x60\x27\x23\xb4\xe3\x73\x87\x52\x5d\xc4\xea\x8e\x05\xaa\xbf\x5a",

    b"\x20\x7f\x7c\x95\xdd\xd2\x61\xa9\x83\x84\xf7\xea\xa7\xd0\x5e\xec" +
    b"\x95\x1b\x0b\x3e\xf8\x78\x8e\x6f\x2f\x6b\x4a\x85\xee\x18\xc1\x6a",

    b"\x90\xa1\x14\x4a\x23\x33\xb2\x08\x03\x02\xdb\x36\xe6\xf9\xdc\x19" +
    b"\xd3\x0f\x4f\x96\x99\xcc\x23\xf0\xe4\xc6\x36\x21\x8e\xe6\x34\x48",

    b"\xa0\x0d\xd5\x81\x3f\x14\x47\x43\x17\x03\x5b\xa3\x9c\xbb\xdb\xfe" +
    b"\x81\x3c\x79\x25\x53\xf2\xd1\x5b\x51\xd0\x82\x87\x5c\xc0\x08\x54",
]

montgomery_public_keys = list(map(
    XEdDSA25519.mont_pub_from_mont_priv,
    montgomery_private_keys
))

twisted_edwards_private_keys = [
    b"\x40\x51\x7b\x8e\xdd\xae\x10\x26\xff\xdf\x20\x5f\x9e\xda\x15\xda" +
    b"\xcc\x0e\xf9\xec\xaf\x59\x80\x87\x08\xf9\x42\x2d\x30\xb4\x57\x4c",

    b"\x38\xb1\xc1\x42\x43\x97\xce\x59\x91\x37\x0b\x31\x52\xee\xed\x15" +
    b"\x5a\x45\x00\x51\x33\xb5\xb1\x2d\x6e\xe8\x2f\x17\x2f\x5f\x6f\x61",

    b"\x58\x46\xf2\x3f\x2c\x79\x50\x05\x12\xbe\x99\xd3\x61\x7f\xef\x8f" +
    b"\x69\x52\xdf\x4d\xbf\xb2\xce\xdb\x27\x1a\xae\xd1\x94\xcb\x68\x01",

    b"\xce\xd7\x7c\x27\xc1\xfb\xf9\x95\xc6\x23\xb4\xec\xcb\x67\x2a\x41" +
    b"\x66\x34\xe5\x7b\x98\x33\x85\xc9\x33\xa3\xa5\xf1\x8b\x8c\xda\x07",

    b"\x88\x33\xcd\xb7\x1a\x03\x0b\x49\x81\x05\xe1\xef\xc5\x3d\x52\x03" +
    b"\x1b\x01\xd0\x57\x7d\xfe\x39\xcc\x3c\x03\x45\x4c\x66\xfb\xca\x4c",

    b"\x56\xae\x7d\x18\xe2\x7e\xed\x5e\x9b\xb3\x1c\x78\xe0\x5f\x5e\x1b" +
    b"\x7c\xce\xfe\x1e\xfd\x15\xa1\x39\x0e\x05\xbd\x0a\x8d\x8e\x05\x0e",

    b"\x26\xc6\xc0\xad\x78\xd1\x0a\x39\xf4\xb9\x5a\xe4\xcc\x3c\x0a\x14" +
    b"\xa0\xd8\xdc\x4b\x1c\x8c\x78\xad\xa2\x3b\x15\x71\xfa\x55\x40\x05",

    b"\x5b\x4c\x3c\xf5\xda\xe2\x1e\xbf\x58\xc5\xcd\x89\x6e\x04\xba\xa5" +
    b"\x6a\xe4\xf4\xc1\x07\x87\x71\x90\xd0\x94\xb5\x7a\x11\xe7\x3e\x05",

    b"\x90\xa1\x14\x4a\x23\x33\xb2\x08\x03\x02\xdb\x36\xe6\xf9\xdc\x19" +
    b"\xd3\x0f\x4f\x96\x99\xcc\x23\xf0\xe4\xc6\x36\x21\x8e\xe6\x34\x48",

    b"\xee\xe9\xed\xab\x5e\x3e\x27\xcd\xee\xa9\x72\x2e\x9b\x1f\x5e\x7e" +
    b"\x7e\xc3\x86\xda\xac\x0d\x2e\xa4\xae\x2f\x7d\x78\xa3\x3f\xf7\x0b",
]

twisted_edwards_public_keys = [
    b"\x19\x9b\xa1\x30\x1e\xb5\x89\x4d\x8c\x7c\x02\xa0\xb7\xe2\x21\x9f" +
    b"\xea\x8d\x32\x70\xd0\x4c\x21\xf6\x95\x09\x9e\x73\x94\xa7\x54\x38",

    b"\x5f\xad\xfe\x14\xed\xfc\x3f\x0d\xd5\xc7\xa2\x22\xb2\xfd\x67\x46" +
    b"\x32\xf1\xd3\xaf\x99\x4d\xfe\xa9\x72\x10\xa4\xe6\x46\x0a\x37\x3f",

    b"\x7b\x78\x2a\x6d\xa7\x74\x52\x4d\x85\x54\xc9\xb8\x2c\xfe\x29\x55" +
    b"\xd5\x84\x4e\x24\x4f\xd8\xcd\xdc\x29\xec\xd0\x26\xd3\x61\xf7\x29",

    b"\x55\x82\xf5\x4f\xf8\x1c\xb0\x56\xc5\xf0\xc1\xee\x42\x8e\x92\x8d" +
    b"\xa1\x6e\x54\xfa\x89\x16\xd0\x48\x0f\x98\xd2\x50\x42\x32\x8f\x30",

    b"\xee\xa6\x1a\xf2\xa7\xd9\x81\x89\xe2\xdd\x16\x75\x1d\x32\xc5\xc6" +
    b"\x15\x77\xb1\x57\x39\xc7\xe7\x33\x2d\xba\x68\x19\x2b\xa6\x3f\x06",

    b"\xe8\x3d\xed\x4a\x59\x84\x45\xb7\x06\xc9\x8c\x78\xc8\xe6\xcd\x08" +
    b"\x9e\xe1\xa5\x0e\x67\xfb\xec\x62\xbe\x01\x9e\x00\xeb\x7e\x8c\x35",

    b"\x80\xc7\xef\x07\x1d\xc1\x27\x85\x33\x28\xa0\x21\xf1\xb2\x29\x94" +
    b"\x18\xaa\x7b\x21\xb8\x36\x87\x47\xbf\xe8\x23\xae\x10\x2b\x0a\x12",

    b"\xa5\x7f\x86\xbe\xbb\xd4\x5a\x50\xa0\x7a\xa1\x3c\x87\x16\x05\x9c" +
    b"\xc7\x31\xfd\x9a\x3b\x74\x68\x6e\xb8\x4c\x0e\xce\x06\x27\x00\x6c",

    b"\xa5\xd1\xcf\xc0\xaa\xb6\x8f\xe2\x67\xf9\xbb\x77\xc3\x67\x0c\x25" +
    b"\x1a\xbb\xcb\x66\x6a\xed\xee\x72\x92\xe4\xe5\x43\x17\x18\x93\x4f",

    b"\x18\x48\x13\x61\xbd\x42\x84\xe4\x7f\x75\xf1\xe9\x9d\x89\xfd\x2e" +
    b"\x4f\xe8\xfc\xe0\x97\x0d\xcb\x24\xad\xb6\xbe\xb3\xe1\xcb\xfd\x4d",
]

def test_conversion():
    assert (len(montgomery_private_keys)      ==
            len(montgomery_public_keys)       ==
            len(twisted_edwards_private_keys) ==
            len(twisted_edwards_public_keys))

    for i in range(len(montgomery_private_keys)):
        mont_priv      = montgomery_private_keys[i]
        mont_pub       = montgomery_public_keys[i]
        wanted_ed_priv = twisted_edwards_private_keys[i]
        wanted_ed_pub  = twisted_edwards_public_keys[i]

        converted_ed_priv, converted_ed_pub = XEdDSA25519.mont_priv_to_ed_pair(mont_priv)

        assert converted_ed_priv == wanted_ed_priv
        assert converted_ed_pub  == wanted_ed_pub

        converted_ed_pub = XEdDSA25519.mont_pub_to_ed_pub(mont_pub)

        assert converted_ed_pub == wanted_ed_pub
