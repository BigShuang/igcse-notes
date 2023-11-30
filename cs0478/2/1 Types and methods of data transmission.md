## 2.1 Types and methods of data transmission
### 1 Data packets
Data sent over long distances is usually broken up into data packets (sometimes called datagrams).
长距离发送的数据通常被分解为数据包（有时称为数据报）。

#### Packet structure
A typical packet is split up into:
- a packet header
- the payload
- a trailer.


#### packet header
- the IP address of the sending device
- the IP address of the receiving device
- the sequence number of the packet (this is to ensure that all the packets can 
be reassembled into the correct order once they reach the destination)
- packet size (this is to ensure the receiving station can check if all of the 
packets have arrived intact).

payload consists of the actual data being sent in the packet (this is usually about 64KiB).

trailer
some way of identifying the end of the packet; 
this is essential to allow each packet to be separated from each other as they travel from sending to receiving station

an error checking method; cyclic redundancy checks (CRCs) are used to check 
data packets

#### cyclic redundancy checks (CRCs) 
- this involves the sending computer adding up all the 1-bits in the payload and storing this as a hex value in the trailer before it is sent
这涉及发送计算机将有效负载中的所有 1 位相加，并在发送之前将其作为十六进制值存储在尾部中
- once the packet arrives, the receiving computer recalculates the number of 1-bits in the payload 
一旦数据包到达，接收计算机就会重新计算有效负载中 1 位的数量
- the computer then checks this value against the one sent in the trailer
然后计算机会根据预告片中发送的值检查该值
- if the two values match, then no transmission errors have occurred; otherwise the packet needs to be re-sent.
如果两个值匹配，则没有发生传输错误； 否则需要重新发送数据包。

#### Packet switching
分组交换

A router receives a data packet and, based on the information in the header, decides where to send it next.
路由器接收数据包，并根据标头中的信息决定下一步将其发送到何处。

Packet switching is a method of data transmission in which a message is broken up into a number of packets.

**steps**:
- data is broken into packets
- each packet will follow its own path (route)
- routers will determine the route of each packet
- routing selection depends on the number of packets waiting to be processed at each node
- selecting the shortest available route 
*the shortest possible path available is always selected – this may not always be the shortest path that could be taken, since certain parts of the route may be too busy or not suitable*
- packets may arrive out of order 
*unfortunately, packets can reach the destination in a different order to that in which they were sent*
- Once the last packet has arrived, packets are reordered
- If a packet is missing, it is requested again. 


#### The benefits of packet switching
- there is no need to tie up a single communication line
无需占用单一通信线路
- it is possible to overcome failed, busy or faulty lines by simply re-routing packets
只需重新路由数据包即可克服故障、繁忙或故障线路
- it is relatively easy to expand package usage
扩展包用途相对容易
- a high data transmission rate is possible.
高数据传输速率是可能的。

#### The drawbacks of packet switching

- packets can be lost and need to be re-sent
数据包可能会丢失并需要重新发送
- the method is more prone to errors with real-time streaming (for example, a live sporting event being transmitted over the internet)
该方法在实时流媒体中更容易出错（例如，通过互联网传输的现场体育赛事）
- there is a delay at the destination whilst the packets are being re-ordered
当数据包被重新排序时，目的地有延迟



bouncing may clogging up the system. 
To overcome this, a method called hopping is used. A hop number is added to the header of each packet, and this number is reduced by 1 every time it leaves a router

#### Activity 2.1

### 2 Data transmission
three factors need to be considered when transmitting data （usually considered by a communication protocol.）

- the direction of data transmission (for example, can data transmit in one direction only, or in both directions)
数据传输的方向（例如数据可以仅在一个方向上传输，还是可以在两个方向上传输）
- the method of transmission (for example, how many bits can be sent at the same time)
传输方法（例如，可以同时发送多少位）
- how will data be synchronised (that is, how to make sure the received data is in the correct order).
数据如何同步（即如何保证接收到的数据顺序正确）。

#### Simplex, half-duplex and full-duplex
Transmission mode 传输方式
单工、半双工和全双工

Simplex mode occurs when data can be sent in **ONE DIRECTION ONLY** (for example, from sender to receiver). 


Half-duplex mode occurs when data is sent in **BOTH DIRECTIONS but NOT AT THE SAME TIME** (for example, data can be sent from ‘A’ to ‘B’ and from ‘B’ to ‘A’ along the same transmission line, but they can’t both be done at the same time). 


Full-duplex mode occurs when data can be sent in **BOTH DIRECTIONS AT THE SAME TIME** (for example, data can be sent from ‘A’ to ‘B’ and from ‘B’ to ‘A’ along the same transmission line simultaneously).

#### Serial and parallel data transmission
Types of data transmission 数据传输类型
串行和并行数据传输

Serial data transmission occurs when data is sent **ONE BIT AT A TIME over a SINGLE WIRE/CHANNEL**. 
当数据通过单线/通道一次发送一位时，就会发生串行数据传输。
Bits are sent one after the other as a single stream.
 比特作为单个流被一个接一个地发送。

Parallel data transmission occurs when **SEVERAL BITS OF DATA** (usually one byte) are sent down **SEVERAL CHANNELS/WIRES** all at the same time. 
当几位数据（通常是一个字节）同时通过多个通道/线路发送时，就会发生并行数据传输。 
Each channel/wire transmits one bit
每个通道/线路传输一位

### 3 Universal serial bus (USB)

a form of serial data transmission. 
串行数据传输的一种形式。
USB is now the most common type of input/output port found on computers and has led to a standardisation method for the transfer of data  between devices and a computer. 
USB 现在是计算机上最常见的输入/输出端口类型，并导致了设备和计算机之间数据传输的标准化方法。

USB allows both half-duplex and full-duplex data transmission.
USB 允许半双工和全双工数据传输。


When a device is plugged into a computer using one of the USB ports:
当设备使用 USB 端口之一插入计算机时：

- the computer automatically detects that a device is present (this is due to a small change in the voltage on the data signal wires in the USB cable)
计算机自动检测到设备存在（这是由于 USB 电缆中数据信号线上的电压发生微小变化所致）
- the device is automatically recognised, and the appropriate device driver software is loaded up so that the computer and device can communicate effectively
自动识别设备，并加载相应的设备驱动软件，使计算机和设备能够有效通信
- if a new device is detected, the computer will look for the device driver that matches the device; if this is not available, the user is prompted to download the appropriate driver software (some systems do this automatically and the user will see a notice asking for permission to connect to the device website).
如果检测到新设备，计算机将寻找与该设备匹配的设备驱动程序； 如果此功能不可用，系统会提示用户下载适当的驱动程序软件（某些系统会自动执行此操作，并且用户将看到一条通知，要求获得连接到设备网站的权限）。

