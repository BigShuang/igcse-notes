## 1.1 number systems
– how and why computers use binary to represent data
– the denary, binary and hexadecimal number systems
– converting numbers between denary, binary and hexadecimal
– how and why hexadecimal is used for data representation
– how to add two positive 8-bit numbers
– overflow when performing binary addition
– logical binary shifts on positive 8-bit integers
– two’s complement notation to represent positive and negative binary numbers

### 1.1.1 Binary represents data
**bit**: the basic computing element that is either 0 or 1, and is formed from the words Binary digit
比特, 二进制位

**how and why computers use binary to represent data**
This system is chosen because it only consists of 1s and 0s. Since computers contain millions and millions of tiny ‘switches’, which must be in the ON or OFF position, they can be represented by the binary system. 
A switch in the ON position is represented by 1; a switch in the OFF position is represented by 0.

### 1.1.2 Binary, denary and hexadecimal systems
binary: 二进制
denary: 十进制
hexadecimal: 十六进制

#### Converting from binary to denary
二的幂次表
$$
\begin{aligned}
2^{0}&=1 \\
2^{1}&=2 \\
2^{2}&=4 \\
2^{3}&=8 \\
2^{4}&=16 \\
2^{5}&=32 \\
2^{6}&=64 \\
2^{7}&=128 \\
2^{8}&=256 \\
2^{9}&=512 \\
2^{10}&=1024 \\
2^{11}&=2048 \\
2^{12}&=4096 \\
2^{13}&=8192 \\
2^{14}&=16384 \\
2^{15}&=32768 \\
\end{aligned}
$$


**Activity 1.1** 
`0 0 1 1 0 0 1 1`
$2^5 + 2^4 + 2^1 + 2^0 = 32 + 16 + 2 + 1 = 51$
`0 1 1 1 1 1 1 1`
$2^6 + 2^5 + 2^4 + 2^3 + 2^2 + 2^1 + 2^0 $
$=64 + 32 + 16 + 8 + 4 + 2 + 1 = 127 $

a. 51
b. 127
c. 153
d. 116
e. 255
f. 15
g. 143
h. 179
i. 112
j. 238
k. 443
l. 341
m. 4087
n. 1856
o. 2047
p. 3856
q. 4793
r. 35807
s. 4256
t. 65535

#### Converting from denary to binary
Method 1:
subtract the largest possible power of 2 and keep doing this until the value 0 is reached. 
减去 2 的最大可能幂并继续这样做，直到达到值 0。

Method 2:
This method involves successive division by 2.
Write the result of the division including the remainder.
keep dividing until the result is zero. 
Finally write down all the remainders in reverse order
该方法涉及连续除以 2。
写出除法的结果，包括余数。
继续除法，直到结果为零。
最后倒序写出所有余数

**Activity 1.2**
$41=32+8+1 = 2^5+2^3+2^0 = 101001$

$67 \div 2 = 33 \dots 1$
$33 \div 2 = 16 \dots 1$
$16 \div 2 = 8 \dots 0$
$8 \div 2 = 4 \dots 0$
$4 \div 2 = 2 \dots 0$
$2 \div 2 = 1 \dots 0$
$1 \div 2 = 0 \dots 1$

$67 = 1000011$

a. 41 = 101001
b. 67 = 1000011
c. 86 = 1010110
d. 100 = 1100100
e. 111 = 1101111
f. 127 = 1111111
g. 144 = 10010000
h. 189 = 10111101
i. 200 = 11001000
j. 255 = 11111111
k. 3300 = 110011011100
l. 888 = 1101111000
m. 4095 = 111111111111
n. 16400 = 10000000010000
o. 62307 = 1111000111010111

#### The hexadecimal system
十六进制

0123456789ABCDEF
A in hex = 10 in denary, B = 11, C = 12, D = 13, E = 14, F = 15.

$$
\begin{aligned}
16^{0}&=1 \\
16^{1}&=16 \\
16^{2}&=256 \\
16^{3}&=4096 \\
16^{4}&=65536 \\
\end{aligned}
$$


Table1.1 summarises the link between binary, 
hexadecimal and denary
#### Converting from binary to hexadecimal 

Starting from the right and moving left, 
split the binary number into groups of 4 bits. 
If the last group has less than 4 bits, then simply fill in with 0s from the left. 

