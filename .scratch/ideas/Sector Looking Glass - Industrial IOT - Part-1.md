
# Sector Looking Glass - Industrial IOT - Part-1

..why am i writing this...

Before we begin though, I want to define what I mean by Industrial IoT. 

Industrial IoT is an ecosystem of devices, sensors, applications, and associated networking equipment that work together to collect, monitor, and analyze data from industrial operations. Analysis of such data helps increase visibility and enhances troubleshooting and maintenance capabilities. It can also increase efficiencies, reduce costs, and improve safety and security.

Second, before you invest your attention, here is why you should care. 
There are multiple market forces which has ensured its an industry here to stay. 

First, as the definition states, the goal of IIoT is increase efficeincy and reduce cost. 
At the minimum, increased visibility is a good step forward for a lot of legacy organizations which have legacy hardware already in their facilities. We would cover how visibility drives efficiency in a couple of domains, and also talk about predictive maintenance and its compouding effect on lower OpEx and longer Asset life. More on this in later parts of the series. 

Second, it helps organizations capture more data about how their internal universe operates. This data was pretty much spilling over like an open tap with no bucket underneath it. This early capture, even if not harnessed immediately, could reap dividends if its harvested and stored with a bit of love and care.  We will dive into some challenges in data storage later in this series. 

Now for the issues I want to bring your attention to, 
 - Solving the basic skill gap and creating a desire to explore. 
    - This can only be done by breaking down guarded knowledge silos. 
 - Learning Path to get upto speed with different aspects of IIoT. 
    - I want to create a simple path which covers different technologies and shares insights about how these get used in the industry. 
 - Common architecture patterns.
 - State of Security in IIoT. 


## History of Industrial Machines

Industrial automation is nothing new. Humans have been building for a century and counting and machines do our bidding a lot. 
Its also commonplace to find "connected" machines within a factory, warehouse, power plant for most of last century.  So what's the buzz with Industrial IoT?

To answer this self posed question, lets make a distinction. 
Machines were connected to some kind of control room for operations. This so called connection may or maynot be logged, maybe for the sake of operations, compliance or safety.  Whatever the case be, such "connected" machines were connected for operational necessity. Each connection was proprietary with a few standards of interconnect showing up across different industries. 

But the key difference was how these connections looked nothing like what computers/telephony interconnects ever looked. 
These connections were often from a different multi-verse and were evolutions on top of a basic two wire telegraph like systems as their Optimus Prime. 

And this led to a point in history around 2000's where Computer Interconnects became really good, thanks to the explosion of the Internet, mobile phones and miniaturization of computer like systems to system on chips. 
At the same time, industries with incumbent machine manufacturers were languishing in their own universe of protocols and were reaching a point where things were very fragmented within the same factory floor. Huge vendor lockins, difficulty in inter-operation of machines from different vendors and in general a cacophony of vendors, protocols, systems, system integrators and reporting/operating sub-systems threatened to stall any modernization attempts. 

Its not so much the fact that these protocols were bad, no, not at all. It was just the abundace of them. Like so many of them!
And remember, its not like the internet itself doesn't have its own multitude of protocols. But we atleast have a consistent way of connecting networks of networks. Things like BGP, Ethernet, Fibre atleast share their protocol stack and agree to conventions in publically shared RFCs for anyone to reimplement.  I can't stress enough how amazing this is! Lets just say, Industrial machines really wanted to get on this bandwagon but were finding it kinda difficult. 

Then there is the question of data silos. You may ask, what data? 

Early days, getting information about a machine being on/off was a luxury. If someone got this in an excel like format, a clever excel formula would give you an Uptime MIS of that machine. All that this data could tell you was, hey, your machine was not working for 12 hours in the last week. That sucks, please ask the operator what the hell went wrong.  It could be any of Breakdown, Supply chain issues of no raw material, operator on leave or well, incompetence. 

Slowly, a few machines started coming with sensors onboard. And if you were really lucky, these sensors exposed their data in some standard protocol like modbus or serial. If you were unlucky, you knew there is a sensor, you know you need to get an addon card or even worse, a license from the manufacturer  so you could see or export this sensor data.  

