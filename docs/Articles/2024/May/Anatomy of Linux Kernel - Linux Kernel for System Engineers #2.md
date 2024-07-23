---
title: Linux Kernel Explained - Deep Dive Series for System Engineers
created: 2024-04-28 14:46
public: true
categories:
    - Engineering
tags:
    - series/bits-n-bytes
    - software_engineering/linux-internals
    - topic/deep-dives
topic:
    - linux
date: 2024-04-28
description:
    Deep dive into Linux Kernel for system engineers by @wiresurfer | Learn
    about BIOS, GRUB, Linux Kernel, Initramfs and Root file system.
---

# Linux Kernel Explained - Deep Dive Series for System Engineers

The Linux kernel is a monumental achievement in the world of open-source
software, driven by a passionate community of contributors.  
This collaborative effort has resulted in a powerful, versatile operating system
that powers an estimated 80-90% of the internet. From the smartphones in our
pockets to the vast cloud infrastructure, Linux is the backbone of many
technologies we rely on daily.

<!-- more -->

Linux is not just for servers and desktops. Here is a short list of places where
the Linux kernel is chugging along.

-   **Smartphones**: Android, the most widely used mobile operating system, is
    built on the Linux kernel.
-   **MacOS and iOS**: While MacOS is based on a different Unix variant (Loosely
    related FreeBSD), it shares many principles + components with Linux.
-   **Cloud Infrastructure**: Major cloud service providers like AWS, Google
    Cloud, and Azure rely heavily on Linux to power their data centers.
-   **IoT Devices**: From smart home devices to industrial sensors, many IoT
    devices run on Linux.
-   **Networking and Telecommunications**: Many telecom systems and every major
    ISP uses Linux in its networking stack. Your home router is probably running
    an embedded Linux kernel already
-   **Entertainment**: Streaming services, gaming platforms, and more use
    Linux-based servers to deliver content seamlessly.  
    .. and the list goes on and on ..

> Mankind's Achievement in Collaborative Development
>
> The success of the Linux kernel exemplifies human ingenuity and collaborative
> spirit. It showcases how collective effort and shared knowledge can create
> something that far surpasses individual contributions. As we progress into the
> future, the way we build the kernel also needs to scale to an every changing
> landscape of devices and services. A challenge indeed!
>
> ![Famous XKCD Strip. That tiny pillar was once Linus maintaining Linux Kernel. Thankfully he has more hands on deck today](Assets/media/Linux%20Kernel%20Explained%20-%20Deep%20Dive%20Series%20for%20System%20Engineers/Linux%20Kernel%20Explained%20-%20Deep%20Dive%20Series%20for%20System%20Engineers-image-2024-05-29-231847.png)

---

### Why write about the Linux Kernel?

**The Evolution of Programming Abstractions**

In the early days of computing, programmers worked close to the hardware, using
assembly languages or early high-level languages like Fortran.

As technology advanced and business needs grew, programming languages became
more abstract to accommodate a broader range of developers. This evolution
brought us C, C++, Java, and various scripting languages. Today, new programming
languages emerge regularly, each aiming to solve specific problems or improve
developer productivity. Abstractions gave us superpower, and now I see a lot of
engineers unaware of how this machine works.

We are at a point in human learning, where the abstractions are too much to
unwrap. Its of utmost importance that we write down,

