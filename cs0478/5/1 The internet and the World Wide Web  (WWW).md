## 1 The internet and the World Wide Web (WWW)

### 1 The differences between the internet and the World Wide Web (WWW)

The word internet comes from INTER connected NETwork, since it is basically a worldwide collection of interconnected networks. 
“互联网”一词来源于互联网络，因为它基本上是全球互联网络的集合。
The internet is actually a concept rather than something tangible (that is, something we can touch). 
互联网实际上是一个概念，而不是有形的东西（即我们可以触摸的东西）。
It relies on a physical infrastructure that allows networks and individual devices to connect to other networks and devices.
它依赖于允许网络和单个设备连接到其他网络和设备的物理基础设施。

The World Wide Web (WWW) is only a part of the internet that users can access using web browser software. 
万维网 (WWW) 只是互联网的一部分, 用户可以使用网络浏览器软件访问的。

The World Wide Web consists of a massive collection of web pages, and is based on the hypertext transfer protocol – see Section 5.1.3. 
万维网由大量网页组成，并且基于超文本传输协议 - 请参阅第 5.1.3 节。

Therefore, the World Wide Web is a way of accessing information using the internet; so the internet and the World Wide Web are actually quite different. 
因此，万维网是一种利用互联网获取信息的方式； 所以互联网和万维网实际上是完全不同的。


### 2 Uniform resource locators (URL)

Web browsers are software that allow users to access and display web pages on their device screens. 
Web 浏览器是允许用户访问并在其设备屏幕上显示网页的软件。

Browsers interpret hypertext mark-up language (HTML) sent from websites and produce the results on the user’s device. 
浏览器解释从网站发送的超文本标记语言 (HTML)，并在用户设备上生成结果。

Uniform resource locators (URLs) are text addresses used to access websites. 
统一资源定位符 (URL) 是用于访问网站的文本地址。

A URL is typed into a browser address bar using the following format:
使用以下格式将 URL 输入到浏览器地址栏中：
`protocol://website address/path/file name`

The **protocol** is usually either `http` or `https`.
The **website address** is:
- domain host (www),
- domain name (website name),
- domain type (.com, .org, .net, .gov, for example),
- and sometimes country code (.uk, .de, .cy, for example).

The **path** is the web page, but is often omitted and it then becomes the root directory of the website.
路径是网页，但经常被省略，它就成为网站的根目录。

The **file** name is the item on the web page. 

### 3 HTTP and HTTPS

Hypertext transfer protocol (http) is a set of rules that must be obeyed when transferring files across the internet. 
超文本传输协议 (http) 是通过 Internet 传输文件时必须遵守的一组规则。

When some form of security (for example, SSL or TLS) is used, then this changes to https (you will often see the green padlock in the status bar as well). 
当使用某种形式的安全性（例如 SSL 或 TLS）时，它会更改为 https（您通常也会在状态栏中看到绿色的挂锁）。

The ‘s’ stands for secure, and indicates a more secure way of sending and receiving data across a network (for example, the internet).
“s”代表安全，表示通过网络（例如互联网）发送和接收数据的更安全的方式。

### 4 Web browsers

Browsers are software that allow a user to access and display web pages on their device screens. 

Browsers interpret (translate) the HTML from websites and show the result of the translation; for example, videos, images/text and audio. 

Most browsers have the following features:
- they have a home page
- they can store a user’s favourite websites/web pages (referred to as bookmarks)
- they keep a history of websites visited by the user (user history)
- they have the ability to allow the user to navigate forwards and backwards through websites/web pages already opened
- many web pages can be open at the same time by using multiple tabs
- they make use of cookies 
- they make use of hyperlinks that allow navigation between websites and web pages; links can be opened in one of two ways: 
  either open in a new tab by using <ctrl> + <click> or 
  open in the same tab by simply clicking on the link 
- data is stored as a cache
- make use of JavaScript 
- they use an address bar

### 5 Retrieval and location of web pages
网页的检索和定位

All websites are written in HTML and hosted on a web server that has its own IP address. 

To retrieve pages from a website your browser needs to know this IP address.

#### Domain Name Server (DNS)
a system for finding IP addresses for a domain name given in a URL.
用于查找 URL 中给出的域名的 IP 地址的系统。

