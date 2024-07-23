---
- id: ff081205-b36a-43ec-9f4a-aabcbf170e79
---

%%ff081205-b36a-43ec-9f4a-aabcbf170e79_start%%
## LISA21 - BPF Internals
> [Omnivore](https://omnivore.app/me/https-www-youtube-com-watch-v-5-z-2-au-7-qth-4-18f21989898)  |  [Original](https://www.youtube.com/watch?v=_5Z2AU7QTH4)

BPF Internals

Brendan Gregg

Extended BPF (aka eBPF) is a new type of software for secure, performant, event-driven programs, and has seen widespread adoption. Your Linux servers may already be running BPF programs; Netflix cloud instances run 15 by default, and Facebook over 40. These programs are for networking, performance tools, security policies, device drivers, application proxies, and more. Many have said that BPF is taking over Linux.

This talk is a deep dive that describes how BPF works internally and dissects some modern performance observability tools. Details covered include the kernel BPF implementation: the verifier, JIT compilation, and the BPF execution environment; the BPF instruction set; different event sources; and how BPF is used by user space, using bpftrace programs as an example. This includes showing how bpftrace is compiled to LLVM IR and then BPF bytecode, and how per-event data and aggregated map data are fetched from the kernel.

View the full LISA21 program at https://www.usenix.org/conference/lisa21/program


---
%%ff081205-b36a-43ec-9f4a-aabcbf170e79_end%%