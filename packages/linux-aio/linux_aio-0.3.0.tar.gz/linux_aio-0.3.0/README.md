**\[english\]** | [\[한국어 (korean)\]](https://github.com/isac322/linux_aio/blob/master/README.kor.md)

# linux_aio: Python wrapper for [Linux Kernel AIO](http://lse.sourceforge.net/io/aio.html)

[![](https://img.shields.io/travis/com/isac322/linux_aio.svg?style=flat-square)](https://travis-ci.com/isac322/linux_aio)
[![](https://img.shields.io/pypi/v/linux_aio.svg?style=flat-square)](https://pypi.org/project/linux-aio/)
[![](https://img.shields.io/codecov/c/github/isac322/linux_aio.svg?style=flat-square)](https://codecov.io/gh/isac322/linux_aio)
[![](https://img.shields.io/pypi/implementation/linux_aio.svg?style=flat-square)](https://pypi.org/project/linux-aio/)
[![](https://img.shields.io/pypi/pyversions/linux_aio.svg?style=flat-square)](https://pypi.org/project/linux-aio/)
[![](https://img.shields.io/pypi/wheel/linux_aio.svg?style=flat-square)](https://pypi.org/project/linux-aio/)
[![](https://img.shields.io/pypi/l/linux_aio.svg?style=flat-square)](https://pypi.org/project/linux-aio/)

Python wrapper module that uses Linux Kernel AIO directly


## What is Linux Kernel AIO?

[Linux IO Models table](https://oxnz.github.io/2016/10/13/linux-aio/#io-models)

In summary, it allows non-blocking and asynchronous use of blocking IO operations such as [read(2)](http://man7.org/linux/man-pages/man2/read.2.html) and [write(2)](http://man7.org/linux/man-pages/man2/write.2.html).


### Related documents

- [Linux Asynchronous I/O](https://oxnz.github.io/2016/10/13/linux-aio/)
- [Linux Kernel AIO Design Notes](http://lse.sourceforge.net/io/aionotes.txt)
- [How to use the Linux AIO feature](https://github.com/littledan/linux-aio) (in C)


### **It is different from [POSIX AIO](http://man7.org/linux/man-pages/man7/aio.7.html)**

The POSIX AIO APIs have the `aio_` prefix, but the Linux Kernel AIO has the` io_` prefix.

There is already a POSIX AIO API for asynchronous I/O, but Linux implements it in glibc, a user-space library, which is supposed to use multi-threading internally.
So, as you can see from the experiment below, it's much worse than using the blocking IO API.


## Implementation & Structure

### Package `linux_aio.raw`

- [ctypes module](https://docs.python.org/3/library/ctypes.html) is used.
- It is defined to correspond `1:1` with the C header of Linux AIO.
	- Implemented 100% of the functionality when using C.
	- All the functions shown in the man page based on [Linux man pages (4.16)](http://man7.org/linux/man-pages/man2/io_submit.2.html), and all the functions added in [4.20.3 source code](https://elixir.bootlin.com/linux/v4.20.3/source/include/uapi/linux/aio_abi.h#L71), as far as I can find them. 
- If you know how to use the [ctypes module](https://docs.python.org/3/library/ctypes.html) to operate on pointers, you can also build other types of wrappers based on this package.
- It uses `syscall` for invoking ABI and [cffi](https://pypi.org/project/cffi/) for gathering [different syscall number by architecture](https://fedora.juszkiewicz.com.pl/syscalls.html) on module installation.
	- [refer the code](linux_aio/raw/syscall.py)
- [python stub](https://github.com/python/mypy/wiki/Creating-Stubs-For-Python-Modules) (`pyi` files - for type hint) are included.

### Package `linux_aio`

- It based on package `linux_aio.raw`.
- Unlike `linux_aio.raw`, it can be used without knowledge of `ctypes`
- Examples can be found in the code in the [test directory](test).


## Example

Examples can be found in the code in the [test directory](test).


## Notes & Limits

- Obviously available only on Linux
- Because it is a wrapper, it brings the constraints of Linux.
	- It can not be used for files used as a kernel interface. (e.g. `cgroup`)
	- [Sometimes it works as Blocking.](https://stackoverflow.com/questions/34572559/asynchronous-io-io-submit-latency-in-ubuntu-linux)
		- There are some things that have been solved through development after posting.
	- Some features are being added because they are still under development.
	- There are also some features that are not supported when the Linux version is low
		- You need to check [Linux man pages (4.16)](http://man7.org/linux/man-pages/man2/io_submit.2.html) and its related API documentation


## Evaluation

[Experiment script](https://gist.github.com/isac322/8606f5c464fa390cb88b47354981cdab) (requires python 3.7)

### Setup

- Distribution: Ubuntu Server 16.04.5 LTS
- Linux: 4.19.0
- CPU: 2-way Intel(R) Xeon(R) CPU E5-2683 v4 @ 2.10GHz
- MEM: total 64GB
- Storage: SK hynix SC300B SATA 512GB
- Python: 3.7.2 ([Ubuntu ppa](https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa))


- Attempts to read a total of `1000` times in` 1ms` intervals.
- The file size varies from `1KB` to` 100KB`, but it is small.
- Experiment with increasing the number of files read at the same time
- Because we have experimented with high-performance server, there may be larger performance differences when testing on a typical desktop.


### Comparison target

- [aiofiles](https://pypi.org/project/aiofiles/) - Uses Thread pool
- [aiofile](https://pypi.org/project/aiofile/) - Uses POSIX AIO
- [libaio](https://pypi.org/project/libaio/) - Uses [libaio](http://lse.sourceforge.net/io/aio.html)
- [python built-in open()](https://docs.python.org/3/library/functions.html#open)


**It is not a perfectly fair comparison.**

`aiofiles` and `aiofile` are libraries that support [asyncio](https://docs.python.org/3/library/asyncio.html). Since `open()` is blocking, there is a disadvantage that you can not do any other work while IO is going on. `libaio` and `linux_aio` are non-blocking, but must be polled.


### Results

**It may differ from environment to environment.**

#### Runtime

- Unit: second

| # of files 	|   1   	|   6   	|   12  	|   24  	|
|:---------:	|:-----:	|:-----:	|:-----:	|:-----:	|
|  aiofiles 	| 1.681 	| 3.318 	| 5.354 	| 9.768 	|
|  aiofile  	| 1.543 	| 1.958 	| 2.493 	| 3.737 	|
|   libaio  	| 1.311 	| 1.344 	| 1.362 	| 1.423 	|
|   open()  	| 1.252 	| 1.322 	| 1.375 	| 1.481 	|
| linux_aio 	| 1.305 	| 1.327 	| 1.353 	| 1.431 	|

#### Threads

| # of files 	|  1  	|  6  	|  12 	|  24 	|
|:---------:	|:---:	|:---:	|:---:	|:---:	|
|  aiofiles 	| 321 	| 321 	| 321 	| 321 	|
|  aiofile  	|   3 	|   8 	|  15 	|  26 	|
|   libaio  	|   1 	|   1 	|   1 	|   1 	|
|   open()  	|   1 	|   1 	|   1 	|   1 	|
| linux_aio 	|   1 	|   1 	|   1 	|   1 	|

#### Memory

- Physical memory (Virtual memory)

| # of files 	|       1       	|       6       	|       12      	|       24      	|
|:---------:	|:--------------	|:--------------	|:--------------	|:--------------	|
|  aiofiles 	| 21MB (22.6GB) 	| 21MB (22.6GB) 	| 21MB (22.6GB) 	| 21MB (22.6GB) 	|
|  aiofile  	|  17MB (258MB) 	|  17MB (654MB) 	| 17MB (1080MB) 	| 18MB (1949MB) 	|
|   libaio  	|   17MB (76MB) 	|   17MB (76MB) 	|   17MB (76MB) 	|   17MB (76MB) 	|
|   open()  	|   17MB (76MB) 	|   17MB (76MB) 	|   17MB (76MB) 	|   17MB (76MB) 	|
| linux_aio 	|   17MB (76MB) 	|   17MB (76MB) 	|   17MB (76MB) 	|   17MB (76MB) 	|

#### CPU Utilization

| # of files 	|   1   	|   6   	|   12   	|   24   	|
|:---------:	|------:	|------:	|-------:	|-------:	|
|  aiofiles 	| 42.8% 	| 85.0% 	| 102.2% 	| 113.2% 	|
|  aiofile  	| 31.4% 	| 52.4% 	|  67.0% 	|  84.0% 	|
|   libaio  	| 14.0% 	| 16.0% 	|  17.2% 	|  20.6% 	|
|   open()  	| 13.4% 	| 17.6% 	|  21.0% 	|  26.2% 	|
| linux_aio 	| 13.0% 	| 15.0% 	|  16.0% 	|  21.0% 	|