URLs and domain name servers eliminate the need for a user to memorise IP addresses. 
URL 和域名服务器消除了用户记住 IP 地址的需要。

The DNS process involves converting a URL (such as www.hoddereducation.co.uk) into an IP address the computer can understand (such as 107.162.140.19). 
DNS 过程涉及将 URL（例如 www.hoddereducation.co.uk）转换为计算机可以理解的 IP 地址（例如 107.162.140.19）。

The DNS process involves more than one server.
DNS 过程涉及多个服务器。

DNS servers contain a database of URLs with the matching IP addresses. 

### 6 Cookies

Cookies are small files or code stored on a user’s computer. 
Cookie 是存储在用户计算机上的小文件或代码。

They are sent by a web server to a browser on a user’s computer. 
它们由网络服务器发送到用户计算机上的浏览器。

> Each cookie is effectively a small look-up table containing pairs of (key, data) values, for example, (surname, Jones) (music, rock). 
每个 cookie 实际上都是一个小型查找表，其中包含成对的（键、数据）值，例如（姓氏、琼斯）（音乐、摇滚）。
> Every time a user visits a website, it checks if it has set cookies on their browser before. 
每次用户访问网站时，它都会检查该网站之前是否在其浏览器上设置了 cookie。 
> If so, the browser reads the cookie which holds key information on the user’s preferences such as language, currency and previous browsing activity. 
如果是这样，浏览器会读取 cookie，其中保存了有关用户偏好的关键信息，例如语言、货币和之前的浏览活动。
> Cookies allow user tracking and maintain user preferences.
Cookie 允许用户跟踪并维护用户偏好。
> Collected data can also be used to customise the web page for each individual user. 
收集的数据还可用于为每个用户定制网页。
> For example, if a user buys a book online, the cookies remember the type of book chosen by the user and the web page will then show a message such as “Customers who bought Hodder IGCSE ICT also bought Hodder IGCSE Computer Science”.
例如，如果用户在线购买一本书，cookie 会记住用户选择的书籍类型，然后网页将显示一条消息，例如“购买了 Hodder IGCSE ICT 的客户也购买了 Hodder IGCSE 计算机科学”。

There are two types of cookie:
- session cookie
- persistent (or permanent) cookie.
If a cookie doesn’t have an expiry date associated with it, it is always considered to be a session cookie.

#### Session cookies

This type of cookie is stored in temporary memory on the computer, doesn’t actually collect any information from the user’s computer and doesn’t personally identify a user. 
这种类型的 cookie 存储在计算机的临时内存中，实际上不会从用户的计算机收集任何信息，也不会识别用户的个人身份。

Hence, session cookies cease to exist on a user’s computer once the browser is closed or the website session is terminated.
因此，一旦浏览器关闭或网站会话终止，会话 cookie 将不再存在于用户的计算机上。

#### Persistent (permanent) cookies

Summary of the uses of (persistent) cookies:
- allow the website to remember users’ passwords, email addresses and invoice details, so they won’t have to insert all of this information every time they visit or every time they purchase something from that website
允许网站记住用户的密码、电子邮件地址和发票详细信息，这样他们就不必在每次访问或每次从该网站购买商品时都插入所有这些信息
- serve as a memory, enabling the website to recognise users every time they visit it
作为记忆，使网站能够在用户每次访问时识别出用户
- save users’ items in a virtual shopping basket/cart
将用户的物品保存在虚拟购物篮/购物车中
- track internet habits and users’ website histories or favourites/bookmarks 
跟踪互联网习惯和用户的网站历史记录或收藏夹/书签
- target users with advertising that matches their previous buying or surfing habits
通过与用户之前的购买或浏览习惯相匹配的广告来定位用户
- store users’ preferences (for example, recognise customised web pages)
存储用户的偏好（例如，识别定制网页）
- are used in online financial transactions
用于在线金融交易
- allow progress in online games and quizzes to be stored
允许存储在线游戏和测验的进度
- allow social networking sites to recognise certain preferences and browsing histories
允许社交网站识别某些偏好和浏览历史记录
- allow different languages to be used on the web pages automatically as soon as users log on.
允许用户登录后自动在网页上使用不同的语言。