Most common pattern in 70s to 2000s was a kind of middle ground.  Machines would come with sensors, control signals and a way to connect the machine to a Programmable Logic Controller. As most things in Industrial manufacturing goes, no points for guessing PLCs originated from Automobile manufacturing. PLCs did a small set of things, and did that well. They had Digital and Analog IO pins,  and a real-time logic chip which was programmable and had small non-volatile memory.  By using a chain of PLCs talking to each others digital/analog IO pins, you could build a primitive "network" in your factory. This network is what we is sometimes called a "Fieldbus [^3]"  And thats how we rolled out those Volkswagen's and Chevy's to the world. 

> Do you notice how a PLC from 1970s is indistinguishable in its core idea to an Arduino or a Raspberry Pi.  You would also notice their sense of networking is different from computer networks which were meant to carry "packets" while the core unit of interchange for machines was "signals"


Even more interesting was the fact that PLCs were programmed by *drumroll*  computers!
And yet computers were not used for the actual control because of a few major drawbacks. namely, they were slow and unpredictable. Or as a more astute tecnical writer might put it, they lacked real time gurantees and high realibility. 

I often think of PLCs as the ASICs [^2] of the industrial world.  They were unencumbered from the wide ranging general purpose needs of a personal computer. This was their super power, simple logic units which just worked, when programmed once. 
I have seen PLCs in the wild which were programmed 20 years ago and have never been reprgrammed ever. Barring failures in sensors or power electronics attached to them, they just work! Just make sure you have their logic program saved in some format which can be accessed 20 years down the line. That and the logic programmer used to flash this PLC.  All the rest of the failure modes are a simple electrical/cabling/replacement fix. Power gone? change power supply. Sensor misfiring, change sensor. I respect this low abstraction world. 

And here in begins the problem. Over time, as computers became ubiquitous, even of factory floors, it was often demanded that these two systems work together in meaningful ways. Starting in 2000s operators were becoming tech savy. Laptops, Palmtops, Blackberries, Mobile phones! and yet, they had to go to the control room to see the sensor reading on their HVAC or air compressor. Why! 

When you try to connect a PLC to the world of computers, you are essentially doing two things. 
 - Reading a bunch of PLC regiser memory 
 - Putting it into some meaningful computer protocol which can be sent over the "wire"




# 🤖 Protocols in Industrial IoT 



## 🌐 Protocols Used in Industrial Automation
- Industrial automation relies on various protocols to enable communication between devices and systems.
- Some commonly used protocols in industrial automation include:
  - Modbus: A serial communication protocol that was developed by Modicon in 1979 for use with programmable logic controllers (PLCs) [^1^].
  - OPC (OLE for Process Control): A set of standards for interoperability in the industrial automation industry [^2^].
  - Profibus: A protocol used for communication between automation systems and field devices [^2^].
  - DeviceNet: A communication protocol used in industrial automation to connect devices to a control network [^2^].
  - Ethernet/IP: An industrial Ethernet protocol used for communication between devices in automation systems [^2^].
  - Profinet: A protocol that enables real-time communication between devices in industrial automation systems [^2^].

## 🌞 Protocols Used in Commercial Solar/Wind Farms
- Commercial solar/wind farms also utilize protocols to facilitate communication and control of the equipment.
- Some commonly used protocols in commercial solar/wind farms include:
  - Modbus: The Modbus protocol is often used in solar/wind farms for communication between devices such as inverters, meters, and SCADA systems [^3^].
  - DNP3 (Distributed Network Protocol 3): A protocol widely used in the utility industry for monitoring and control of power systems, including solar/wind farms [^4^].
  - IEC 61850: A standard for communication in substations, often used in solar/wind farms for control and monitoring purposes [^4^].
  - MQTT (Message Queuing Telemetry Transport): A lightweight messaging protocol used in IoT applications, which can be utilized in solar/wind farm monitoring and control systems [^4^].
  - OPC-UA (OPC Unified Architecture): A platform-independent communication protocol widely used in industrial automation, including solar/wind farms, for interoperability between devices and systems [^4^].

# 📚 History of MODBUS-TCP and MODBUS-SERIAL

## 🏭 MODBUS-TCP
- MODBUS-TCP is a variant of the MODBUS protocol that uses Transmission Control Protocol (TCP) as the underlying communication protocol.
- It was developed to enable communication over Ethernet networks, providing a more flexible and scalable solution compared to the traditional serial-based MODBUS protocols [^3^].
- MODBUS-TCP was first published by Modicon (now Schneider Electric) in 1979 for use with its programmable logic controllers (PLCs) [^1^].
- Today, MODBUS-TCP is widely adopted in industrial automation systems and is used for communication between devices such as PLCs, HMIs (Human Machine Interfaces), and SCADA (Supervisory Control and Data Acquisition) systems.

