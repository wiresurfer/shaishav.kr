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
description: Deep dive into Linux Kernel for system engineers by @wiresurfer | Learn about BIOS, GRUB, Linux Kernel, Initramfs and Root file system.
---
# Linux Kernel Explained - Deep Dive Series for System Engineers

The Linux kernel is a monumental achievement in the world of open-source software, driven by a passionate community of contributors.  
This collaborative effort has resulted in a powerful, versatile operating system that powers an estimated 80-90% of the internet. From the smartphones in our pockets to the vast cloud infrastructure, Linux is the backbone of many technologies we rely on daily.
<!-- more -->
Linux is not just for servers and desktops. Here is a short list of places where the Linux kernel is chugging along.

- **Smartphones**: Android, the most widely used mobile operating system, is built on the Linux kernel.
- **MacOS and iOS**: While MacOS is based on a different Unix variant (Loosely related FreeBSD), it shares many principles + components with Linux.
- **Cloud Infrastructure**: Major cloud service providers like AWS, Google Cloud, and Azure rely heavily on Linux to power their data centers.
- **IoT Devices**: From smart home devices to industrial sensors, many IoT devices run on Linux.
- **Networking and Telecommunications**: Many telecom systems and every major ISP uses Linux in its networking stack. Your home router is probably running an embedded Linux kernel already
- **Entertainment**: Streaming services, gaming platforms, and more use Linux-based servers to deliver content seamlessly.  
 .. and the list goes on and on ..

> Mankind's Achievement in Collaborative Development
> 
> The success of the Linux kernel exemplifies human ingenuity and collaborative spirit. It showcases how collective effort and shared knowledge can create something that far surpasses individual contributions. As we progress into the future, the way we build the kernel also needs to scale to an every changing landscape of devices and services. A challenge indeed! 
> 
> 
> ![Famous XKCD Strip. That tiny pillar was once Linus maintaining Linux Kernel. Thankfully he has more hands on deck today](Assets/media/Linux%20Kernel%20Explained%20-%20Deep%20Dive%20Series%20for%20System%20Engineers/Linux%20Kernel%20Explained%20-%20Deep%20Dive%20Series%20for%20System%20Engineers-image-2024-05-29-231847.png)

---

### Why write about the Linux Kernel?

**The Evolution of Programming Abstractions**

In the early days of computing, programmers worked close to the hardware, using assembly languages or early high-level languages like Fortran. 

As technology advanced and business needs grew, programming languages became more abstract to accommodate a broader range of developers. This evolution brought us C, C++, Java, and various scripting languages. Today, new programming languages emerge regularly, each aiming to solve specific problems or improve developer productivity. Abstractions gave us superpower, and now I see a lot of engineers unaware of how this machine works. 

We are at a point in human learning, where the abstractions are too much to unwrap. Its of utmost importance that we write down, 

