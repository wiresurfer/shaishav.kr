# Data Collection in Industrial IoT

## 🤖 Protocols in Industrial IoT

### 🌐 Industrial Automation

-   Industrial automation relies on various protocols to enable communication
    between devices and systems.
-   Some commonly used protocols in industrial automation include:
    -   Modbus: A serial communication protocol that was developed by Modicon in
        1979 for use with programmable logic controllers (PLCs) [^1^].
    -   OPC (OLE for Process Control): A set of standards for interoperability
        in the industrial automation industry [^2^].
    -   Profibus: A protocol used for communication between automation systems
        and field devices [^2^].
    -   DeviceNet: A communication protocol used in industrial automation to
        connect devices to a control network [^2^].
    -   Ethernet/IP: An industrial Ethernet protocol used for communication
        between devices in automation systems [^2^].
    -   Profinet: A protocol that enables real-time communication between
        devices in industrial automation systems [^2^].

### 🌞 Commercial Solar/Wind Farms

-   Commercial solar/wind farms also utilize protocols to facilitate
    communication and control of the equipment.
-   Some commonly used protocols in commercial solar/wind farms include:
    -   Modbus: The Modbus protocol is often used in solar/wind farms for
        communication between devices such as inverters, meters, and SCADA
        systems [^3^].
    -   DNP3 (Distributed Network Protocol 3): A protocol widely used in the
        utility industry for monitoring and control of power systems, including
        solar/wind farms [^4^].
    -   IEC 61850: A standard for communication in substations, often used in
        solar/wind farms for control and monitoring purposes [^4^].
    -   MQTT (Message Queuing Telemetry Transport): A lightweight messaging
        protocol used in IoT applications, which can be utilized in solar/wind
        farm monitoring and control systems [^4^].
    -   OPC-UA (OPC Unified Architecture): A platform-independent communication
        protocol widely used in industrial automation, including solar/wind
        farms, for interoperability between devices and systems [^4^].

## 📚 History of MODBUS-TCP and MODBUS-SERIAL

### 🏭 MODBUS-TCP

-   MODBUS-TCP is a variant of the MODBUS protocol that uses Transmission
    Control Protocol (TCP) as the underlying communication protocol.
-   It was developed to enable communication over Ethernet networks, providing a
    more flexible and scalable solution compared to the traditional serial-based
    MODBUS protocols [^3^].
-   MODBUS-TCP was first published by Modicon (now Schneider Electric) in 1979
    for use with its programmable logic controllers (PLCs) [^1^].
-   Today, MODBUS-TCP is widely adopted in industrial automation systems and is
    used for communication between devices such as PLCs, HMIs (Human Machine
    Interfaces), and SCADA (Supervisory Control and Data Acquisition) systems.

### 🌐 MODBUS-SERIAL

-   MODBUS-SERIAL is the original variant of the MODBUS protocol that uses
    serial communication, such as RS-232 or RS-485.
-   It was also developed by Modicon in 1979 for use with its PLCs [^1^].
-   MODBUS-SERIAL is well-suited for communication over long distances and in
    environments with electromagnetic interference.
-   It is widely used in industrial automation systems for communication between
    devices such as PLCs, remote terminal units (RTUs), and sensors.

## 🤖 History of OPC-UA and Its Differences from MODBUS Protocols

### 📚 History of OPC-UA

-   OPC-UA (OPC Unified Architecture) is a communication protocol developed by
    the OPC Foundation.
-   It was designed to address the limitations of the earlier OPC (OLE for
    Process Control) protocol.
-   OPC-UA was first released in 2008 and has since gained popularity in the
    industrial automation industry.
-   It provides a platform-independent and secure communication framework for
    interoperability between devices and systems.

### ✨ Differences between OPC-UA and MODBUS Protocols

-   OPC-UA and MODBUS are both widely used protocols in the industrial
    automation industry, but they have some key differences:
    -   Architecture: OPC-UA follows a client-server architecture, allowing for
        more complex and distributed systems, while MODBUS is a simpler
        master-slave protocol [^4^].
    -   Security: OPC-UA has built-in security features such as encryption and
        authentication, making it more secure compared to MODBUS [^4^].
    -   Platform Independence: OPC-UA is platform-independent, enabling
        interoperability across different operating systems and devices. MODBUS,
        on the other hand, is more closely tied to specific hardware and
        software implementations [^4^].
    -   Functionality: OPC-UA provides more advanced features such as historical
        data access, alarms and events, and complex data types, which are not
        supported in the MODBUS protocol [^4^].

## Footnotes

🔖 References 
[^1^]: [Modbus - Wikipedia](https://en.wikipedia.org/wiki/Modbus)
[^2^]: [What is Modbus and How does it work? | Schneider Electric USA](https://www.se.com/us/en/faqs/FA168406/)
[^3^]: [Demystifying Modbus Protocols: RTU, TCP, ASCII, and Plus | EMQ](https://www.emqx.com/en/blog/modbus-protocol-the-grandfather-of-iot-communication)
[^4^]: [OPC-UA vs Modbus - What's the difference? | Matrikon](https://www.matrikonopc.com/opc-ua-versus-modbus.aspx)
