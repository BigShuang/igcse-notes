## 1.2 Text, sound and images
### 1.2.1 Character sets – ASCII code and Unicode
American Standard Code for Information Interchange
美国标准信息交换码
use in communication systems and computer systems. 

The standard ASCII code character set consists of 7-bit codes (0 to 127 in denary or 00 to 7F in hexadecimal) that represent the letters, numbers and characters found on a standard keyboard, together with 32 control codes (that use codes 0 to 31 (denary)  or 00 to 19 (hexadecimal)).

标准 ASCII 代码字符集由代表标准键盘上的字母、数字和字符的 7 位代码（十进制的 0 到 127 或十六进制的 00 到 7F）以及 32 个控制代码（使用代码 0 到 31（十进制）或 00 到 19（十六进制））。


Unicode can represent all languages of the world, thus supporting many operating systems, search engines and internet browsers used globally. 
Unicode 可以代表世界上所有的语言，从而支持全球使用的许多操作系统、搜索引擎和互联网浏览器。


As can be seen in Table 1.2 and Figure 1.6, ASCII uses one byte to represent a character, whereas Unicode will support up to four bytes per character. 

- create a universal standard that covered all languages and all writing systems
创建涵盖所有语言和所有书写系统的通用标准
  
- produce a more efficient coding system than ASCII
产生比 ASCII 更有效的编码系统
  
- adopt uniform encoding where each character is encoded as 16-bit or 32-bit code
  采用统一编码，每个字符编码为16位或32位代码
- create unambiguous encoding where each 16-bit and 32-bit value always represents the same character
  创建明确的编码，其中每个 16 位和 32 位值始终表示相同的字符
- reserve part of the code for private use to enable a user to assign codes for  their own characters and symbols (useful for Chinese and Japanese character sets, for example)
保留部分代码供私人使用，以便用户能够为自己的字符和符号分配代码（例如，对于中文和日文字符集有用）

### 1.2.2 Representation of sound
vibration
`/vaɪˈbreɪʃn/`
振动;震动;抖动;颤动;(感情的)共鸣

- frequency
 频率
- wavelength
 波长
- amplitude
 振幅

Computers cannot work with analogue data, so sound waves need to be sampled in order to be stored in a computer. 
计算机无法处理模拟数据，因此需要对声波进行采样才能存储在计算机中。
Sampling means measuring the amplitude of the sound wave. 
采样意味着测量声波的振幅。

This is done using an analogue to digital converter (ADC). 
这是使用模数转换器 (ADC) 完成的。
#### sampling resolution
The number of bits per sample is known as the **sampling resolution** (also known as the bit depth). 
if 4 binary bits can be used to represent each amplitude value, the sampling resolution is 4 bits.
#### Sampling rate
**Sampling rate** is the number of sound samples taken per second. This is 
measured in hertz (Hz), where 1Hz means ‘one sample per second’.

#### how is sampling used to record a sound clip?
1. the amplitude of the sound wave is first determined at set time intervals (the  sampling rate)
根据采样率，确定每个时间戳的声波振幅
2. this gives an approximate representation of the sound wave
找到近似数量
3. each sample of the sound wave is then encoded as a series of binary digits.
  然后，声波的每个样本都被编码为一系列二进制数字。


#### benefits and drawbacks
The benefits and drawbacks of using a larger sampling resolution when recording sound

Benefits 
larger dynamic range
better sound quality 
less sound distortion 
更大的动态范围
更好的音质
声音失真较小


Drawbacks
produces larger file size
takes longer to transmit/download music files
requires greater processing power
产生更大的文件大小
传输/下载音乐文件需要更长的时间
需要更强的处理能力

> CDs have a 16-bit sampling resolution and a 44.1 kHz sample rate – that is 44 100 
samples every second. This gives high-quality sound reproduction.

### 1.2.3 Representation of (bitmap) images

Bitmap images are made up of pixels (picture elements); 
an image is made up of a two-dimensional matrix of pixels. 

Each pixel can be represented as a binary number, and so a bitmap image is stored in a computer as a series of binary numbers.


#### colour depth
The number of bits used to represent each colour is called the colour depth. 
用于表示每种颜色的位数称为颜色深度。

An 8 bit colour depth means that each pixel can be one of 256 colours
8 位颜色深度意味着每个像素可以是 256 种颜色之一


#### Image resolution
Image resolution refers to the number of pixels that make up an image