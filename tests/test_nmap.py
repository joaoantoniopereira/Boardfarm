import random
import re

import rootfs_boot
from devices import board, lan, prompt

class TestNmap(rootfs_boot.RootFSBootTest):

    def boot(self, reflash=True):
        pass

    def runTest(self):
        lan.sendline('\nsudo nmap -p 20,21,22,23,53,80,443 192.168.1.254')
        lan.expect(r'20/tcp.*?filtered', timeout=100)
        lan.expect(r'21/tcp.*?open', timeout=100)
        lan.expect(r'22/tcp.*?open', timeout=100)
        lan.expect(r'23/tcp.*?open', timeout=100)
        lan.expect(r'53/tcp.*?open', timeout=100)
        lan.expect(r'80/tcp.*?open', timeout=100)
        lan.expect(r'443/tcp.*?open', timeout=100)
        lan.expect(prompt)