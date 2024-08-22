Write a blog about state of eBPF in windows. My opinion is that its a step in
the right direction, it will take some time though, as eBPF is closely tied to
the linux internal kernel structures. And mapping them one-to-one is going to be
a tough ask in generalization. Its always the utopian promise of a unified
system which breaks down when you try and do anything serious. If developers end
up maintaining a different fork of their ebpf program for linux, vs a limited
fork for windows, adoption would be cruelly slow. this would take the steam out
of such an effort. running cilium on windows natively would be a good starting
point to convince me this is viable. this also opens up short term benefits for
kube on windows.

Research to incorporate in the blog post

1. this blog is motivated by a discussion posted by brendan gregg on hacker
   news/linkedin. He has been promoting ebpf for perf monitoring. here is the
   link to his blog post
   https://www.brendangregg.com/blog/2024-07-22/no-more-blue-fridays.html here
   is the hackernew discussion https://news.ycombinator.com/item?id=41033579

2. https://opensource.microsoft.com/blog/2021/05/10/making-ebpf-work-on-windows/#:~:text=Today%20we%20are%20excited%20to,of%20existing%20versions%20of%20Windows.

3. Using eBPF to create native Windows drivers
   https://www.youtube.com/watch?v=4hsvWDWwWYI

4. Cilium beyond linux. https://www.youtube.com/watch?v=gJ1z5iMsDJA
