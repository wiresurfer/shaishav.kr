---
title: Deep Dive into Linux Graphics - From Program to Pixel
created: 2024-07-15 10:00
date: 2024-07-15
public: true
coverImage: https://user-images.githubusercontent.com/62131389/124236344-4ddb8c80-db51-11eb-9278-c001b21a46ac.png
categories:
    - Engineering
tags:
    - topic/linux
    - topic/graphics
    - topic/programming
topic:
    - linux
    - graphics
description:
    Explore the complex journey of a pixel from a user program to your screen in
    Linux. This comprehensive guide covers the entire Linux graphics stack,
    including window managers, display servers, the Linux kernel, GPUs, and
    more.
---

# Deep Dive into Linux Graphics: From Program to Pixel

Linux graphics is a complex ecosystem involving multiple layers of software and
hardware. In this deep dive, I'll explore each component of the Linux graphics
stack, from user programs to the final pixel on your screen. On this quest, I
will provide practical examples and commands you can run on your Linux machine
to interact with these components directly and take a peek under the hood

<!-- more -->

> Why Should You Care?

Understanding the Linux graphics stack can be beneficial for:

-   Developers: Gain insights into how to optimize graphics performance and
    create visually stunning applications.
-   System Administrators: Troubleshoot graphics-related issues and configure
    systems for optimal performance.
-   Tech Enthusiasts: Deepen your knowledge of the underlying technology that
    powers our digital experiences.

I would also mention a special subset of readers for whom this blog would
function as compulsory reading - _VR/AR/XR_ enthusiasts and _Embedded Engineers_
building Smart Devices with a screen. There will be a more in-depth version of
the graphics stack which will focus specifically on zero copy buffers in the
Display stack. Such techniques along with gstreamer advancements are the
cornerstone of high framerate Vision ML systems

> The Pixel's Epic Quest

Imagine a pixel, a tiny speck of color, trying to make its way onto your screen.
Its journey begins with a user program and this intent to light up a pixel
traverses myraids of key software and eventually hardware components before an
actual photon of light is presented on screen.

Our aim is to go from the highest levels of abstraction down to the lower
trenches. Lets begin our journey from the user program itself