![Another XKCD strip. Oh well, that's what abstractions resulted in. Cat memes! |367](Assets/media/Linux%20Kernel%20Explained%20-%20Deep%20Dive%20Series%20for%20System%20Engineers/Linux%20Kernel%20Explained%20-%20Deep%20Dive%20Series%20for%20System%20Engineers-image-2024-05-29-232015.png)

**The Linux Kernel as a Foundational Technology**

Despite the rapid pace of technological advancement, some foundational
technologies remain constant. The Linux kernel is one such pillar, integral to
many cutting-edge fields. Rarely is there a skill more transferable than knowing
about the internals of the kernel. It's useful in space tech, robotics,
manufacturing, industrial automation, cloud, networking, energy, adtech,
streaming and communications.

**Encouragement for Developers**

Understanding the Linux kernel is a valuable skill for both new and seasoned
developers. It provides deep insights into operating system design and
functionality. By exploring Linux, developers can gain a "superpower" that
enhances their ability to innovate and solve complex problems.

For those looking to delve deeper, numerous resources and guided curriculums are
available, crafted by experts in the field.  
I will try to curate a journey which will help you get your Aha moment and get a
glimpse into the under belly of your machine.

![XKCD telling us, we just need the hardware, Neuralink took this seriously?](Assets/media/Linux%20Kernel%20Explained%20-%20Deep%20Dive%20Series%20for%20System%20Engineers/Linux%20Kernel%20Explained%20-%20Deep%20Dive%20Series%20for%20System%20Engineers-image-2024-05-29-232317.png)

---

## Learning Path

1. Booting Up Linux Kernel
2. Understanding how Linux Kernel is organized
    1. CPU, Scheduling and Timers
    2. Memory Layout and Management
    3. Device and Drivers
    4. Human Interface Devices
        1. HID
        2. Linux Graphics Stack
        3. Sound Subsystem
    5. Storage Interface and Virtual File System
    6. Networking Interface
    7. Inter Process Communication
3. Writing your first kernel modules
4. Linux kernel development workflow
5. eBPF: Advanced tips and tricks for debugging, networking and more.

## Booting up Linux Kernel

Its always important to know what happens before Linux kernel boots up. This
foundation would help you make heads and tails of your hardware and never be
afraid of "Bare metal". In this day and age of layers of abstractions on which a
world of cloud infrastructure powers most of the internet, its important to know
how things work at its core.

I have written in some detail how
[Linux Kernel boots up in a separate post : Booting Linux Kernel](./Booting%20up%20Linux%20Kernel%20-%20Linux%20for%20Engineers%201.md)

## Linux Kernel Organization

When taken as a whole, Linux kernel source code is an intimidating pile of C
structs and pointer allocs which would give anyone the jeebies. To tame this
beast you have to understand its organization. Compartmentalization is the key
here. Its also important to note that different subsystems are written in a way
where they build on abstractions and don't step on the toes of other modules.

All this is to say, you don't need to tame the whole beast. You can take healthy
bite-sized chunks from the system of your choice and at the level of abstraction
you are comfortable with. That in itself would be a rewarding experience.

Take for eg. Networking. You could look at it bottom up. In which case you would
look at the world of `drivers/net`, `linux/netdevice.h` and probably the nitty
gritties of `struct skbuff`

Or maybe you are interested in just TCP-IP. In which case you would look at
`socker syscalls` -> `sys_socket` -> `address_families` ->
`net/protocols/tcp_prot`

I would write about the kernel organization in detail in an upcoming blog post.
For now I would leave you with this amazing diagram which was instrumental in my
exploration of the kernel's organization
<img src="https://raw.githubusercontent.com/makelinux/linux_kernel_map/main/LKM.svg" />

> You can open the SVG and zoom in/out or try the
> [interactive kernel map here](https://makelinux.github.io/kernel/map/)

### 1. CPU, Scheduling and Timers

The CPU, Scheduling, and Timers component is responsible for managing processor
resources and ensuring efficient execution of processes. It handles task
scheduling, context switching, and time-keeping operations.

a) This component manages CPU allocation among processes, implements scheduling
algorithms, and maintains system timers.

b) Key files and directories:

-   `/kernel/sched/`: Contains the core scheduler implementation
-   `/include/linux/sched.h`: Defines important scheduling structures
-   `/kernel/time/`: Implements various timekeeping functions

c) Important system calls:

-   `sched_yield()`: Voluntarily give up CPU time
-   `nice()`: Change process priority
-   `sched_setaffinity()`: Set CPU affinity for a process

d) Further reading:

-   [Linux Kernel Development](https://www.amazon.com/Linux-Kernel-Development-Robert-Love/dp/0672329468)
    by Robert Love
-   [Linux Kernel Source](https://github.com/torvalds/linux/tree/master/kernel/sched)

### 2. Memory Layout and Management

The Memory Layout and Management component is crucial for efficient utilization
of system memory. It handles memory allocation, deallocation, and protection
mechanisms.

a) This component manages physical and virtual memory, implements paging and
swapping, and provides memory protection.

b) Key files and directories:

