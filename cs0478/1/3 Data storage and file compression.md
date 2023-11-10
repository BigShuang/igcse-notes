## 1.3 Data storage and file compression
### 1.3.1 Measurement of data storage
A bit is the basic unit of all computing memory storage terms and is either 1 or 0. 
位是所有计算内存存储术语的基本单位，要么是 1，要么是 0。

The word comes from binary digit. 
这个词来自二进制数字。

The byte is the smallest unit of memory in a computer. 
字节是计算机中存储的最小单位。

1 byte is 8 bits. A 4-bit number is called a nibble – half a byte. 
1 个字节是 8 位。 4 位数字称为半字节 - 半个字节。

`KMGTPE` - $2^{10}$

since memory size is actually measured in terms of powers of 2, 
another system has been adopted by the IEC (International Electrotechnical Commission) 
that is based on the binary system

### 1.3.2 Calculation of file size
The file size of an image
$\text{image resolution (in pixels)} \times \text{colour depth (in bits)}$
The size of a mono sound file
$\text{sample rate (in Hz)} \times \text{sample resolution (in bits)} \times \text{length of sample (in seconds)}$

*example 1*
colour depth of 32 bits
$\text{1 byte}= \text{8 bits}$
$\text{32 bits} = \text{4 bytes}$
$1080 = 5 \times 8 \times 27 = 5 \times 2^{3} \times 3^{3}$
一张照片的字节数量为
$1024 \times 1080 \times 4 = 2^{10} \times 5 \times 2^{3} \times 3^{3} \times 2^2$
$= 2^{15} \times 5 \times 3^{3}$

$\text{64 GiB} = 64 \times 2^{30} = 2^6 \times 2^{30} = 2^{36}$ $\text{bytes}$

所以64GB能容纳的照片数量为
$2^{36}  \div (2^{15} \times 5 \times 3^{3}) = 2^{21} \div 5 \div 3^{3} = 15534.459259$

### 1.3.3 Data compression
reasons to compression

- to save storage space on devices such as the hard disk drive/solid state drive
节省硬盘驱动器/固态驱动器等设备上的存储空间
  
- to reduce the time taken to stream a music or video file
减少流式传输音乐或视频文件所需的时间

- to reduce the time taken to upload, download or transfer a file across a network
减少通过网络上传、下载或传输文件所需的时间

- the download/upload process uses up network bandwidth – this is the maximum rate of transfer of data across a network, measured in bits per second. 
下载/上传过程会占用网络带宽——这是通过网络传输数据的最大速率，以每秒位数为单位。
This occurs whenever a file is downloaded, for example, from a server. 
每当下载文件时（例如从服务器下载文件）就会发生这种情况。
Compressed files contain fewer bits of data than uncompressed files and therefore use less bandwidth, which results in a faster data transfer rate.
压缩文件比未压缩文件包含更少的数据位，因此使用更少的带宽，从而实现更快的数据传输速率。
- reduced file size also reduces costs. For example, when using cloud storage, the cost is based on the size of the files stored. 
减小文件大小还可以降低成本。 例如，使用云存储时，成本取决于存储文件的大小。
Also an internet service provider (ISP) may charge a user based on the amount of data downloaded.
此外，互联网服务提供商 (ISP) 可能会根据下载的数据量向用户收费。

bandwidth – this is the maximum rate of transfer of data across a network, measured in bits per second. 
带宽

### 1.3.4 Lossy and lossless file compression
File compression can either be lossless or lossy.
文件压缩可以是无损的，也可以是有损的。

#### Lossy file compression
Common lossy file compression algorithms are:
- MPEG-3 (MP3) and MPEG-4 (MP4)
- JPEG.

#### Lossless file compression

**Run-length encoding (RLE)** can be used for lossless compression of a number of different file formats

- it is a form of lossless/reversible file compression
- it reduces the size of a string of adjacent, identical data (e.g. repeated colours in an image)
- a repeating string is encoded into two values:
  the first value represents the number of identical data items (e.g. 
characters) in the run.
the second value represents the code of the data item (such as ASCII code if it is a keyboard character)
- RLE is only effective where there is a long run of repeated units/bits.