#!/usr/bin/env python

import socket
import time

host = 'chal.2023.sunshinectf.games'
port =  23200
test_line =  '⇧⇧⇦⇦⇧⇦⇧⇨⇦⇦⇩⇧⇧⇧⇩⇦⇦⇦⇨⇧⇧⇦⇨⇩⇧⇧⇦⇨⇧⇧⇩⇧⇧⇦⇩⇨⇦⇨⇦⇦⇩⇨⇩⇧⇩⇩⇧⇧⇩⇩'

def xlate(self):
    resp = []
    for char in self:
        if char == '⇧':
            char = 'w'
            resp.append(char)
        if char == '⇦':
            char = 'a'
            resp.append(char)
        if char == '⇨':
            char = 'd'
            resp.append(char)
        if char == '⇩':
            char = 's'
            resp.append(char)

    #print("inp_line : %s" % self)
    new_line = ''.join(resp)
    #print('new_line : %s' % new_line)
    return(new_line)

#print(xlate(test_line))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print("RESP1: %s" % s.recv(500))
s.send(b'\r\n')
print("RESP2: %s" % s.recv(500).decode('utf-8'))

for _ in range(500):
    #print("Attempt: %s" % _)
    resp =  s.recv(200)
    resp = resp.decode('utf-8','ignore').strip('\n')
    resp = resp.strip('\r')
    if resp:
        print('%s , %s' % (str(_).rjust(3) , resp))
   
    if resp:
        answer = xlate(resp) 
        doit = s.send(answer.encode())
        s.send(b'\r\n')

'''

# extra because of blank lines i'm not catching, or something

415 , ⇩⇩⇨⇧⇦⇨⇩⇩⇧⇦⇦⇦⇦⇦⇨⇨⇩⇨⇦⇨⇦⇧⇩⇦⇧⇩⇨⇩⇧⇨⇦⇨⇧⇨⇦⇨⇦⇩⇧⇩⇧⇩⇨⇨⇧⇩⇧⇦⇨⇨
417 , ⇧⇦⇨⇨⇧⇦⇧⇧⇦⇦⇨⇦⇨⇨⇨⇦⇩⇨⇦⇦⇧⇧⇧⇨⇦⇧⇧⇧⇧⇩⇦⇩⇧⇩⇨⇧⇨⇨⇧⇧⇦⇩⇨⇨⇦⇧⇨⇩⇧⇦
418 , ⇦⇨⇧⇦⇦⇧⇧⇧⇨⇩⇩⇩⇩⇦⇨⇨⇩⇦⇧⇨⇧⇦⇧⇧⇩⇦⇩⇧⇩⇩⇧⇧⇨⇨⇦⇦⇧⇦⇦⇧⇦⇦⇦⇩⇨⇦⇨⇨⇩⇦
420 , YOU WIN!!!
Your prize is sun{d0_r0b0t5_kn0w_h0w_t0_d4nc3}

'''
