---
title: Business of Datacenters - An India perspective
created: 2024-08-31 02:05
date: 2024-08-31
public: true
ShowToc: true
coverImage: https://stl.tech/wp-content/uploads/2023/02/Indian-data-center-market.webp
categories:
    - Business
tags:
    - topic/business
    - topic/indian-markets
    - topic/deep-dives
topic:
    - Startups
authors:
    - wiresurfer
description:
    An in-depth analysis of India's datacenter landscape, exploring the current
    state, challenges, and future prospects of the country's AI and data
    infrastructure.
---

# Business of Datacenters - An India perspective #1

A few months ago I had a word with my friend Kumar Aakash about our views on
AI's future, specially in the context of Indian startup opportunities. One thing
which came up was a lack of any serious specialized AI datacenter infrastructure
at that time. Some of the key challenges we noted were

<!-- more -->

-   GPU/TPU datacentres and the high tarrif to even import these.
-   Infererence datacentres too end up going to Mumbai or Chennai across the
    indian internet backbone.
-   Its hard to control where new startups host their AI services. Controlling
    data leaving India is hard.

Cut to last month, another friend of mine called me with an inquiry. He was
approached by folks to invest in a Datacenter business. Their model was
peculiar. They were selling fractional units of the datacenter in 1TB
increments. You invested an amount of Rs X for 1TB of capacity which was leased
to you for a persiod of 10 years as a depereciating asset. The datacentre folks
would then turn around and rent out this capacity and return the investor a
monthly rental revenue.

I digress as this blog isn't gonna cover the novelty/loopholes in the per TB
datacenter business. Thats another can of worms which we will open some other
day in an errata.

Today I wanted to ask a first principles question which has been bothering me
for a while.

> Is India ready to host its own AI revolution? If not, what steps can we take
> to be ready in the coming decade.

## State of the Union : India's DC landscape

India accounts for about 4% of the worlds datacenter capacity as of 2023. It
goes without saying that we account for a whole lot more humans in the world
than 4% would account for.

