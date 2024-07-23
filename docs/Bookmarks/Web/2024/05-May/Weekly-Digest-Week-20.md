---
- id: 55a88ed0-01d0-4d98-b66f-84b5b2457a3a
---

%%55a88ed0-01d0-4d98-b66f-84b5b2457a3a_start%%
## Linux Kernel vs DPDK: HTTP Performance Showdown
> [Omnivore](https://omnivore.app/me/https-youtu-be-z-wes-9-ea-09-xe-si-j-9-i-47-pv-zt-my-uc-ti-u-18f8e3712d8)  |  [Original](https://youtu.be/zWes9ea09XE?si=J9i47PvZtMYUcTiU)

🎥 Watch all the P99 CONF 2022 talks here: https://www.p99conf.io/

In this session I will use a simple HTTP benchmark to compare the performance of the Linux kernel networking stack with userspace networking powered by DPDK (kernel-bypass).

It is said that kernel-bypass technologies avoid the kernel because it is "slow", but in reality, a lot of the performance advantages that they bring just come from enforcing certain constraints.

As it turns out, many of these constraints can be enforced without bypassing the kernel. If the system is tuned just right, one can achieve performance that approaches kernel-bypass speeds, while still benefiting from the kernel's battle-tested compatibility, and rich ecosystem of tools.


---
%%55a88ed0-01d0-4d98-b66f-84b5b2457a3a_end%%