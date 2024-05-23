# Linux Internals MOOC
## Linux Internals


### Turing Machines
### Memory Management

Hardware architectures
![|375](Assets/media/Linux%20Internals%20MOOC/LinuxInternals-image-2024-04-15-122457.png)


Physical Memory and Single Address Space
- Simple and no abstractions in between
- Portable programs aren't easy
- Low security. pure chaos


Virtual Memory
 - Swap
 - Multi tasking and Context Switching
 - Memory Mapping
 - Secured Access at Hardware level

MMU and TLB
- Memory Management Unit and its Hardware implementation
- Translation Lookaside buffer. 

![|375](Assets/media/Linux%20Internals%20MOOC/LinuxInternals-image-2024-04-15-122859.png)


Kernel Virtual Memory
![|267](Assets/media/Linux%20Internals%20MOOC/LinuxInternals-image-2024-04-15-123002.png)


CONFIG_PAGE_OFFSET , control where the kernel memory ends and this split can be controlled at kernel compile time. 
Page Faults and Interrupts


Direct Memory Access 

IO

Shared Memory


### Process Management


Hardware and Drivers

Networking

Tracing and Tools




----
[Introduction — The Linux Kernel documentation](https://linux-kernel-labs.github.io/refs/heads/master/lectures/intro.html)