We have decent connectivity for our countryment with 46.3% indians online as
of 2021. And we do fare pretty well at bandwidth of our network connections
[jumping 72 places up to be 47th world wide as of 2023](https://utkarsh.com/current-affairs/india-jumpes-72-positions-in-the-ookla-speedtest-global-index#:~:text=According%20to%20the%20latest%20Ookla,5G%20services%20within%20the%20country).

Lets just say, with JIO lighting the match to rock bottom pricing, even with
recent corrections, India's connectivity story is a net win!

I will admit, we do have swathes of land, underserved communities and patches of
silence all across our geography which still dont have a decent reliable network
backhaul. But I don't see this as an impossible to solve situation. I am
confident products like starlink would drive the cost and feasibility of
satellite internet down as soon as we have local playes and regulatory hirdles
covered. We also need to think of services we would offer once we connect these
brand new users. This could well be a topic for another day, but lets just say,
LEO and MEO are gonna get crowded soon. Keep an eye out for Mukesh Ambani's JIO
space, Sunil Mittal backed OneWeb along with longtime incumbent Hughes and
INMARSAT pivoting to satellite broadband in the next 5 years.

In short, India's bandwidth usage has seen significant growth over the past few
years. Here are some key points:

1. **Average Data Consumption**: As of 2023, the average data consumption per
   user per month in India was around 24.1 gigabytes³. This is a substantial
   increase from previous years.

2. **Total Data Usage**: The total volume of wireless internet data usage in
   India surged to 32,397 petabytes in 2021, up from around 4,200 petabytes in
   2018⁴.

3. **Internet Penetration**: By 2024, the internet penetration rate in India
   rose to over 52%, meaning more than half of the population had internet
   access².

4. **4G and 5G Traffic**: 4G data traffic contributes to 99% of the overall data
   traffic, while 5G was launched in India in October 2022³.

This rapid increase in data usage is driven by affordable mobile internet plans,
widespread smartphone adoption, and the growing digital ecosystem in the
country.

So far so good, but lets look at our internet consumption patterns.

India's internet usage is driven by a variety of services, both for consumers
and businesses. Here's a breakdown:

### Consumer Bandwidth-Intensive Services

1. **Streaming Services**: Platforms like Netflix, Amazon Prime Video, and
   Disney+ Hotstar are major contributors to data consumption. Video streaming
   accounts for a significant portion of internet traffic[^6].
2. **Social Media**: Apps like YouTube, Instagram, Facebook, and TikTok also
   consume a lot of bandwidth due to video content
3. **Online Gaming**: Games like PUBG Mobile, Call of Duty Mobile, and other
   multiplayer games require substantial data for real-time interaction.
4. **Video Conferencing**: Services like Zoom, Microsoft Teams, and Google Meet
   have seen increased usage, especially post-pandemic⁶.

### Business Bandwidth-Intensive Services

1. **Cloud Services**: Businesses rely heavily on cloud platforms like AWS,
   Microsoft Azure, and Google Cloud for storage, computing, and other
   services⁶.
2. **Enterprise Applications**: Tools like Salesforce, SAP, and other SaaS
   applications are widely used.
3. **Data Analytics**: Big data and analytics platforms consume significant
   bandwidth for data processing and transfer.
4. **Remote Work Tools**: VPNs, remote desktop applications, and collaboration
   tools are essential for business operations.
5. AI! With Generative AI sticking to text at the moment, we are still in a slow
   bandwidth growth phase. But sooner rather than later,, audio and multimodal
   models will start demanding much bigger piece of the bandwidth pie. AI
   service providers also need DC capacity to host inference and training
   hardware in India which has created a high demand for GPU and NPU compute.
   Yotta data centers and Jarvislabs are two new players in this space with
   their GPU offerings as their USP and claim to fame

### Hosting Locations

-   **Domestic Hosting**: Many Indian companies and services host their data
    within India. This includes local data centers operated by companies like
    Reliance Jio, Airtel, and Tata Communications.
-   **International Hosting**: Some services, especially global platforms like
    Netflix and AWS, have data centers both in India and abroad. However, a
    significant portion of their infrastructure is still based internationally

### Data Flow and Undersea Cables

India, like most countries relies on undersea cables to connect to global
internet infrastructure. These cables are crucial for international data
transfer, especially for services hosted outside India. However, there is a
growing trend towards increasing domestic data center capacity to reduce latency
and improve service reliability. This trend is driven by the needs of two of the
most ubiquitous and dataintensive services which consumers love! Streaming and
Social Media!. Snappy snacable video needs to be cached and served from as close
to a user as possible or else we incur a penalty of moving bits over expensive
undersea cables. There's also a growing need to keep Indian user generated
content withing our national perimeter for reasons as simple as national safety
and as far fetched as abuse of indian data for AI training by foreign actors.

I say far fetched, but its already happening. A sizeable chunk of content
created by Indians lands up on services run by US megacorps. For a brief period,
we did indulge Chinese social media apps but a very swift regulatory push saw
that door shut pretty quickly. With recent push by OpenAI to collaborate with 3
letter agencies within USA and play a more direct role with development of AI as
a national security tool, its natural to conclude we may have given up a lot of
our users data in lieu of all the cat memes.

India has made significant strides in expanding its data center (DC) capacity to
host popular services like streaming, social media, online gaming, and video
conferencing. Here are some key points:

### Current Data Center Capacity

1. **Growth in Data Centers**: India has seen a rapid increase in the number of
   data centers. Major players like Reliance Jio, Airtel, Tata Communications,
   and global giants like AWS, Microsoft Azure, and Google Cloud have
   established or are expanding their data centers in India.
2. **Government Initiatives**: The Indian government has been promoting data
   localization, encouraging companies to store data within the country. This
   has led to increased investment in local data center infrastructure.
3. **Capacity and Scalability**: The current data center capacity is growing,
   with several new projects underway. For instance, Adani Group and Hiranandani
   Group are investing heavily in building large-scale data centers.

### Hosting Popular Services

-   **Streaming Services**: Platforms like Netflix and Amazon Prime Video have
    started hosting content locally to reduce latency and improve user
    experience. Hosting services are incentivized to host local content close so
    sooner or later pareto 80% of data would be hosted on our soil.
-   Related to streaming, Youtube is another big player backed by hyperscale
    infrastructure. Its hard to curb them to one geography. And they usually
    build up their own infrastructure rather than buy capacity on the market.

-   **Social Media**: Companies like Facebook and Instagram are increasingly
    using local data centers for better performance and compliance with data
    localization laws. While this promotes players like Meta to start with
    keeping data local, hyperscalers have a global mesh of interconnects and
    there's no stopping where the data would eventually get copied to, for
    operations, redundancy and strategic reasons.
-   There's strategic partnership between Jio and Meta and recently Reliance
    chairman Mukesh Ambani has gone on to announce an AI cloud hosted in India
    powered by Meta AI.
-   **Online Gaming**: Gaming companies are also setting up local servers to
    provide a smoother gaming experience with lower latency.
-   **Video Conferencing**: Services like Zoom and Microsoft Teams have been
    optimizing their infrastructure to include local data centers.

# Challenges and Future Prospects

Its abundantly clear that the DC sector is gonna see a windfall over the next
decade.

-   **Infrastructure Development**: While significant progress has been made,
    continuous investment in infrastructure is needed to keep up with the
    growing demand.
-   **Energy and Sustainability**: Data centers require substantial energy, and
    there is a push towards sustainable and energy-efficient solutions.
-   **Regulatory Environment**: Compliance with data protection and localization
    laws is crucial for both domestic and international companies operating in
    India.

Overall, India is on the right path to becoming self-sufficient in hosting its
own data for popular services. The ongoing investments and government support
are likely to further enhance the country's data center capacity in the coming
years.

I have compiled a few important resources if you are inclined to look at the
technical aspects of a datacentre, with an intention to write about this as I
dive deeper. Till then, this Board should be self explanatory.

<iframe width="768" height="432" src="https://miro.com/app/live-embed/uXjVKk_KO-A=/?moveToViewport=-4011,-3576,11830,6571&embedId=833406712359" frameborder="0" scrolling="no" allow="fullscreen; clipboard-read; clipboard-write" allowfullscreen></iframe>

If you are someone who's working in the DC space in India, or planning on diving
into this space, I would love to hear from you. More specifically, what are you
building and what's your play? What's your biggest challenge? I would love to
connect over linkedin or twitter and hear your unique perspective and add to
this series of blogs.

---

(1) India: average data consumption per user per month 2023 - Statista.
https://www.statista.com/statistics/1114922/india-average-data-consumption-per-user-per-month/.
(2) India's Internet Data Usage Shoots Up To 14.1 GB Per Month.
https://inc42.com/buzz/indias-internet-data-usage-shoots-up-to-14-1-gb-per-month/.
(3) India: internet penetration rate 2024 | Statista.
https://www.statista.com/statistics/792074/india-internet-penetration-rate/. (4)
Internet usage in India - statistics & facts | Statista.
https://www.statista.com/topics/2157/internet-usage-in-india/. (5) Massive data
usage growth in India: Economic survey.
https://economictimes.indiatimes.com/industry/telecom/telecom-news/massive-data-usage-growth-in-india-economic-survey/articleshow/89245236.cms.

(6) 52% of Indian population had internet access in 2022, says report.
https://economictimes.indiatimes.com/tech/technology/52-of-indian-population-had-internet-access-in-2022-says-report/articleshow/99964704.cms.
(7) US tech giants fight Indian telcos’ bid to regulate internet services, pay
for network usage.
https://www.msn.com/en-us/money/technology/us-tech-giants-fight-indian-telcos-bid-to-regulate-internet-services/ar-AA1p66j8.
(8) India adds 7.3 cr internet subscribers in FY24.
https://www.fortuneindia.com/macro/india-adds-73-cr-internet-subscribers-in-fy24/118083.
(9) India's internet user base grows 8% YoY to 95.4 crore.
https://www.newsbytesapp.com/news/science/india-s-internet-user-base-up-8-in-a-year/story.
(10) Internet usage in India - statistics & facts | Statista.
https://www.statista.com/topics/2157/internet-usage-in-india/. (11) Digital
2023: India — DataReportal – Global Digital Insights.
https://datareportal.com/reports/digital-2023-india.
(12)https://www.blackridgeresearch.com/blog/list-of-top-ten-largest-data-center-companies-in-india