![Another XKCD strip. Oh well, that's what abstractions resulted in. Cat memes! |367](Assets/media/Linux%20Kernel%20Explained%20-%20Deep%20Dive%20Series%20for%20System%20Engineers/Linux%20Kernel%20Explained%20-%20Deep%20Dive%20Series%20for%20System%20Engineers-image-2024-05-29-232015.png)

**The Linux Kernel as a Foundational Technology**

Despite the rapid pace of technological advancement, some foundational technologies remain constant. The Linux kernel is one such pillar, integral to many cutting-edge fields. Rarely is there a skill more transferable than knowing about the internals of the kernel. It's useful in space tech, robotics, manufacturing, industrial automation, cloud, networking, energy, adtech, streaming and communications. 

**Encouragement for Developers**

Understanding the Linux kernel is a valuable skill for both new and seasoned developers. It provides deep insights into operating system design and functionality. By exploring Linux, developers can gain a "superpower" that enhances their ability to innovate and solve complex problems.

For those looking to delve deeper, numerous resources and guided curriculums are available, crafted by experts in the field.  
I will try to curate a journey which will help you get your Aha moment and get a glimpse into the under belly of your machine.

![XKCD telling us, we just need the hardware, Neuralink took this seriously?](Assets/media/Linux%20Kernel%20Explained%20-%20Deep%20Dive%20Series%20for%20System%20Engineers/Linux%20Kernel%20Explained%20-%20Deep%20Dive%20Series%20for%20System%20Engineers-image-2024-05-29-232317.png)

---


### What Happens When You Press the Power Button on a Machine?

When you press the power button on your machine, a series of events unfold to initialize and start your compute![High level Sequence of Boot up Steps |475](Assets/media/Linux%20Kernel%20Explained%20-%20Deep%20Dive%20Series%20for%20System%20Engineers/Linux%20Kernel%20Explained%20-%20Deep%20Dive%20Series%20for%20System%20Engineers-image-2024-05-30-000610.png)

## BIOS and Power-On Self Test (POST)

The first program that runs on the hardware is the BIOS (Basic Input/Output System). The BIOS is an embedded program responsible for starting the computer and performing a POST (Power-On Self Test). Its stored on a ROM chip on your bios and is usually shipped by the motherboard vendor, although most vendors seem to source them from a few well known providers. In the world of BIOS, UEFI is the new modern reincarnation on the block. But from the linux kernel bootup perspective, BIOS vs UEFI has limited implications in the startup process*.

![Minimum POST checks at startup. Pic Credit: CGDirector.com |700](Assets/media/Linux%20Kernel%20Explained%20-%20Deep%20Dive%20Series%20for%20System%20Engineers/Linux%20Kernel%20Explained%20-%20Deep%20Dive%20Series%20for%20System%20Engineers-image-2024-05-30-000719.png)

1. **Power-On Self Test (POST):** During POST, the BIOS initializes the CPU and memory subsystem. It checks if these components are functioning correctly. If they start properly, the computer is ready to boot. However, this depends on the rest of the hardware functioning correctly as well.
2. **Hardware Initialization:** The BIOS initializes and lists all other peripheral hardware attached to the system. These peripherals are generally connected via buses like I2C, PCI Express, and SATA, which connect them to the CPU
3. **RAM check**: Verify RAM speed and make sure the bus speed of various subsystems are compatible. 
4. Boot a Storage Device: Try to find bootable storage devices. Either a disk with Master Boot Record entries, or a GPT UUID partitioned disk. 




5. ![BIOS and UEFI both perform POST on motherboards. UEFI just happens to be with the times.|750](Assets/media/Linux%20Kernel%20Explained%20-%20Deep%20Dive%20Series%20for%20System%20Engineers/Linux%20Kernel%20Explained%20-%20Deep%20Dive%20Series%20for%20System%20Engineers-image-2024-05-30-000359.png)


##### The Role of BIOS and Bootloader
- **BIOS:** Acts as the first basic check, initializing the system and performing POST.
- **Bootloader:** A more advanced program that loads the operating system, transitioning from BIOS initialization to the Linux kernel startup.

---
## Bootloader and GRUB

After POST, the BIOS looks for special I/O devices to provide the next program to run, typically the bootloader.

1. **Bootloader Initialization:** The bootloader is the next program in the sequence. Due to legacy standards, it starts the system in a 16-bit mode, then brings it up to a 32-bit or 64-bit mode. This process has been streamlined in the ARM world, but remains common in x86 processors.
2. **Loading the Operating System:** The bootloader loads the operating system, giving us the first glimpse of the Linux kernel.

Here is the minimal set of commands you can use on a GRUB prompt to start a linux system. 

```grub
insmod linux
set root=(hd0,1)
linux /boot/vmlinuz-3.13.0-29-generic root=/dev/sda1
initrd /boot/initrd.img-3.13.0-29-generic
boot
```

A quick description of what's happening. 

- load the linux grub module. This module tells grub how to start a Linux like operating system. 
- `/boot/vmlinuz-3.13.0-29-generic` is the compressed compiled linux kernel. 
- `/dev/sda1` is the root file system device
- `/boot/initrd.img-3.13.0-29-generic` is the initial ram disk
- `boot` kicks off the boot process and runs vmlinux. 

> **Future Topics**  
> If you're interested, I can cover BIOS and bootloader in more detail in future posts. However, for practicality, most of us won't be dealing directly with building BIOS or bootloaders. This high-level overview should provide a clear understanding of the initial steps in the boot sequence.

---

## Linux Kernel Bootup Sequence

Many seasoned developers have observed a Linux system boot up, witnessing a stream of text scrolling by on the screen. This output primarily consists of driver initializations and service startups. Despite its apparent complexity, the Linux kernel boot process is relatively straightforward. Let's delve into the most prevalent Linux kernel boot sequence

![Linux Boot Process in a Nutshell](Assets/media/Linux%20Kernel%20Explained%20-%20Deep%20Dive%20Series%20for%20System%20Engineers/Linux%20Kernel%20Explained%20-%20Deep%20Dive%20Series%20for%20System%20Engineers-image-2024-05-30-014854.png)

## Bare Minimum Linux Kernel?

As we saw in the grub commands, achieving a minimal boot for a practical PC experience requires,

- **vmlinuz** : Compressed compiled linux kernel binary
- **initramfs** or **initrd** : compressed archive which can be expanded by vmlinuz or grub and placed into memory
- (additionally) **root filesystem**

Linux follows a two stage booting process. The bootloader first loads the stage 1 kernel. 

*Stage 1* kernel's aim is simple and can be listed as follows

- Load just enough kernel modules to mount a proper filesystem. 
- Mount said root file system
- Hand over control to an init executable in the root filesystem. (/init, /sbin/init or configured paths in [linux/init/main.c at torvalds/linux · GitHub](https://github.com/torvalds/linux/blob/4a4be1ad3a6efea16c56615f31117590fd881358/init/main.c#L1523))

Because storage hardware comes in various formats (curse of linux's ubiquity), kernel developers have chosen to break the booting process into an initial in-memory file system load (**Initramfs** or **initrd**) which then mounts and loads the **root filesystem** 

*Stage 2* kernel boot is where the init process starts configuring hardware and running services, usually running programs initiated in userspace but invoking kernel space syscalls. This ensures the boot process can be configured without having to recompile the kernel for every small customizations. This design choice is the reason why we all aren't kernel developers (yet)

> Note: About minimal linux  
> For a truly minimal boot experience we could have a stripped down **vmlinuz** which runs a statically compiled */sbin/init* program to print hello world! all in < 10mbs of RAM, if you configure your kernel boot correctly!

> **Initramfs** and **initrd** (initial ramdisk) serve a similar purpose. initramfs is a modern take on initrd;  
> Write to me if you think I should write about the internals of initramfs/initrd.  
> PS: A quick search would point to some great resources.  
> I do find [What’s the Difference Between initrd and initramfs? | Baeldung on Linux](https://www.baeldung.com/linux/initrd-vs-initramfs) a good reference. 

## Root File System : Linux Kernel Directory Structure

Upon starting, the Linux kernel prepares and virtually presents some special file system in a specific way. The root file system and the initial RAM file system (initramfs) are crucial parts of this structure.  
Initramfs is the first file system that the kernel mounts and operates in memory, rather than on disk.  
Root filesystem is then loaded and presents more kernel modules, libraries, binary utilities and daemons.  
The root filesystem also starts various daemons which could further mount other storage devices and filesystems. 

We need to be aware of `/proc` and `/sys` directories, which contain information about the running kernel and allow certain kernel parameters to be modified.  
We also need to learn how all these file systems are combined together to provide a singular working view of the running system using overlayfs

<iframe style="border:none" width="800" height="450" src="https://whimsical.com/embed/RutWT6bkMH1J4nU7D7p2FV"></iframe>




### Init Process and the Role of PID 1: systemd and upstart in modern linux distros

In the world of Linux, PID 1 holds a special place. PID 1, or Process ID 1, is the first process started by the Linux kernel during the boot sequence and is the ancestor of all other processes. Understanding PID 1 and its role is crucial for grasping how a Linux system initializes and manages services.

When the Linux kernel finishes its initial setup, it launches the first user-space process, which is assigned PID 1. Traditionally, this process was the `init` system, responsible for starting system processes, handling system initialization, and managing services. The `init` system follows a predefined sequence to bring the system to a usable state.

PID 1 is critical because it remains running as long as the system is up and serves as the parent for all other processes. If PID 1 terminates, the kernel will panic, causing the system to halt or reboot, as there would be no process to adopt orphaned child processes.

#### systemd as init

In modern Linux distributions, `systemd` has largely replaced the traditional `init` system as the default system and service manager. `systemd` is designed to provide a more efficient and feature-rich way of managing system processes and services. It still occupies the PID 1 slot and takes on the responsibilities of its predecessor but with enhanced capabilities.

#### How systemd Works?

When the kernel passes control to `systemd` as PID 1, `systemd` begins its initialization process by mounting the initial file systems and starting essential services. It reads its configuration from unit files located in `/etc/systemd/system/` and `/usr/lib/systemd/system/`. These unit files describe how to manage services, sockets, devices, and other system components.

`systemd` also sets up the cgroups (control groups) to manage resource allocation and limits for processes

![|850](Assets/media/Linux%20Kernel%20Explained%20-%20Deep%20Dive%20Series%20for%20System%20Engineers/Linux%20Kernel%20Explained%20-%20Deep%20Dive%20Series%20for%20System%20Engineers-image-2024-05-29-030657.png)

## Kernel Privilege rings and security. PID 1's security implications

In the architecture of modern computer systems, privilege rings play a crucial role in maintaining security and stability. The Linux kernel operates in these rings to control access to resources and enforce security policies. Understanding the concept of privilege rings and the security implications of PID 1 helps in comprehending how Linux ensures a secure environment.

#### Privilege Rings Explained

Privilege rings are hierarchical levels of privileges that a system's processes can have. They range from Ring 0, the highest level of privilege, to Ring 3, the lowest.

- **Ring 0 (Kernel Mode):** The most privileged level, where the operating system kernel operates. It has unrestricted access to all system resources and hardware.
- **Ring 3 (User Mode):** The least privileged level, where user applications run. It has restricted access, requiring sudo to elevate to kernelmode

- ![](Assets/media/Linux%20Kernel%20Explained%20-%20Deep%20Dive%20Series%20for%20System%20Engineers/Linux%20Kernel%20Explained%20-%20Deep%20Dive%20Series%20for%20System%20Engineers-image-2024-05-29-031152.png)

The kernel mode (Ring 0) allows the operating system to execute critical tasks that require direct access to hardware and memory. User mode (Ring 3) provides a restricted environment for applications, preventing them from directly accessing hardware and system memory, thus protecting the system from malicious software and user errors.

> Ironically Ring 1 and Ring 2 have felt out of favor. 
> 
> As a hobbyist linux nerd, I discovered that the benefits of rings 1 and 2 in the modern protection model are greatly diminished due to paging only distinguishing between privileged (ring 0, 1, 2) and unprivileged levels. 
> 
> Anecdotally Intel designed rings 1 and 2 to house device drivers, providing them with some privileges while keeping them somewhat separate from kernel code. Although rings 1 and 2 can access supervisor pages, they still trigger a General Protection Fault (GPF) if they use a privileged instruction, similar to ring 3. Despite this, rings 1 and 2 are useful in certain designs. 
> 
> For instance, VirtualBox places guest kernel code in ring 1, and some operating systems do utilize them, though it is not a widely popular design choice at present.
