---
tags:
  - topic/platform-engineering
  - topic/devops
  - topic/deep-dives
  - series/bits-n-bytes
categories:
  - Engineering
title: Ghost in a shell - What the heck is a Terminal/Shell/TTY?
coverImage: https://i.gifer.com/embedded/download/ALh3.gif
public: 
ShowToc:
date: 2024-04-07
---
# Ghost in a shell - What the heck is a Terminal/Shell/TTY?

Long ago, in the early days of computing, when machines were vast and mysterious entities hidden behind layers of complexity, the world of Unix was emerging. It was a time when interactions with these computing behemoths were facilitated by peculiar devices known as terminals.
<!-- more -->
![](Assets/media/Ghost%20in%20a%20shell%20-%20What%20the%20heck%20is%20a%20Terminal,Shell%20and%20TTY/Ghost%20in%20a%20shell%20-%20What%20the%20heck%20is%20a%20Terminal,Shell%20and%20TTY-image-20240116000635848.png)


Picture this: a teleprinter-style contraption resembling a typewriter, affectionately referred to as a "teletypewriter" or simply a "tty." These were the portals through which users communicated with the mighty computers. But what was a terminal, really? Etymologically speaking, a terminal was at the end of an electric wire, forming a connection between humans and machines.

In the Unix realm, terms like terminal, tty, console, and shell danced intricately in a linguistic ballet. Terminal and tty were once synonymous, representing the text input/output environment. Meanwhile, the console, from a furniture perspective, stood as the physical terminal, the primary link to the machine.

As time marched forward, the electronic keyboards and displays became the new norm for terminals. The tty transformed into a specific kind of device file, extending beyond mere read and write commands. Some ttys were born from the kernel, others from terminal emulators like Xterm, Screen, SSH, and Expect.


![Display Replaced Paper | 480](Assets/media/Ghost%20in%20a%20shell%20-%20What%20the%20heck%20is%20a%20Terminal,Shell%20and%20TTY/Ghost%20in%20a%20shell%20-%20What%20the%20heck%20is%20a%20Terminal,Shell%20and%20TTY-image-20240116000801901.png)


The word "terminal" also took on a traditional meaning—a device where users interacted with a computer using a keyboard and display. Enter the X terminal, a thin client dedicated solely to human-computer interaction, with applications running on a more potent computer.

As the wheels of time went by, terminals started bridging effortlessly larger communication chasm. What started off as same room terminals, soon covered buildings, then grew to campus level machines, and slowly piggy backed on the parallelly influential telecommunications network to enable terminals across miles. 


![Beginning to look a lot like a modern day Desktop| 480](Assets/media/Ghost%20in%20a%20shell%20-%20What%20the%20heck%20is%20a%20Terminal,Shell%20and%20TTY/Ghost%20in%20a%20shell%20-%20What%20the%20heck%20is%20a%20Terminal,Shell%20and%20TTY-image-20240116002335555.png)



But what about the console? It wasn't just any terminal; it was the primary one directly connected to the machine. In some systems, like Linux and FreeBSD, the console manifested as several ttys, adding a layer of confusion with names like "console," "virtual console," and "virtual terminal."

And then there was the shell—a guiding force, the user's interface upon logging in. Was it the home environment for the user, or the realm where other programs dwelled? The mystery lingered.

Unix, being a diverse universe, birthed numerous shells. Bash, Zsh, and fish each brought their unique flavors to the interactive shell scene. Command-line shells allowed users to string together commands, often following the Bourne shell syntax. We had also entered the era of tele-communicaiton. teletypewriters had come a long way. 

![Two essential elements. Communicate and Type. With a cameo from early segment LED display | 480](Assets/media/Ghost%20in%20a%20shell%20-%20What%20the%20heck%20is%20a%20Terminal,Shell%20and%20TTY/Ghost%20in%20a%20shell%20-%20What%20the%20heck%20is%20a%20Terminal,Shell%20and%20TTY-image-20240116000701840.png)

As the dust settled, in the intricate dance between the terminal and the shell, tasks were divided. The terminal converted keys into control sequences, while the shell turned these sequences into executable commands. Line editing, input history, and completion were the domains of the shell.

Output, on the other hand, belonged to the shell. Instructions like "display foo," "switch foreground color to green," and "move cursor to the next line" emanated from the shell, guiding the terminal's actions.

As users traversed this digital landscape, copy-pasting and job control became part of their routine. The terminal facilitated inter-application copy-paste, while the shell managed job control, orchestrating programs in the background.

Thus, the history of terminals, consoles, and shells unfolded—a tale of technological evolution, linguistic intricacies, and the symbiotic dance between humans and machines in the Unix cosmos.

## Illustrate the problem


## Talk about the Core Idea of the Solution


## Evidence about the Solution Approach


## Solution Playbook 


## Call to Action


## Footnotes
- [What is the exact difference between a 'terminal', a 'shell', a 'tty' and a 'console'? - Unix & Linux Stack Exchange](https://unix.stackexchange.com/questions/4126/what-is-the-exact-difference-between-a-terminal-a-shell-a-tty-and-a-con)
- [The TTY demystified](https://www.linusakesson.net/programming/tty/)
- [Linux TTY Shell Cheat Sheet - Steflan's Security Blog](https://steflan-security.com/linux-tty-shell-cheat-sheet/)
- [Upgrading Simple Shells to Fully Interactive TTYs - ropnop blog](https://blog.ropnop.com/upgrading-simple-shells-to-fully-interactive-ttys/)
- [socat](http://www.dest-unreach.org/socat/doc/socat.html)
- [Unix Shells and Terminals - by Erik Engheim - Erik Explores](https://erikexplores.substack.com/p/unix-shells-and-terminals)
