---
title: Tech Tip - My WSL2 devsetup for terminal productivity
created: 2024-08-14 16:27
date: 2024-08-14
public: true
coverImage: https://miro.medium.com/v2/resize:fit:1400/0*XcnXh0HWWO8tHSpA.jpg
categories:
    - engineering
tags:
    - topic/techtips
    - topic/devtools
    - topic/wsl2
topic:
    - techtips
description:
    Here are some tips to make your Windows devloper machine experience as close
    to a linux box. We cover terminal, neovim, Xserver applications and
    networking in WSL2 to make your life easy.
---

# Tech Tip - My WSL2 devsetup for terminal productivity

This guide is aimed at an intermediate to advanced user. We won't be covering
how to setup WSL2 from scratch. There are ample guides for it, but if you insist
on following my recommended source, here is a great guide.

<!-- more -->

This should help people with getting a step by step guide to getting WSL2 up and
running.
[How to Install WSL2 on Win10](https://www.freecodecamp.org/news/how-to-install-wsl2-windows-subsystem-for-linux-2-on-windows-10/)

For the folks who are more comfortable with both windows and linux, the rest of
the blog would work out more as a guideline which you can tweak to your liking.
I have broken down the document into sections with a set objective. Follow along
and happy tinkering.

## Preparing Windows Installation

We need to get some basic tools up and running on the windows machine. I highly
recommend chocolatey. Its been my package manager of choice and helps me get a
base set of tools on my windows machine.

List of tools would be

-   git
-   winrar
-   microsoft-windows-terminal
-   nerd-fonts-JetBrainsMono
-   vlc
-   vscode
-   gh
-   vcxsrv

## Windows Terminal, fonts and colorschemes.

Need to talk about nerdfonts, `choco install nerd-fonts-JetBrainsMono`

Need to cover color schemes using terminal json config. Reach their help section
on how to use a theme. Preview how the themes would look on the browser and then
Download something which you find useful.

[Windows terminal Themes](https://windowsterminalthemes.dev/) is your friend
here.

## Enable WSL2 Windows Features

```powershell
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux -NoRestart
Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform
shutdown /r
```

## WSL2 and Ubuntu 22.04

```powershell
$downloadUrl="https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi"
if ((Get-CimInstance Win32_operatingsystem).OSArchitecture.StartsWith('ARM 64')) {
    $downloadUrl="https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_arm64.msi"
}
$ProgressPreference = 'SilentlyContinue'; Invoke-WebRequest -Uri $downloadUrl -OutFile .\Downloads\wsl_kernel.msi
# run it
.\Downloads\wsl_kernel.msi

wsl --update
wsl --version
wsl --set-default-version 2
```

Install Ubuntu22.04

```powershell
$downloadUrl="https://aka.ms/wslubuntu2204"
# download it:
$ProgressPreference = 'SilentlyContinue'; Invoke-WebRequest -Uri $downloadUrl -OutFile .\Downloads\wslubuntu2204.AppxBundle
# install the exe:
If ($PSVersionTable.PSEdition -eq "Core") {
    Import-Module Appx -UseWindowsPowerShell
}
Add-AppxPackage .\Downloads\wslubuntu2204.AppxBundle
```

Launch ubuntu shell from the start menu or from cmd/powershell

```powershell
ubuntu.exe
```

Set a password and update/upgrade packages

```bash
sudo passwd
```

Shutdown wsl distro for now using powershell/cmd. elevated

```powershell
wsl --shutdown
```

## Customizing WSL2 distro settings

Cover custom changes to .wslconfig WSLConfig is done on the windows side and
affects the WSL2 engine which runs your linux distros. Its important to
customize this to control how disk, memory, swap and processors are allocated to
your WSL2 vm. It also enables/disables virtualization, memory page reporting as
well as dns/firewall/proxy settings for your WSL2 guest os.

You can use something as simple as note pad to edit this file. Its usually
located in `%UserProfile%\.wslconfig` which on most systems would resolve to
`C:\Users\<username>\.wslconfig`

For advanced users, here is a list of flags available for you to tinker with.
[MSDN: About .wslconfig](https://learn.microsoft.com/en-us/windows/wsl/wsl-config#wslconfig)

To edit .wslconfig you can run `notepad C:\Users\<username>'.wslconfig` from
cmd/powershell/run

My recommended settings do the following

-   Gives you control over ram/swap/processors allocated to your VM. This
    maintains performance for both Windows host, and limits how much a rogue
    WSL2 instance can hog as guest
-   Control over swapfile location.
-   enabling nestedVirtualization for using docker/kvm/qemu natively inside wsl2
-   removing all kinds of network meddling done automatically by windows inside
    your WSL2 machine.
-   disabling firewall reduces cpu/memory usage by Windows Defender service
    which constantly keeps running over WSL2 files.
-   automemory reclaim to an aggressive level. frees up memory for windows as
    soon as possible.
-   vmIdleTimeout to sleep/stop the WSL2 guest os after 1hr.

```
# notepad %UserProfile%\.wslconfig
# Recommended .wslconfig.

guiApplication=true
memory=6GB
processor=4

swapfile=C:\\temp\\wsl-swap.vhfx

pageReporting=false
nestedVirtualization=true
vmIdleTimeout=3600000

autoproxy=false
firewall=false
dnsTunneling=false

[experimental]
sparseVhd=true
autoMemoryReclaim=dropcache
```

WSL.conf is used to edit the behavior of a WSL2 distro. Its located at
`/etc/wsl.conf` We want to control the username, enable systemd, disable
mounting windows drives, tweak the networking setup and disable the use of
windows exe's being launched from WSL2. All these tweaks ensure WSL2 works as
independent of the windows os as possible. Mounting windows drives also seems to
affect shell performance on linux bash/zsh/git while putting Windows defender in
hyperdrive. These config changes lead to a more predictable Linux OS with much
quieter fan/resource usage.

```
# sudo vi /etc/wsl.conf
# Set the user when launching a distribution with WSL.
[user]
default = wsluser

[boot]
systemd=true
command = service docker start

# Automatically mount Windows drive when the distribution is launched
[automount]
# Set to true will automount fixed drives (C:/ or D:/) with DrvFs under the root directory set above. Set to false means drives won't be mounted automatically, but need to be mounted manually or with fstab.
enabled = false

# Sets the directory where fixed drives will be automatically mounted. This example changes the mount location, so your C-drive would be /c, rather than the default /mnt/c.
root = /mnt

# Sets the `/etc/fstab` file to be processed when a WSL distribution is launched.
mountFsTab = true

# Network host settings that enable the DNS server used by WSL 2. This example changes the hostname, sets generateHosts to false, preventing WSL from the default behavior of auto-generating /etc/hosts, and sets generateResolvConf to false, preventing WSL from auto-generating /etc/resolv.conf, so that you can create your own (ie. nameserver 1.1.1.1).
[network]
hostname = wsl
generateHosts = false
generateResolvConf = false

# Set whether WSL supports interop processes like launching Windows apps and adding path variables. Setting these to false will block the launch of Windows processes and block adding $PATH environment variables.
[interop]
enabled = false
appendWindowsPath = false

```

## XServer

WSL2 doesn't require running a separate Xserver anymore. We have set the option
in .wslconfig above to enable GUI Applications.

If you are doing a new installation follow this
[MSDN: GUI apps in WSL on Windows](https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps)

If you are on an older distro, specially if you haven't abandoned Win10 yet You
would need to install an Xserver.
[Chocolatey: vcxsrv package](https://community.chocolatey.org/packages/vcxsrv)

And follow the steps here. [Guide2WSL: X11](https://www.guide2wsl.com/x11/)

Start vcxsrv and enable unautorized clients from connecting Set
`DISPLAY=<windows-host-ip>:0` variable in your profile to point to your Windows
host ip address install an xserver app, start with xeyes.
`sudo apt-get install xorg-x11-apps && xeyes`

Check the status of opengl and accelerated graphics rendering if you care for
this. `sudo apt-get install mesa-utils && glxgears`

```bash
sudo apt-get install xorg-x11-apps mesa-utils
xeyes
glxgears
```

Whether this runs or not depends a lot on your particular video card, drivers in
WSL2 and your mesa,glx,drip packages. This is a separate can of worms which I
intend to cover in a different post.

## Docker containers in WSL2

You have three options to go with here.

1. Use docker cli/client in wsl2 and docker-daemon running in windows using
   [Docker Desktop](https://www.docker.com/products/docker-desktop/)
    1. This will work for most users.
    2. Uses more resources.
    3. docker-desktop isn't available for Windows arm devices.
    4. Gets tricky when using with advanced permissions, hosts, etc.
    5. Comes out of the box.
    6. Steps
       [Docker Desktop on Windows WSL](https://docs.docker.com/desktop/wsl/)
2. User docker client + docker daemon running inside WSL2.
    1. Much cleaner, closest to how things would be on a tradition Ubuntu
       distro.
    2. Works on ARM.
    3. Consumes lesser resources. you have advanced control on hosts, volumes,
       permissions et.al.
    4. plays well with k3d/kind/minikube and friends.
    5. Steps to follow:
       [Guide2WSL Docker daemon inside WSL2](https://www.guide2wsl.com/dockerd/)
3. Run docker using buildkit + containerd + nerdctl/podman
    1. For advanced users. You can run rootless containers too.
    2. You have control over networking using CNI plugins
    3. You can also stop buildkit from running and only launch it on demand.
    4. No daemons by default. Most frugal in terms of resources
    5. Steps for nerdctl :
       [Guide2WSL: nerdctl on wsl2](https://www.guide2wsl.com/nerdctl/)
    6. Steps for podman:
       [Guide2WSL: podman on wsl2](https://www.guide2wsl.com/podman/)

## Bonus : Tailscale for accessing your phone,windows, wsl2, tablet over one network

I use tailscale to bring all my devices online on a virtual network. This makes
things like ssh'ing from my tablet to my devmachine over public internet
seamless. It also enables things like ADB debuggig over the network feasible. Or
testing a web project/api from a mobile app or mobile browser.

Steps are self explanatory, you need a github account. You can follow the
[quickstart guide at tailscale docs](https://tailscale.com/kb/1017/install)

## Bonus : Window snapping and keyboard controls.

I use powertoys to enable just two features.

1. FancyZones for dividing my screens into snap reagions. Specially for
   ultrawide of portait monitors, you would want to snap in 1/3rd sections, or
   snap above and below.
2. alt+space to launch applications.

With these two settings, and some custom shortcuts for minimize, maximize, move
to next screen, I can happily disable all desktop icons and make the taskbar
autohide.

I tend to keep the same shortcuts between my xubuntu machine and my windows
machines. Which means moving from my ubuntu desktop to my travel ultralight
spectre x360 is a breeze.

## Development Experience.

One of the reasons I force myself to use neovim is the fact that my programming
experience is pretty much the same whether I am inside WSL2 on windows or on a
linux shell. Coupled with tmux and neovim/lunarvim I get to be productive on a
14inch 1920x1080 screen or a triple monitor setup.

Using a browser which supports vimium plugin on android tablet, windows and
ubuntu makes sure my browsing the web isn't a mouse heavy exercide.

Overall this setup has reduced my RSI so much that I am no longer afraid of long
stints of programming anymore. I can spend well over 4 hours straight without
much fatigue while writing long articles with minimal distraction.

## Conclusion

I hope this article lays out some steps for people constrained with using a
windows machine, or people who generally want the best of both worlds. There are
still some rough edges, but give it time and you would not be too bothered by
it. Guide2WSL is a great resource for starters.

A WSL2 setup like this helps me contribute or atleast work on a custom linux
kernel for WSL2 which supports ebpf tracing. If you can hack on the linux kernel
then i doubt there is anything limiting your experience other than knowing how
things work and how to work around issues.

Good luck and I am curious to hear your thoughs and suggestions!.