#### Converting from hexadecimal to binary
take each hexadecimal digit and write down the 4-bit code which corresponds to the digit.

#### Convert hexadecimal numbers into denary
Take each of the hexadecimal digits and multiply it by the heading values.
Add all the resultant totals together to give the denary number.

#### Convert from denary to hexadecimal
successive division by 16 until the value “0” is reached.

### 1.1.3 Use of the hexadecimal system
a computer can only work with binary data.
computer scientists find hexadecimal to be more convenient to use.
计算机只能用二进制，计算机科学家则常用更方便的十六进制。


#### Error codes
#### Media Access Control (MAC) addresses
媒体访问控制 (MAC) 地址

Media Access Control (MAC) address refers to a number which uniquely identifies a device on a network. 

The MAC address refers to the network interface card (NIC) which is part of the device. 

A MAC address is usually made up of 48 bits which are shown as 6 groups of two hexadecimal digits (although 64-bit addresses also exist):
`NN – NN – NN – DD – DD – DD` or `NN:NN:NN:DD:DD:DD`

The first half (NN – NN – NN) is the identity number of the manufacturer of the device.
The second half (DD – DD – DD) is the serial number of the device. 

#### Internet Protocol (IP) addresses

Each device connected to a network is given an address known as the Internet 
Protocol (IP) address. 

An IPv4 address is a 32-bit number written in denary or hexadecimal form: e.g. 109.108.158.1 (or 77.76.9e.01 in hex). 
IPv4 has recently been improved upon by the adoption of IPv6. 
An IPv6 address is a 128-bit number broken down into 16-bit chunks, represented by a hexadecimal number. 

$2^4=32$
$2^6=128$

#### HyperText Mark-up Language (HTML) colour codes
HyperText Mark-up Language (HTML) 
超文本标记语言 (HTML)

All colours can be made up of different combinations of the three primary colours (red, green and blue). 
The different intensity of each colour (red, green and blue) is determined by its hexadecimal value. 
This means different hexadecimal values represent different colours. 


The # symbol always precedes hexadecimal values in HTML code. 
The colour codes are always six hexadecimal digits representing the red, green and blue components.
16 进制颜色

> https://www.sioe.cn/yingyong/yanse-rgb-16/



**Activity 1.7**
Red 53
Green 55
Blue 139
偏深蓝的一个颜色

十六进制颜色码
`#35358B`

### 1.1.4 Addition of binary numbers
carry 进位


overflow error

### 1.1.5 Logical binary shifts
Computers can carry out a logical shift on a sequence of binary numbers. The logical shift means moving the binary number to the left or to the right. 
计算机可以对一系列二进制数字进行逻辑移位。逻辑移位意味着将二进制数向左或向右移动。

Each shift left is equivalent to multiplying the binary number by 2 and each shift right is equivalent to dividing the binary number by 2.
每次左移相当于二进制数乘以2，每次右移相当于将二进制数除以2。


Losing 1 bit following a shift operation will cause an error.
This error is because we have exceeded the maximum number of left shifts possible using this register.

### 1.1.6 Two’s complement (binary numbers)
二进制补码（二进制数）

In two’s complement the left-most bit is changed to a negative value.
the new range of possible numbers is: 
−128 (10000000) to +127 (01111111).
#### Writing positive binary numbers in two’s complement format
for positive binary numbers, it is no different

#### Converting positive denary numbers to binary numbers
#### Converting positive binary numbers to positive denary numbers
#### Writing negative binary numbers converting to denary
`10010011`
$−128 + 16 + 2 + 1 = −109$

#### Converting negative denary numbers into binary numbers
##### Method 1

One method of finding the binary equivalent to −67 is to simply put 1s in their correct places
找到与 -67 等价的二进制数的一种方法是简单地将 1 放在正确的位置
$−128 + 32 + 16 + 8 + 4 + 1 = −67$
$128-67 = 61 = 32 + 16 + 8 + 4 + 1 $

##### Method 2
looking at the two binary numbers above, there is another possible way to find the binary representation of a negative denary number

互换01后最右边加1

first write the number as a positive binary value – in this case 67: 0 1 0 0 0 0 1 1
we then invert each binary value, which means swap the 1s and 0s around: 1 0 1 1 1 1 0 0
then add 1 to that number: 1
this gives us the binary for −67: 1 0 1 1 1 1 0 1