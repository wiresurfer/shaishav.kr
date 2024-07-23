---
- id: f712d176-06d0-46b6-9a66-afaf9742d2be
---

%%f712d176-06d0-46b6-9a66-afaf9742d2be_start%%
## Networks Are Under AI Pressure: Can Cilium Provide Relief? - Isovalent
> [Omnivore](https://omnivore.app/me/networks-are-under-ai-pressure-can-cilium-provide-relief-isovale-18f9cd08d22)  |  [Original](https://isovalent.com/blog/post/cilium-the-network-and-security-platform-for-the-cloud-native-ai-era/)

In this blog post, we explore why some of the largest AI companies and services are using Cilium and Isovalent.

### Highlights

> [OpenAI’s Kubernetes infrastructure already exceeded 7,500 nodes](https://openai.com/index/scaling-kubernetes-to-7500-nodes/)). [⤴️](https://omnivore.app/me/networks-are-under-ai-pressure-can-cilium-provide-relief-isovale-18f9cd08d22#ec37bed5-50ca-46d1-b6db-91ab888d4d61)  ^ec37bed5

7500 8vCPU nodes [min]  would still be a huge TDP wattage! 
Underscores how chip advancement, and green energy would be instrumental in our AI future

> highly reliable networks [⤴️](https://omnivore.app/me/networks-are-under-ai-pressure-can-cilium-provide-relief-isovale-18f9cd08d22#1731b227-a467-4ab3-a8d5-ea71abcee252)  ^1731b227

Linux networking stack would soon bottleneck when coming to training models across GPUS. 

Single CPU + single GPU -> bottleneck is PCIx16 bandwidth + memory lanes. 

Sincle CPU + Multi GPU -> bottleneck is PCI Bandwidth. Interrupts and DMA, soft IRQ

Multi node CPU+GPU  -->  bottle neck is all of the above + NIC + kernel + interconnect.  Even with infiniband links across Nodes,  high throughput networking in kernel is needed.   
Imagine  -> CUDA/Pytorch/keras  being optimized in userland,  Infiniband/NIC offering highest gpbs interconnect,  but kernel conking off at moving tensors across machines. 

> protect their intellectual property [⤴️](https://omnivore.app/me/networks-are-under-ai-pressure-can-cilium-provide-relief-isovale-18f9cd08d22#1fef791e-cfaa-4633-af28-bbd896cef058)  ^1fef791e

only when in PaaS mode. 
i would argue, training is done on private VPC with bastion nodes. 

Not on public eavesdroppable internet. 

So model theft is a difficult vector. 


---
%%f712d176-06d0-46b6-9a66-afaf9742d2be_end%%