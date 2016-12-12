import pexpect

class TelnetConnection():
    '''
    To use, set conn_cmd in your json to "cu -s <port_speed> -l <path_to_serialport>"
    and set connection_type to "local_serial"

    '''
    def __init__(self, device=None, conn_cmd=None, **kwargs):
        self.device = device
        self.conn_cmd = conn_cmd
        print kwargs
        self.username = kwargs['board_username']
        self.password = kwargs['board_password']

    def connect(self):
        pexpect.spawn.__init__(self.device,
                           command='/bin/bash',
                           args=['-c', self.conn_cmd])
        try:
            result = self.device.expect(["sername"])
            self.device.sendline(self.username + "\r")
            result = self.device.expect(["assword"])
            self.device.sendline(self.password + "\r")
        except pexpect.EOF as e:
            raise Exception("Board is in use (connection refused).")

    def close():
        self.device.sendline("exit")