-   `/mm/`: Contains memory management implementations
-   `/include/linux/mm.h`: Defines memory management structures
-   `/arch/x86/mm/`: Architecture-specific memory management (for x86)

c) Important system calls:

-   `mmap()`: Map files or devices into memory
-   `brk()`: Change the location of the program break
-   `mprotect()`: Set protection on a region of memory

d) Further reading:

-   [Understanding the Linux Virtual Memory Manager](https://www.kernel.org/doc/gorman/html/understand/)
    by Mel Gorman
-   [Linux Kernel Source - mm subsystem](https://github.com/torvalds/linux/tree/master/mm)

### 3. Device and Drivers

The Device and Drivers component provides a framework for managing hardware
devices and their corresponding software drivers.

a) This component facilitates communication between the kernel and hardware
devices, manages device initialization, and handles device-specific operations.

b) Key files and directories:

-   `/drivers/`: Contains various device drivers
-   `/include/linux/device.h`: Defines device and driver structures
-   `/include/linux/module.h`: Provides module-related definitions

c) Important system calls:

-   `ioctl()`: Device-specific operations
-   `open()`: Open a device file
-   `read()` and `write()`: Perform I/O operations on devices

d) Further reading:

-   [Linux Device Drivers](https://lwn.net/Kernel/LDD3/) by Jonathan Corbet,
    Alessandro Rubini, and Greg Kroah-Hartman
-   [Linux Kernel Source - drivers](https://github.com/torvalds/linux/tree/master/drivers)

### 4. Human Interface Devices

#### 4.1 HID (Human Interface Device)

The HID subsystem manages input devices such as keyboards, mice, and game
controllers.

a) This component provides a unified interface for various input devices,
handling device detection, input event processing, and device-specific features.

b) Key files and directories:

-   `/drivers/hid/`: Contains HID driver implementations
-   `/include/linux/hid.h`: Defines HID-related structures and functions

c) Important system calls:

-   `read()`: Read input events from HID devices
-   `ioctl()`: Perform device-specific operations on HID devices

d) Further reading:

-   [Linux Input Subsystem](https://www.kernel.org/doc/html/latest/input/input_uapi.html)
    documentation
-   [Linux Kernel Source - HID drivers](https://github.com/torvalds/linux/tree/master/drivers/hid)

#### 4.2 Linux Graphics Stack

The Linux Graphics Stack manages display output, rendering, and GPU
interactions.

a) This component handles graphics rendering, display management, and GPU
acceleration.

b) Key files and directories:

-   `/drivers/gpu/`: Contains GPU driver implementations
-   `/include/drm/`: Defines Direct Rendering Manager (DRM) structures and
    functions

c) Important system calls:

-   `ioctl()`: Used extensively for graphics operations
-   `mmap()`: Map video memory into user space

d) Further reading:

-   [Linux GPU Driver Developer's Guide](https://www.kernel.org/doc/html/latest/gpu/index.html)
-   [Linux Kernel Source - GPU drivers](https://github.com/torvalds/linux/tree/master/drivers/gpu)

#### 4.3 Sound Subsystem

The Sound Subsystem manages audio devices and sound processing.

a) This component handles audio device drivers, sound mixing, and audio
processing.

b) Key files and directories:

-   `/sound/`: Contains ALSA (Advanced Linux Sound Architecture) implementations
-   `/include/sound/`: Defines sound-related structures and functions

c) Important system calls:

-   `ioctl()`: Used for various audio operations
-   `read()` and `write()`: Perform I/O on audio devices

d) Further reading:

-   [ALSA Project Documentation](https://www.alsa-project.org/wiki/Main_Page)
-   [Linux Kernel Source - sound](https://github.com/torvalds/linux/tree/master/sound)

### 5. Storage Interface and Virtual File System

The Storage Interface and Virtual File System (VFS) component provides a unified
interface for various file systems and storage devices.

a) This component manages file system operations, provides a common API for
different file systems, and handles storage device interactions.

b) Key files and directories:

-   `/fs/`: Contains implementations of various file systems
-   `/include/linux/fs.h`: Defines file system-related structures and functions
-   `/block/`: Implements block device drivers