![A picture is worth a thousand words. Linux Graphics Stack in a nutshell](https://user-images.githubusercontent.com/62131389/124236344-4ddb8c80-db51-11eb-9278-c001b21a46ac.png)

## The Starting Point: User Programs

User programs are the origin of all graphical content on your screen. These can
range from simple command-line tools to complex graphical applications like web
browsers or video editors.

### X11: Creating a Simple X11 Program

Let's create a basic X11 program that opens a window: I am not going into the
details of linking libraries and assume someone who's reading this is somewhat
aware of how to make this snippet work. If you do find this difficult, drop a
message on Twitter and I would be happy to update this section with a detailed
set of steps. You can also jump over the code sample and take it at face value.

```c
#include <X11/Xlib.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    Display *d;
    Window w;
    XEvent e;
    char *msg = "Hello, X11!";
    int s;

    d = XOpenDisplay(NULL);
    if (d == NULL) {
        fprintf(stderr, "Cannot open display\n");
        exit(1);
    }

    s = DefaultScreen(d);
    w = XCreateSimpleWindow(d, RootWindow(d, s), 10, 10, 200, 100, 1,
                            BlackPixel(d, s), WhitePixel(d, s));
    XSelectInput(d, w, ExposureMask | KeyPressMask);
    XMapWindow(d, w);

    while (1) {
        XNextEvent(d, &e);
        if (e.type == Expose) {
            XDrawString(d, w, DefaultGC(d, s), 10, 50, msg, strlen(msg));
        }
        if (e.type == KeyPress)
            break;
    }

    XCloseDisplay(d);
    return 0;
}
```

Compile this program with:

```bash
gcc -o x11_example x11_example.c -lX11
```

Run it with:

```bash
./x11_example
```

This program demonstrates how an application interacts with the X11 display
server to create a window and draw text.

## Window Manager: The Organizer

The window manager is responsible for the placement and appearance of windows on
your screen. It receives requests from applications to create, move, resize, and
destroy windows. Window managers can be categorized into two main "meta"
categories. We have a stacking window manager or a tiling window manager. As the
name suggests, stacking window managers position new windows one on top of
another. On the other hand tiling window managers try to place windows so that
all active windows are visible without stacking on top of another window.

Some popular window managers include:

1. i3/sway: Tiling window managers sharing compatible configuration syntax but
   i3 being the OG wm supporting both x11/wayland vs sway being a modern wayland
   tiling wm
2. GNOME Shell: The default window manager for the GNOME desktop environment
3. KWin: The window manager for the KDE Plasma desktop
4. Xfwm: Lightweight stacking window manager from the Xubuntu/Xserver
   distributions.
5. Awesome WM: highly configurable, next generation framework window manager for
   X.

### Interacting with Window Managers

You can interact with your window manager using various tools and commands
provided by the window manager package.

For example, with i3, you can use the `i3-msg` command:

```bash
i3-msg move container to workspace 2
```

This command moves the currently focused window to workspace 2.

To see which window manager is currently running, you can use:

```bash
ps aux | grep -E "i3|gnome-shell|kwin"
```

## Display Server: The Middleman

The display server acts as an intermediary between user applications and the
graphics hardware. The two main display server protocols in use today are X11
and Wayland.

### X11

X11 is the older, more established protocol. You can check if you're running X11
with:

```bash
echo $XDG_SESSION_TYPE
```

If it returns "x11", you're using X11.

To see information about your X server, use:

```bash
xdpyinfo | less
```

This command provides details about your display, including the number of
screens, color depth, and available extensions.

### Wayland

Wayland is a newer protocol designed to address some of X11's limitations. Check
if you're running Wayland:

```bash
echo $XDG_SESSION_TYPE
```

If it returns "wayland", you're using Wayland.

To list Wayland clients:

```bash
sudo ls -l /proc/*/fd | grep wayland
```

This command shows which processes have open file descriptors to Wayland
sockets.

## The Linux Kernel: The Core

The Linux kernel provides crucial support for graphics operations through
various subsystems. This is where we cross over from userspace to kernel space.
To understand the kernel side of the story, we need to make a distinction about
exactly what is being rendered on screen?

If we talk about simple windows like text editors and your terminal we are in
the realm of 2D rendering. Usually, such 2D rendering is being done by a user
program aided by a component library like GTK or QT. Now a days though, most
programs including text editors, browsers are increasingly becoming "GPU"
rendered. They render 2D elements using 3D primitives while maintaining the
ability to render 3D when necessary.

Whether you render 2D primitives or 3D render your elements, usually decides the
magic combination of libraries and kernel modules which would work together to
bring your scene to life.

User Program > Python > QT

### Direct Rendering Manager (DRM)

DRM is responsible for managing GPU memory and providing a communication channel
between user space and the GPU.

To see DRM-related kernel messages:

```bash
dmesg | grep -i drm
```

### Kernel Mode Setting (KMS)

KMS allows the kernel to set display modes. You can see KMS-related information
with:

```bash
cat /sys/class/drm/card0/enabled
```

This shows whether KMS is enabled for your primary graphics card.

### Interacting with Graphics Devices

To list graphics devices:

```bash
ls /dev/dri/
```

This directory contains device nodes for your graphics hardware.

## GPU: The Powerhouse

The GPU performs the complex calculations necessary to render graphics. Modern
Linux systems use various APIs to interact with the GPU.

### OpenGL

OpenGL is a widely-used graphics API. To check OpenGL support:

```bash
glxinfo | grep "OpenGL version"
```

### Vulkan

Vulkan is a more recent, low-overhead graphics API. Check Vulkan support:

```bash
vulkaninfo | grep "Vulkan Instance Version"
```

If these commands aren't available, you may need to install additional packages:

```bash
sudo apt-get install mesa-utils vulkan-tools
```

## Memory Management: Getting Data Where It Needs to Go

Efficient memory management is crucial for graphics performance.

### Framebuffers

Framebuffers are regions of memory that hold pixel data. To list framebuffer
devices:

```bash
ls /dev/fb*
```

To get information about a framebuffer:

```bash
fbset -i
```

### Direct Memory Access (DMA)

DMA allows for efficient data transfer between system memory and the GPU. To see
DMA-related kernel messages:

```bash
dmesg | grep -i dma
```

## Display Pipeline: The Final Stretch

The display pipeline processes pixel data before it reaches your screen.

### Display Controller (DC)

The display controller manages the flow of pixel data to your display. You can
often find information about it in your system logs:

```bash
journalctl -k | grep -i "display controller"
```

### Encoder and Connector

These components prepare the signal for your specific display interface (e.g.,
HDMI, DisplayPort). To see information about your display connections:

```bash
xrandr --prop
```

This command shows all connected displays and their properties.

## The Finish Line: Your Display

Finally, the pixel data reaches your physical display. To get information about
your current display settings:

```bash
xdpyinfo | grep dimensions
```

This shows your current screen resolution.

## Additional Components

### EGL

EGL provides an interface between rendering APIs like OpenGL ES and the native
platform window system. To check EGL support:

```bash
eglinfo
```

If not available, you may need to install it:

```bash
sudo apt-get install libegl1-mesa-dev
```

### V4L2 (Video4Linux2)

V4L2 is the Linux kernel's API for video capture and output. To list V4L2
devices:

```bash
v4l2-ctl --list-devices
```

To see capabilities of a specific device (e.g., /dev/video0):

```bash
v4l2-ctl -d /dev/video0 --all
```

## Practical Exercise: Tracing Graphics Operations

Let's put it all together with a practical exercise. We'll trace the journey of
a graphics operation from a user program to the display.

1. First, let's start a simple graphics program:

    ```bash
    glxgears &
    ```

2. Now, let's trace the system calls made by this program:

    ```bash
    strace -p $(pgrep glxgears)
    ```

    You'll see various system calls related to X11, memory management, and more.

3. Let's check which files this process has open:

    ```bash
    lsof -p $(pgrep glxgears)
    ```

    You should see references to X11 sockets, shared libraries, and possibly DRM
    devices.

4. Now, let's look at the GPU usage:

    ```bash
    sudo intel_gpu_top  # For Intel GPUs
    # or
    sudo radeontop  # For AMD GPUs
    ```

    This will show you real-time GPU usage statistics.

5. Finally, let's check the impact on the display pipeline:

    ```bash
    sudo cat /sys/kernel/debug/dri/0/i915_display_info  # For Intel GPUs
    ```

    This shows current display pipeline configuration.

Through this exercise, we've traced a graphics operation from the user program
(glxgears), through the X11 server, to the GPU, and finally to the display
pipeline.

## Conclusion

The Linux graphics stack is a complex but fascinating system. From user programs
to the final pixel on your screen, there are numerous components working
together to create the visual output we see. By understanding these components
and how they interact, we can better optimize, troubleshoot, and appreciate the
technology behind our Linux desktops.

Remember, the examples provided here are just the tip of the iceberg. Each
component we've discussed has depths of complexity that entire books have been
written about. Don't hesitate to dive deeper into any area that particularly
interests you!
