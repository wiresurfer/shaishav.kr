---
title: Linux Kernel Explained - Deep Dive Series for System Engineers
created: 2024-04-28 14:46
public: true
category:
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
# Booting up Linux Kernel - Linux for Engineers #1

> Linux kernel is a monumental achievement of collaboration in the world of open-source software.  
  It has resulted in a powerful, versatile operating system base that powers an estimated 80-90% of the modern tech world  
  From smartphones in our pockets to the vast cloud infrastructure, Linux is the backbone of many technologies we rely on daily.  
  This series chronicles different aspects of modern day Linux system.  
  Each article aims to be a **tldr;** While linking to amazing talks/presentations/articles by some great minds.  
  Treat this as a crash course for the lazy and a jump-off point for the curious.  
  Happy reading!  
  Have feedback or questions, or want to be notified about more such articles? Follow me on Twitter [@wiresurfer](https://x.com/wiresurfer)  

## ⚡ And then there was light! ⚡

Ever wondered what happens when you press the power button on your machines.  
The fan's come to life, your RGB lights light up, there is a bell sound, and the screen shows a sea of gibberish \[or if you started using laptops, you probably see a fancy logo and a spinner. How boring is that!]  
By the end of this article, I want to unwrap the song and dance that goes on between hardware and different types of software to finally bring to you a usable PC. 

I won't hold back on some technical details and gloss over some in the interest of salvaging some brevity.

This post in particular will have a buildup and posturing in the beginning about hardware, bios and grub.  
While it isn't absolutely necessary for a Linux Kernel bootup saga, I do feel its important for a well rounded understanding. 

For the impatient, feel free to jump to [Linux Kernel Bootup Sequence](#Linux-Kernel-Bootup-Sequence)

---
## 🖥️ Modern PC Architecture  

A modern day PC hasn't changed its core design philosophy for over 30 years. Yes, there has been miniaturization and our electronics design has improved by leaps and bounds, but the basic building blocks have remained the same.  
Here is a picture of a motherboard annotated to show different subsystems. 

![|600](Assets/media/Booting%20up%20Linux%20Kernel%20-%20Linux%20for%20Engineers%201/Booting%20up%20Linux%20Kernel%20-%20Linux%20Kernel%20for%20System%20Engineers%201-image-2024-05-31-183240.png)

Even this can be simplified down to the following block diagram.  
If you pay attention, most of the peripherals used with modern machines connect over the PCI express bus. 

![|475](Assets/media/Booting%20up%20Linux%20Kernel%20-%20Linux%20for%20Engineers%201/Booting%20up%20Linux%20Kernel%20-%20Linux%20Kernel%20for%20System%20Engineers%201-image-2024-06-01-003141.png)

- Most demanding high throughput devices are the graphics cards and memory modules. They attach directly to the CPU over dedicated lanes often referred to as the **Northbridge**. 

- **Southbridge** on the other hand is a separate bus controller which manages other peripherals and connects to the CPU with a dedicated link. \[[**D**irect **M**edia **I**nterface or DMI3.0 is an Intel specific link](https://en.wikipedia.org/wiki/Direct_Media_Interface)\]

One thing omitted in this block diagram is a plethora of [i2c, uart, serial ](https://www.wevolver.com/article/i2c-vs-uart), [PWM](https://www.ekwb.com/blog/what-is-pwm-and-how-does-it-work/) and GPIO[^1] which help the motherboard maintain its function. 

Notable peripherals in a motherboard include:

- CMOS Clock \[helps with timekeeping specially in embedded devices. Modern OS's often use NTP to sync time]
- Temperature Sensors [^2]
- PWM controllers for fan control 

The first step in bringing the computer to working order is performed by a special program called the BIOS which is programmed onto a ROM chip on the motherboard, right from the factory. Lets see what happens in the BIOS. 

![High level Sequence of Boot up Steps |475](Assets/media/Linux%20Kernel%20Explained%20-%20Deep%20Dive%20Series%20for%20System%20Engineers/Linux%20Kernel%20Explained%20-%20Deep%20Dive%20Series%20for%20System%20Engineers-image-2024-05-30-000610.png)

## 🧩 BIOS and Power-On Self Test (POST)

BIOS is an embedded program responsible for starting the computer and performing a POST (Power-On Self Test). UEFI is the new modern reincarnation on the BIOS and the new kid on the block. From the Linux kernel bootup perspective, BIOS vs UEFI has limited implications in the startup process[^3]

![Minimum POST checks at startup. Pic Credit: CGDirector.com |475](Assets/media/Linux%20Kernel%20Explained%20-%20Deep%20Dive%20Series%20for%20System%20Engineers/Linux%20Kernel%20Explained%20-%20Deep%20Dive%20Series%20for%20System%20Engineers-image-2024-05-30-000719.png)

1. **Power-On Self Test (POST):** During POST, the BIOS initializes the CPU and memory subsystem. It checks if these components are functioning correctly. If they start properly, the computer is ready to boot. However, this depends on the rest of the hardware functioning correctly as well.
2. **Hardware Initialization:** The BIOS initializes and lists all other peripheral hardware attached to the system. These peripherals are generally connected via buses like I2C, PCI Express, and SATA, which connect them to the CPU
3. **CMOS Battery Check:** Keeping correct time is important. Not so critical these days, but back in the day, a depleted CMOS battery could lead to a lot of mess. Often a motherboard would refuse to boot automatically if it detected a fault in the CMOS Clock. 
4. **RAM check**: Verify RAM speed and make sure the bus speed of various subsystems are compatible. Overclockers tinker with the voltage levels of the RAM and the CPU to force it to run at higher than prescribed clock speeds. BIOS/UEFI these days protects such folks from frying up their threadripper/i9 cpu
5. **Boot a Storage Device:** Try to find bootable storage devices. Either a disk with Master Boot Record entries, or a GPT UUID partitioned disk. 


6. ![BIOS and UEFI both perform POST on motherboards. UEFI just happens to be with the times.|625](Assets/media/Linux%20Kernel%20Explained%20-%20Deep%20Dive%20Series%20for%20System%20Engineers/Linux%20Kernel%20Explained%20-%20Deep%20Dive%20Series%20for%20System%20Engineers-image-2024-05-30-000359.png)


##### Handing over to a Bootloader

As we learned **BIOS** acts as the first sanity check, initializing the system and performing POST. It hands over control to a **Bootloader**, a somewhat more advanced program that is tasked with loading operating systems

---
## 💽 Bootloader and GRUB 

After POST, BIOS looks for special I/O devices to provide the next program to run, typically the bootloader.  
Locating the bootloader is done by following a few conventions which have been in the PC world for decades. In short, BIOS has a configured set of boot devices. This preference is stored in the CMOS. 

After POST, BIOS will start going through each Boot Device and verify if it has a [Master Boot Record](https://en.wikipedia.org/wiki/Master_boot_record). This is where GRUB enters the picture. [GRUB](https://en.wikipedia.org/wiki/GNU_GRUB) is a program residing in the Master Boot Record of a bootable device. 

Here is a quick anatomy of the Master Boot Record. Its the first sector of a disk. A disk sector is traditionally 512bytes. Modern disks have larger sectors up to 4096 bytes \[Advanced Format Disks\] but even these disks access the physical media in 512byte emulated mode \[512e\]

512bytes of the MBR are broken up as follows

- 1-446bytes - Bootloader code. Grub **boot.img**
- 64 bytes - Master Partition Entries, Up to 4 entries, 16 bytes each. 
- Last 2bytes - A special magic number **0xAA55**. This indicates to the BIOS, there is a bootloader on this disk device. 

With that out of the way, lets look at GRUB as a bootloader. 

Now. lets be honest. 512bytes is a tight space, and adding things like splash image, nice graphics and menus to dual boot an OS will take way more than 512bytes. For eg. [EasyBMP](https://easybmp.sourceforge.net/) a tiny library to display images on screen when statically linked is 20kb! 

To work around this limitation, Grub does a multi-stage boot.  
**Stage 1**: ***Boot.img***, Fits in 440byte MBR. Its a simple sled program which loads Stage 1.5 using a [LBA address jump](https://en.wikipedia.org/wiki/Logical_block_addressing)  
**Stage 1.5**: *Core.img*, Fits in 32kb. It has just enough file system modules to load *\/boot\/grub*.  
**Stage 2:** *\/boot\/grub* is a special folder in /boot partition or a path on the root / partition. This is where all grub modules are available. It contains module drives for a large set of IO devices including networking booting. It also brings some nice things like a GUI, selection menus and splash pages!

![|500](Assets/media/Booting%20up%20Linux%20Kernel%20-%20Linux%20for%20Engineers%201/Booting%20up%20Linux%20Kernel%20-%20Linux%20Kernel%20for%20System%20Engineers%201-image-2024-06-01-011821.png)

Now all that theory out of the way, how do we boot the kernel itself? We usually just select a menu and boom! Linux starts loading up?  
Well, there is a bunch of configuration files and menu entries which makes that happen. Just peek into `/boot/grub/grub.cfg`. But we aren't looking at GRUB and its magic. Lets try to boot a system by first principles. 

Here is the minimal set of commands you can use on a GRUB prompt to start a Linux system. 

```grub
insmod linux
set root=(hd0,1)
linux /boot/vmlinuz-3.13.0-29-generic root=/dev/sda1
initrd /boot/initrd.img-3.13.0-29-generic
boot
```

A quick description of what's happening. 

- Load the linux grub module. This module tells grub how to start a Linux like operating system. 
- `hd0,1` - This is the tricky bit! This is grub's way of selecting a hard drive partition. varies on each machine, depending on how it was partitioned. This [stackexchange discussion should come in handy](https://superuser.com/questions/182161/grub-how-find-partition-number-hd0-x)
- `/boot/vmlinuz-3.13.0-29-generic` is the compressed compiled linux kernel. Tab completion is your friend. Version number `3.13.0` would likely change in your case. 
- `/dev/sda1` is the root file system device. 
- `/boot/initrd.img-3.13.0-29-generic` is the initial ram disk
- `boot` kicks off the boot process and runs vmlinux. 

Once we write boot, GRUB is officially trying to hand over control to the kernel. Phew! 

> **Future Topics**  
> If you're interested, I can cover BIOS and bootloader in more detail in future posts. However, for practicality, most of us won't be dealing directly with building BIOS or bootloaders. This high-level overview should provide a clear understanding of the initial steps in the boot sequence.

---

## <a href="#Linux-Kernel-Bootup-Sequence"></a> 🐧 Linux Kernel Bootup Sequence

Many seasoned developers have observed a Linux system boot up, witnessing a stream of text scrolling by on the screen. This output primarily consists of driver initializations and service startups. Despite its apparent complexity, the Linux kernel boot process is relatively straightforward. Let's delve into the most prevalent Linux kernel boot sequence

![Linux Boot Process in a Nutshell](Assets/media/Linux%20Kernel%20Explained%20-%20Deep%20Dive%20Series%20for%20System%20Engineers/Linux%20Kernel%20Explained%20-%20Deep%20Dive%20Series%20for%20System%20Engineers-image-2024-05-30-014854.png)

### Bare Minimum Linux Kernel?

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

## 🌴 Root File System : Linux Kernel Directory Structure

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

### Kernel Privilege rings and security. PID 1's security implications

In the architecture of modern computer systems, privilege rings play a crucial role in maintaining security and stability. The Linux kernel operates in these rings to control access to resources and enforce security policies. Understanding the concept of privilege rings and the security implications of PID 1 helps in comprehending how Linux ensures a secure environment.

#### Privilege Rings Explained

Privilege rings are hierarchical levels of privileges that a system's processes can have. They range from Ring 0, the highest level of privilege, to Ring 3, the lowest.

- **Ring 0 (Kernel Mode):** The most privileged level, where the operating system kernel operates. It has unrestricted access to all system resources and hardware.
- **Ring 3 (User Mode):** The least privileged level, where user applications run. It has restricted access, requiring sudo to elevate to kernelmode

- ![](Assets/media/Linux%20Kernel%20Explained%20-%20Deep%20Dive%20Series%20for%20System%20Engineers/Linux%20Kernel%20Explained%20-%20Deep%20Dive%20Series%20for%20System%20Engineers-image-2024-05-29-031152.png)

The kernel mode (Ring 0) allows the operating system to execute critical tasks that require direct access to hardware and memory. User mode (Ring 3) provides a restricted environment for applications, preventing them from directly accessing hardware and system memory, thus protecting the system from malicious software and user errors.

> Ironically Ring 1 and Ring 2 have felt out of favor. 
> 
> As a hobbyist Linux nerd, I discovered that the benefits of rings 1 and 2 in the modern protection model are greatly diminished due to paging only distinguishing between privileged (ring 0, 1, 2) and unprivileged levels. 
> 
> Anecdotally Intel designed rings 1 and 2 to house device drivers, providing them with some privileges while keeping them somewhat separate from kernel code. Although rings 1 and 2 can access supervisor pages, they still trigger a General Protection Fault (GPF) if they use a privileged instruction, similar to ring 3. Despite this, rings 1 and 2 are useful in certain designs. 
> 
> For instance, VirtualBox places guest kernel code in ring 1, and some operating systems do utilize them, though it is not a widely popular design choice at present.

## 🏁 Conclusion

Dear reader, I hope this gives you a glimpse into the fascinating engineering that powers your PC.  
We followed a popular path through the woods of bootloaders and linux kernels.  
In reality, there are many ways to boot a machine. We've got three components to mix and match. The BIOS, Bootloader and the OS/Kernel. 

In modern devices with a single powerful **System on Chip** design, we sometimes encounter BIOS and Bootloader becoming very slim and having features to offer OEM locking and security. In most systems there is a proprietary "BIOS".[^4] 

Keen readers would noticed how Grub was a two stage bootloader, and Linux kernel was a two stage OS boot system. There have been efforts like **Direct Kernel Boot**[^5] to merge these two components + four steps into a streamlined two step process. This speeds up the boot process and is usually seen as an option in Virtualization solutions and hypervisors. 

In no particular order or importance, here are some interesting projects powering the modern device bootup space. 

- [U-Boot](https://source.denx.de/u-boot/u-boot) - Usually used in embedded devices. Gives fine grained control of where the kernel gets loaded into device memory. As seen in:
	- SpaceX Dragon/falcon/
	- Ubiquiti/TP-Link network devices
- [Coreboot](https://coreboot.org/)
	- Chrome OS devices, Lenovo ThinkPad's and 
- Android Devices : 
	- While android uses a variant of the Linux kernel, there is no standard boot loader prescribed for running android os. 
	- OEMs implement their own boot loader depending on the storage options available and the SoC used. 
	- Qualcomm chipsets use Little Kernel and try to be UEFI compatible. 
	- MediaTek chipsets use a variant of U-Boot. 
	- Major players like Samsung have their own variants of the bootloader. 
- Cloud VMs : AWS/Azure/GCP support custom virtualized BIOS/UEFI for their VMs. 
	- Cloud BIOS supports emulating keyboard/serial console during the boot process, even before the bootloader or OS has loaded. This makes supporting any standard bootloader possible on cloud infrastructure. Critical for disaster recovery scenarios where your server, 7000kms away stops booting!
	- [Virtio and OS Images](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/virtualization_types.html): Cloud Boot disks are virtualized and attached on demand. You could explore **virtio** locally on qemu kvm. Virtualized storage enables using pre-built images for different operating systems. A superpower for running repeatable consistent infrastructure at scale!
	- **[Cloud-Init](https://cloud-init.io/)** : They also have additional initialization steps after the kernel and operating system start called **cloud-init**. This helps setup networking, user accounts, passwords and ssh keys, networking and services. It also helps platform operators to further extend the boot process. 



---

> Have feedback or questions, or want to be notified about more such articles? Follow me on Twitter [@wiresurfer](https://x.com/wiresurfer) > 

---

### Footnotes

[^1]: GPIOs are common in embedded boards like raspberry pi or industrial PCs. Here is an insightful stackoverflow discussion about hacks to [use GPIOs on desktop motherboards](https://superuser.com/questions/993690/do-desktop-computer-motherboards-have-gpio-if-they-do-how-to-read-from-or-writ)
[^2]: PWM Controllers and Temperature Sensors together play a critical role in thermal management. Most modern UEFI motherboards offer fine grained control over the sensor readings and the Fan control curve. 
[^3]: This is a loose statement and I accept its far from true. For all you advanced practitioners out there, remember we are writing this guide down to be approachable. I am shying away from a lot of complexity and keeping things simple. [Adam Williamson from Redhat, who has written about Linux, has a great post about this](https://www.happyassassin.net/posts/2014/01/25/uefi-boot-how-does-that-actually-work-then/)
[^4]: "BIOS" is a symbolic name here. Each SoC needs to start the hardware and do some rudimentary POST. Most Mobile devices also need to initialize a special telephony subsystem which runs its own Baseband OS. A traditional BIOS/UEFI introduced here would mean pushing a square peg through a round hole. 
[^5]: [20.2.3. Direct kernel boot Red Hat Enterprise Linux 6 | Red Hat Customer Portal](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/virtualization_administration_guide/sub-sect-op-sys-dir-kern-boot)
