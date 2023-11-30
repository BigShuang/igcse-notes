## 2.2 Methods of error detection
错误检测方法
### 1 The need to check for errors

When data is transmitted, there is always a risk that it may be corrupted, lost or even gained.

Errors can occur during data transmission due to:

- interference (all types of cable can suffer from electrical interference, which can cause data to be corrupted or even lost)
干扰（所有类型的电缆都可能受到电气干扰，这可能导致数据损坏甚至丢失）
- problems during packet switching (this can lead to data loss – or it is even possible to gain data!)
数据包交换期间出现问题（这可能导致数据丢失 - 甚至有可能获得数据！）
- skewing of data (this occurs during parallel data transmission and can cause data corruption if the bits arrive out of synchronisation).
数据倾斜（这种情况发生在并行数据传输期间，如果位到达不同步，可能会导致数据损坏）。

There are a number of ways data can be checked for errors following 
transmission:
- parity checks
- checksum
- echo check.

### 2 Parity checks, checksum and echo checks
#### Parity checks
This method is based on the number of 1-bits in a byte of data.

The parity can be either called EVEN (that is, an even number of 1-bits in the byte) or ODD (that is, an odd number of 1-bits in the byte). 
奇偶校验可以称为偶（即，字节中具有偶数个 1 位）或奇（即，字节中具有奇数个 1 位）。

One of the bits in the byte (usually the most significant bit or left-most bit) is reserved for a parity bit. 
字节中的一位（通常是最高有效位或最左边的位）被保留用于奇偶校验位。

The parity bit is set according to whether the parity being used is even or odd. 
奇偶校验位根据所使用的奇偶校验是偶数还是奇数来设置。

使用偶数校验(even parity), 偶数个1， 校验位为0
使用奇数校验(odd parity), 奇数个1， 校验位为0

即1得个数和校验种类匹配，校验位为0


But
If two of the bits change value following data transmission, it may be impossible to locate the error using parity checking.

#### parity blocks
奇偶校验块
this method not only identifies that an error has occurred but also indicates where the error is.


#### Checksum

A checksum is a method used to check if data has been changed or corrupted following data transmission. 

Data is sent in blocks, and an additional value, called the checksum, is sent at the end of the block of data.

The checksum process is as follows:
- when a block of data is about to be transmitted, the checksum is calculated from the block of data
- the calculation is done using an agreed algorithm (this algorithm has been agreed by sender and receiver)
- the checksum is then transmitted with the block of data
- at the receiving end, the checksum is recalculated by the computer using the block of data (the agreed algorithm is used to find the checksum)
- the re-calculated checksum is then compared to the checksum sent with the data block
- if the two checksums are the same, then no transmission errors have occurred; otherwise a request is made to re-send the block of data.

#### Echo check

With echo check, when data is sent to another device, this data is sent back again to the sender. 

The sender’s computer compares the two sets of data to check if any errors occurred during the transmission process.

### 3 Check digits

A check digit is the final digit included in a code; it is calculated from all the other digits in the code.

They can usually detect the following types of error: 
他们通常可以检测到以下类型的错误：

- an incorrect digit entered, for example 5327 entered instead of 5307
输入的数字不正确，例如输入了 5327 而不是 5307
- transposition errors where two numbers have changed order, for example 5037 instead of 5307
两个数字改变顺序的换位错误，例如 5037 而不是 5307
- omitted or extra digits, for example 537 instead of 5307 or 53107 instead of 5307
省略或额外的数字，例如 537 代替 5307 或 53107 代替 5307
- phonetic errors, for example 13 (thirteen), instead of 30 (thirty).
语音错误，例如 13（十三），而不是 30（三十）。

#### ISBN 13
Calculation 1 – Generation of the check digit from the other 12 digits in a number
1. add all the odd numbered digits together
2. add all the even numbered digits together and multiply the result by 3
3. add the results from 1 and 2 together and divide by 10
4. take the remainder, if it is zero then use this value, otherwise subtract the remainder from 10 to find the check digit.

Calculation 2 – Re-calculation of the check digit from the thirteen-digit number 
(which now includes the check digit)

1. add all the odd numbered digits together, including the check digit
2. add all the even number of digits together and multiply the result by 3
3. add the results from 1 and 2 together and divide by 10
4. the number is correct if the remainder is zero.

#### Modulo-11

Calculation 1 – Generation of the check digit from the other digits in a number

The following algorithm generates the check digit from the other 7 digits:
1. each digit in the number is given a weighting of 8, 7, 6, 5, 4, 3 or 2 starting from the left (weightings start from 8 since the number will become eight-digit when the 
check digit is added)
2. the digit is multiplied by its weighting and then each value is added to make a total
3. the total is divided by 11
4. the remainder is then subtracted from 11 to find the check digit (note if the remainder is 10 then the check digit ‘X’ is used).


Calculation 2 – Re-calculation of the check digit from the eight-digit number (which now includes the check digit)

To check that the eight-digit number is correct, including its check digit, a similar process is followed:
1. each digit in the number is given a weighting of 8, 7, 6, 5, 4, 3, 2 or 1 starting from the left
2. the digit is multiplied by its weighting and then each value is added to make a total
3. the total is divided by 11
4. the number is correct if the remainder is zero

### 4 Automatic Repeat Requests (ARQs)

ARQ uses positive and negative **acknowledgements** (messages sent to the receiver indicating that data has/has not been received correctly) and **timeout** (this is the time interval allowed to elapse before an acknowledgement is received)

no error, send positive ack 
if an error, send negetive ack

if no acknowledgement of any type has been received by the sending device within this time limit, it automatically re-sends the data until a positive acknowledgement is received 