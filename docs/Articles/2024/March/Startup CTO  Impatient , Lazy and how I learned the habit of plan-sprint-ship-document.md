---
tags:
  - topic/engineering-management
  - topic/leadership
category:
  - Engineering
title: "Startup CTO : Impatient , Lazy and how I learned the habit of plan-sprint-ship-document"
coverImage: https://cdn-images-1.medium.com/max/800/1*pXY33WWBSZ9Kkf3vu5_a1w.png
public: true
ShowToc:
---
# Startup CTO : Impatient , Lazy and how I learned the habit of plan-sprint-ship-document

---
I have an admission to make. I, as a person, am impatient and lazy. Impatient because I can’t stop myself from jumping from one problem to the other with absolutely no time. And lazy, well, lazy in the oddest of ways. Let me explain what I mean by walking you through some of my learnings in the last few years. This article would resonate with hands-on tech engineers who are graduating into more rounded/demanding/business/founder roles.

![](https://cdn-images-1.medium.com/max/800/1*pXY33WWBSZ9Kkf3vu5_a1w.png)

credit: memecrunch.com

Some learnings are equally applicable for people steering products or services and who constantly strike a balance between long term road maps and short term needs. Last couple of years have been extremely enriching in terms of the breadth of hands on experience I got building SearchX, Pinclick and almost a dozen side projects. Here are

### **Shiny Objects are always enticing to an Engineer , but Product Heads need to keep a wide focus.**

This is where impatience shows its ugly face. Engineers try and solve problems. They look at it, make an abstract plan in their heads, and get down to work. Stopping when its either “impossible to crack” or when you have “nailed it”. Either cases lead to a fleeting pause before the engineer plunges into the next problem. These are what I would term _shiny objects._

![](https://cdn-images-1.medium.com/max/800/1*cPvjoUDY6tPy9GvMy99Zhg.gif)

Don’t catch every shiny object that comes your way.

As a founder or project manager, you suddenly can’t think of your product linearly. Problem In — Problem out paradigm doesn’t work anymore just because you have to constantly trade off between different things that need to be in place by different timelines.

**YODA: Plan your steps well, you must.**

> Which brings us to stage 1 of approaching any project. Plan it out in a phased manner. Version 1 , Version 2, **_and the transition plan from 1 and 2._**

If you translate this to startup speak, you could say version 1 is MVP, and version 2 is your product. And that would be a fair parallel, but I would urge you not to go by terminology and take away this one important part.

> **_and the transition plan from version 1 and version 2_**

You see, your MVP, if mildly successful will force you into a rapid build cycle. This is exactly where all semblance of planning goes out of the window. If your MVP is dead on arrival, you should not jump to the transition plan, but rather analyse what was the difference between what you built and what people wanted. Then do an MVP again. Don’t try resurrecting a dead horse. Of course scavenge it for parts, repurpose what you have, but that’s only possible when you had some semblance of a plan in the first place even for your MVP.

**Planning 101**

**a.** As a tech decision maker, your job is to decide on tradeoffs. **Tradeoffs have long range consequences**

_Easy to implement vs scalable or future proof_

_Cutting Edge open source framework or battle tested boring framework_

**b.** Plan in depth for a sprint. Not the whole Project at once.

**d.** Have broad strokes as to how Sprints together attain a projects objective

**e.** Have concrete milestones at end of each sprint. Simple example would be this one paragraph Sprint Milestone for a Week long Sprint.

> Users will be able to single sign on against an api, access control would work, Key business objects would be accessible via authenticated/authorized Crud APIs.

**f.** Tie sprint milestones with adoption and real world testing milestones. Dog food as much as you can.

![](https://cdn-images-1.medium.com/max/800/1*8oUWM232XhkVybNs7eF3DQ.png)

14 day sprint across multiple projects. Each heading contains sub tasks and their respective assignments and dependencies. Orange shows adoption tasks and their stake holder dependence

### **20% of Sprint == 80% of the fun important part**

_aka Pareto is a smart guy. No seriously, ask any consultant friend of yours_

Once you have the plan in place, Divide work items into bite sized chunks and predict resources it would consume to get done. At this point resources could be man hours, or it could be some dependency on other bite sized chunks.

![](https://cdn-images-1.medium.com/max/800/1*QsDI9e3y2ufV6RV1IdL3Iw.png)

This is best done with tools like OmniPlan or Xmind which can really help you visualise timelines and dependence. [Screenshots are from Omniplan sprint schedules we keep for our interdependent sprints]. Its also invaluable to share this plan with your team because that ways they see the big picture as well as their breadth of responsibility.

> **As part of your sprint plan, choose what you have to work on wisely. Choose things which are core to the problem or which require sufficient thought to be future proofed. Don’t put too much on your plate otherwise you will be too occupied and never have a big picture view of the sprint.**

Take for Example any enterprise application. If you break up the project into api scaffolding, authentication , business objects & decisions, and finally UI. You should ideally work on defining business objects as concretely as possible yourself. While you can delegate the task of brainstorming UI to your dev team sitting with your stake holders.

You should definitely sit through these discussions as this helps you hear them go through mock flows. You can update your plans for the business layer to accommodate workflows.

If you follow this approach, you would be picking up 20% of the most directly impactful pieces of the project.

![](https://cdn-images-1.medium.com/max/800/1*-soZFpDzASd57aYAzALMBg.png)

Bite sized chunks of work with pair wise allocation of human capital on critical tasks. Checkpoints are defined and this works as a great template for sync up or milestone meetings.

2. Always pair up your most (skilled + newest) team members on these 20% directly impactful pieces. What I mean by this is, you should engage someone on your team who hasn’t been exposed to a part of the stack/application,plus someone who knows that part well and split the work between them. This achieves two things, you familiarize someone else with a new part of the product. This is mighty helpful when one team member needs downtime, or you want to engage them in some other firefighting. This way work progresses and you can checkpoint easily. Secondly, both members are forced to communicate what they are thinking. This way, they have a clear picture in their head. If things aren’t clear, they generally get cleared up when a discussion happens. One outsider fresh eyes can ask questions which can untangle some deeply intertwined thoughts for the person already familiar with that part of the project

### **Last Mile Crawl**

Usually with any project, there are not one but a couple of 20% chunks. 2 or 3 of these chunks in a project is a healthy number. It also lends itself well to teams of size 5–10 where pairs of two solve 3 problems, and the rest work on the plumbing and connections.

![](https://cdn-images-1.medium.com/max/800/1*741XiUWzHgGDEMDODWlHoQ.png)

Which is where you have to be careful again. As you are nearing completion with your shared task, you should zoom out and periodically check with the progress on the integration front.

Its this 80% grunt work which needs to be executed cleanly or else you would severely impact your products value.

This last mile crawl usually takes a lot of patience. The team gets into the mood of “oh its done” while you can see the deadlines and are happy with the progress. Perfect window for complacence and delay to creep in.

So regularly taking the whole team in for discussions about their progress while also pushing their integrations tasks upwards will help you notice glitches with your project well in advance of the deadline. Start integrating and asking people to merge upstream as often as they can during the last weeks of your project

### **Don’t be Lazy. Document Everything**

When you finish a sprint, its important to spend a buffer period taking feedback from adopters, measure and monitor for bugs and bottlenecks, and familiarize everyone on the team with what got made. This is where you also document the final implementation [**_eg._** _Using socket.io for capturing user presence. Can be extended to support notifications and chat in future iterations]_. Capture concrete release notes, mention explicit tradeoffs or possible issues [**_eg_**. _We have upgraded react to 15.1, new devs can have incompatibility issues with older branches of the code_]

![](https://cdn-images-1.medium.com/max/800/1*_bNbfXONk-771MxdC90j3Q.png)

Yes, you will have to dig deep to get this done. But done it must be.

This is where my laziness has been a problem. Our team at pinclick has worked on some interesting challenges, and shipped internal systems at break neck speed and with amazing finesse. Along the way, we’ve learned some really obscure issues across open source stacks and yet in the hurry of jumping from one sprint to the other, we never got around to documenting our learnings.

Just to give you an idea of the breadth of work that has happened and things which we could have noted down, here is a non exhaustive list and for context, this was work done by a **team of 3** really dedicated and smart young engineers with whom I had the pleasure ofworking with.

**a.** Our CRM was built ground up to integrate closely with our telephony providers and other services like emails, user analytics and recommendation plus pricing engines. We rolled out a companion app for all our property advisors. [August to December Sprints] (As a side project I have been reimplementing a version which is more extensible and generic. This has already generated some interest and paying customers! do check [www.betterengage.com](http://www.betterengage.com/))

**b.** We migrated our infrastructure from EC2, to ECS/ECR and subsequently to kubernetes/ECR with spot instances which has given us flexibility and scaling capabilities and also **reduced our costs to roughly 1/4th** [Which was the main deal here :) ] [Nov to Feb Sprints]

**c.** A Machine Learning Prediction Engine to study user behavior and send signals back to CRM and Marketing, specially Adwords Marketing teams. [March onwards]

**d.** A closely knit telephony system to dial out customers, talk to the customer for a brief moment, confirming their interest and patching it forward to the field agents. [Jan — March].

**e.** We have been revamping our marketing system to add marketing automation, drip marketing and scheduling directly into our key systems [CRM, and Recommendation] [March-April Sprints]

**f.** And this is all besides shipping a v0.9 android app (which was more of a placeholder) and a website (which is now being revamped as our main focus shifts from empowering our advisors during meetings, to empowering online customers with tools to uncover trends and insights from our real estate data, when they visit our website)

### **So what now?**

As we delve into the next phase of our product development and growth, I would like to start documenting our learning more often. Over the last couple of months, I have been approached by and involved in discussions with folks from different companies about their technical and/or marketing challenges and it seems some of our learnings may have wider applicability.

Interestingly, my previous exposure to enterprise scale products and also having worked in an academic research like has given me some insights which I believe are worth sharing with fresh Tech Cofounders and Product leaders.

![](https://cdn-images-1.medium.com/max/800/1*MEMtulTlkasn_nKAZcofqw.png)

Yes, you sir, need to document for your own good, and share for everyone else’s wellbeing. Got it?

Here is what I would be covering in the coming weeks and would love the communities feedback about what else would they want to hear, and topics that I can additionally elaborate on.

1. Choices you make as a CTO: Evaluating Future threats, opportunities, tradeoffs and cost.
2. Node.js / React / React Native — Best Practices on maximal shared code, project structures, rapid prototyping & state of the union
3. Data storage — MongoDb, Redis, Elastic Search — when , why, and how to make optimum use of your DB store.
4. Data visualizations — Geographic data,Openstreetmaps, d3, mapbox gl, deck.gl, crossfilter, state of the union.
5. Deep learning classifiers for Everything Images! — Classifying images using InceptionNet features.
6. Dev Ops — Optimizing for scale, cost and ease of development, Kubernetes and why you should check it out, Dangers or provider Lock In, Docker and dev workflows.
7. Docker — Persistence, backup strategies, fault tolerance, state of the union
8. Marketing and its challenges — Email Marketing Woes, Optimizing Adwords for higher CTR, customer touch points with marketing and branding.
9. Telephony systems — Exotel, Twilio, how to integrate it into your workflows.
10. Project Management and Planning — This is the catch all bucket. So not sure what or how many posts this would cover.

Drop me an email or comment here if you have any feedback for me. I would be happy to learn , adapt and course correct. And if you have questions about your challenges and believe a discussion would be helpful, I would be open to have a chat.

Signing off,

*Your friendly neighborhood @wiresurfer*
**Shaishav Kr**

---

> Congratulations, you made it to the end! Here is your reward.
> follow [Shaishav Kumar a.k.a wiresurfer](https://x.com/wiresurfer), on twitter. Where you can send dog memes my way. or questions. you choose.
> or write to hello@shaishav.kr. Although sending dog memes here would be considered cute but unhelpful.