c) Important system calls:

-   `open()`, `read()`, `write()`, `close()`: Basic file operations
-   `mount()`: Mount a file system
-   `stat()`: Get file status

d) Further reading:

-   [Linux File Systems](https://www.kernel.org/doc/html/latest/filesystems/index.html)
    documentation
-   [Linux Kernel Source - fs](https://github.com/torvalds/linux/tree/master/fs)

### 6. Networking Interface

The Networking Interface component manages network communications and protocols.

a) This component handles network device drivers, protocol implementations, and
network stack operations.

b) Key files and directories:

-   `/net/`: Contains networking subsystem implementations
-   `/include/net/`: Defines networking-related structures and functions
-   `/drivers/net/`: Implements network device drivers

c) Important system calls:

-   `socket()`: Create a network socket
-   `connect()`, `bind()`, `listen()`, `accept()`: Manage network connections
-   `send()`, `recv()`: Send and receive data over network

d) Further reading:

-   [Linux Networking Documentation](https://www.kernel.org/doc/html/latest/networking/index.html)
-   [Linux Kernel Source - net](https://github.com/torvalds/linux/tree/master/net)

### 7. Inter Process Communication

The Inter Process Communication (IPC) component facilitates communication
between different processes.

a) This component provides mechanisms for processes to exchange data and
synchronize their actions.

b) Key files and directories:

-   `/ipc/`: Contains IPC mechanism implementations
-   `/include/linux/ipc.h`: Defines IPC-related structures and functions

c) Important system calls:

-   `pipe()`: Create a pipe for communication
-   `msgget()`, `msgsnd()`, `msgrcv()`: Message queue operations
-   `semget()`, `semop()`: Semaphore operations
-   `shmget()`, `shmat()`, `shmdt()`: Shared memory operations

i) Further reading:

-   [Linux IPC Mechanisms](https://www.kernel.org/doc/html/latest/admin-guide/sysctl/kernel.html#ipc-inter-process-communication)
-   [Linux Kernel Source - ipc](https://github.com/torvalds/linux/tree/master/ipc)

---

## Writing Your First Kernel Module

Kernel modules are pieces of code that can be loaded and unloaded into the
kernel upon demand. They extend the functionality of the kernel without the need
to reboot the system. Let's walk through creating a simple "Hello World" kernel
module.

### Step 1: Set up the development environment

First, ensure you have the necessary tools installed. Run the following
commands:

```bash
# Update package list
sudo apt update

# Install essential tools for kernel development
sudo apt install build-essential linux-headers-$(uname -r)
```

This script updates your package list and installs the build-essential package
(which includes gcc, make, and other necessary tools) and the Linux kernel
headers for your current kernel version.

### Step 2: Create the module source file

Create a new file named `hello_world.c` with the following content:

```c
#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Your Name");
MODULE_DESCRIPTION("A simple Hello World module");
MODULE_VERSION("0.1");

static int __init hello_world_init(void) {
    printk(KERN_INFO "Hello, World!\n");
    return 0;
}

static void __exit hello_world_exit(void) {
    printk(KERN_INFO "Goodbye, World!\n");
}

module_init(hello_world_init);
module_exit(hello_world_exit);
```

This code defines a simple kernel module that prints "Hello, World!" when loaded
and "Goodbye, World!" when unloaded.

### Step 3: Create a Makefile

Create a file named `Makefile` in the same directory with the following content:

```makefile
obj-m += hello_world.o

all:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
```

This Makefile tells the kernel build system how to compile your module.

### Step 4: Build the module

Run the following command to build your module:

```bash
make
```

This will compile your module and create a `hello_world.ko` file.

### Step 5: Load and test the module

Use the following commands to load, test, and unload your module:

```bash
# Load the module
sudo insmod hello_world.ko

# View kernel messages
sudo dmesg | tail

# Unload the module
sudo rmmod hello_world

# View kernel messages again
sudo dmesg | tail
```

These commands load your module, display kernel messages (which should include
your "Hello, World!" message), unload the module, and display kernel messages
again (which should now include your "Goodbye, World!" message).
