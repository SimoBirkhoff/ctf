from z3 import *

x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23 = BitVecs("x0 x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15 x16 x17 x18 x19 x20 x21 x22 x23",8)

x=Solver()


x.add( (x20 ^ 43) == x7 )
x.add( (x21 - x3)  == -20 )
x.add( (x2 >> 222 % 8) == 0 )
x.add( (x13 + 87) == 203 )
x.add( (x11 << 82 % 8) == 380 )
x.add( (x7 >> x17 % 8) == 5 )
x.add( (x6 ^ 83) == x14 )
x.add( (x8 - 63) == 59 )
x.add( (x5 << x9 % 8) == 392 )
x.add( (x16 - x7)  == 20 )
x.add( (x7 << x23 % 8) == 190 )
x.add( (x2 - x7)  == -43 )
x.add( (x21 - 131) == -36 )
x.add( (x2 ^ 71) == x3 )
x.add( (x0 + 208) == 307 )
x.add( (x13 << 64 % 8) == 116 )
x.add( (x20 & 69) == 68 )
x.add( (x8 & 21) == 16 )
x.add( (x12 - 116) == -21 )
x.add( (x4 >> 204 % 8) == 7 )
x.add( (x13 ^ 71) == 51 )
x.add( (x0 >> x0 % 8) == 12 )
x.add( (x10 ^ 243) == 172 )
x.add( (x8 & 172) == 40 )
x.add( (x16 + 40) == 155 )
x.add( (x22 & 29) == 24 )
x.add( (x9 + 39) == 90 )
x.add( (x5 - 71) == -22 )
x.add( (x19 << 194 % 8) == 456 )
x.add( (x20 >> 46 % 8) == 1 )
x.add( (x7 >> 121 % 8) == 47 )
x.add( (x1 + 232) == 340 )
x.add( (x3 >> 244 % 8) == 7 )
x.add( (x19 & 73) == 64 )
x.add( (x4 ^ 124) == 15 )
x.add( (x2 & x11) == 20 )
x.add( (x0 & x0) == 99 )
x.add( (x4 + x5)  == 164 )
x.add( (x15 << 30 % 8) == 6080 )
x.add( (x10 ^ 43) == x17 )
x.add( (x12 ^ 44) == x4 )
x.add( (x19 - x21)  == 19 )
x.add( (x12 - 210) == -115 )
x.add( (x12 - 71) == 24 )
x.add( (x15 >> 193 % 8) == 47 )
x.add( (x19 - 103) == 11 )
x.add( (x17 + x18)  == 168 )
x.add( (x22 ^ 78) == 116 )
x.add( (x23 & x21) == 9 )
x.add( (x6 << x19 % 8) == 396 )
x.add( (x3 + x7)  == 210 )
x.add( (x22 & 237) == 40 )
x.add( (x12 & 172) == 12 )
x.add( (x18 ^ 107) == x15 )
x.add( (x16 & 122) == 114 )
x.add( (x0 & 57) == 33 )
x.add( (x6 ^ 60) == x21 )
x.add( (x20 >> 96 % 8) == 116 )
x.add( (x19 + 194) == 308 )
x.add( (x12 << 16 % 8) == 95 )
x.add( (x2 ^ 206) == 250 )
x.add( (x23 ^ 238) == 199 )
x.add( (x10 << 40 % 8) == 95 )
x.add( (x22 & x9) == 50 )
x.add( (x3 + x2)  == 167 )
x.add( (x17 - x14)  == 68 )
x.add( (x21 + 112) == 207 )
x.add( (x19 ^ 45) == x10 )
x.add( (x12 << 2 % 8) == 380 )
x.add( (x6 & 64) == 64 )
x.add( (x12 & x22) == 26 )
x.add( (x7 << x19 % 8) == 380 )
x.add( (x4 ^ 0) == x4 )
x.add( (x20 ^ 78) == x22 )
x.add( (x6 ^ 229) == 134 )
x.add( (x12 - x7)  == 0 )
x.add( (x19 - x13)  == -2 )
x.add( (x14 >> 212 % 8) == 3 )
x.add( (x12 & 56) == 24 )
x.add( (x8 << x10 % 8) == 15616 )
x.add( (x20 ^ 98) == 22 )
x.add( (x6 >> x22 % 8) == 24 )
x.add( (x22 - x5)  == 9 )
x.add( (x7 << x22 % 8) == 380 )
x.add( (x22 - 153) == -95 )
x.add( (x16 + 3) == 118 )
x.add( (x23 ^ 29) == x18 )
x.add( (x23 + x14)  == 89 )
x.add( (x5 & x2) == 48 )
x.add( (x15 & 159) == 31 )
x.add( (x4 - 2) == 113 )
x.add( (x23 ^ 74) == x0 )
x.add( (x6 ^ 60) == x11)

x.check()
x.model()

l=[x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23]

flag = ''.join([chr(x.model()[i].as_long()) for i in l ])

print "shkCTF{%s}"%flag