## 🌐 MODBUS-SERIAL
- MODBUS-SERIAL is the original variant of the MODBUS protocol that uses serial communication, such as RS-232 or RS-485.
- It was also developed by Modicon in 1979 for use with its PLCs [^1^].
- MODBUS-SERIAL is well-suited for communication over long distances and in environments with electromagnetic interference.
- It is widely used in industrial automation systems for communication between devices such as PLCs, remote terminal units (RTUs), and sensors.

# 🤖 History of OPC-UA and Its Differences from MODBUS Protocols

## 📚 History of OPC-UA
- OPC-UA (OPC Unified Architecture) is a communication protocol developed by the OPC Foundation.
- It was designed to address the limitations of the earlier OPC (OLE for Process Control) protocol.
- OPC-UA was first released in 2008 and has since gained popularity in the industrial automation industry.
- It provides a platform-independent and secure communication framework for interoperability between devices and systems.

## ✨ Differences between OPC-UA and MODBUS Protocols
- OPC-UA and MODBUS are both widely used protocols in the industrial automation industry, but they have some key differences:
  - Architecture: OPC-UA follows a client-server architecture, allowing for more complex and distributed systems, while MODBUS is a simpler master-slave protocol [^4^].
  - Security: OPC-UA has built-in security features such as encryption and authentication, making it more secure compared to MODBUS [^4^].
  - Platform Independence: OPC-UA is platform-independent, enabling interoperability across different operating systems and devices. MODBUS, on the other hand, is more closely tied to specific hardware and software implementations [^4^].
  - Functionality: OPC-UA provides more advanced features such as historical data access, alarms and events, and complex data types, which are not supported in the MODBUS protocol [^4^].

## 🤖 Advantages and Disadvantages of Using MQTT in Industrial Automation
- MQTT (Message Queuing Telemetry Transport) is a lightweight messaging protocol used in IoT applications, which can also be utilized in industrial automation systems.
- Advantages of using MQTT in industrial automation include [^5^]:
  - Low Bandwidth: MQTT is designed to be efficient in terms of bandwidth usage, making it suitable for low-power and low-bandwidth environments.
  - Asynchronous Communication: MQTT enables asynchronous communication between devices, allowing for better scalability and responsiveness.
  - Flexibility: MQTT supports both point-to-point and publish-subscribe communication models, providing flexibility in system architecture design.
  - Decoupling: MQTT decouples the sender and receiver, allowing devices to communicate without being directly connected.
- Disadvantages of using MQTT in industrial automation include [^5^]:
  - Reliability: MQTT relies on the underlying network infrastructure, and if the network connection is unstable, message delivery may be affected.
  - QoS Trade-off: MQTT offers different levels of Quality of Service (QoS), but higher QoS levels may result in increased network traffic and latency.
  - Security Considerations: MQTT does not inherently provide encryption or authentication mechanisms, so additional security measures must be implemented to ensure secure communication.

🔖 References
[^1^]: [Modbus - Wikipedia](https://en.wikipedia.org/wiki/Modbus)
[^2^]: [What is Modbus and How does it work? | Schneider Electric USA](https://www.se.com/us/en/faqs/FA168406/)
[^3^]: [Demystifying Modbus Protocols: RTU, TCP, ASCII, and Plus | EMQ](https://www.emqx.com/en/blog/modbus-protocol-the-grandfather-of-iot-communication)
[^4^]: [OPC-UA vs Modbus - What's the difference? | Matrikon](https://www.matrikonopc.com/opc-ua-versus-modbus.aspx)
[^5^]: [Vladimir Romanov on LinkedIn: #software #automation #mqtt ...](https://www.linkedin.com/posts/vladromanov_software-automation-mqtt-activity-7100461748494704640-Ju-l)

[^X^]: []()
[^1^]: [Programmable Logic Controller : Wikipedia ](https://en.wikipedia.org/wiki/Programmable_logic_controller)
[^2^]: [Application-specific intergrated circuit : Wikipedia](https://en.wikipedia.org/wiki/Application-specific_integrated_circuit)
[^3^]: [Fieldbus : Wikipedia](https://en.wikipedia.org/wiki/Fieldbus)

