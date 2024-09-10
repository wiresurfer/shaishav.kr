# 🤔 How does MODBUS-TCP work?
## 🌈 The MODBUS-TCP Protocol
MODBUS-TCP is a protocol that combines a physical network (Ethernet) with a networking standard (TCP/IP) and a standard method of representing data (Modbus) [^1^]. It is used for communications over TCP/IP networks and connects over port 502 [^4^]. The protocol follows a client-server architecture, where the client initiates a request and the server responds with the requested data [^1^].

## 📚 The MODBUS-TCP Data Packet
The MODBUS-TCP data packet consists of a Modbus Application Protocol header, a function code indicating the message operation, and the data field [^5^]. The data field contains the requested data or the response data, depending on the message type [^5^]. The function codes define the operation to be performed, such as reading or writing data, and are standardized across different MODBUS devices [^5^].

## 🎓 The MODBUS-TCP Topology
MODBUS-TCP uses a client-server topology, where the client initiates the communication and the server responds to the client's request [^1^]. The client can be a human-machine interface (HMI), a supervisory control and data acquisition (SCADA) system, or any other device capable of sending MODBUS-TCP messages [^1^]. The server, on the other hand, is the device that receives the client's request and provides the requested data [^1^]. In the case of Solar Panels/Inverters, the server would be the device that stores and serves the Modbus data [^1^].

[^1^]: [Introduction to Modbus TCP/IP](https://www.prosoft-technology.com/kb/assets/intro_modbustcp.pdf)
[^4^]: [Modbus - Wikipedia](https://en.wikipedia.org/wiki/Modbus)
[^5^]: [Understanding Modbus TCP-IP: An In depth Exploration](https://www.wevolver.com/article/understanding-modbus-tcp-ip-an-in-depth-exploration)

# 🤖 How to collect Modbus Data from Solar Panels/Inverters using Python and asyncio?
## 🌈 Collecting Modbus Data using Python and asyncio
To collect Modbus data from Solar Panels/Inverters using Python and asyncio, you can utilize libraries such as `pymodbus` or `minimalmodbus`. These libraries provide functions to establish a connection to the Modbus device and read data from it [^6^].

## 📚 Steps to Collect Modbus Data
Here are the steps to collect Modbus data using Python and asyncio:

1. Install the required libraries: `pip install pymodbus` or `pip install minimalmodbus`.
2. Import the necessary modules: `from pymodbus.client.asyncio import ModbusTCPClient` or `import minimalmodbus`.
3. Establish a Modbus TCP connection: `client = ModbusTCPClient(host='IP_ADDRESS', port=502)` or `instrument = minimalmodbus.Instrument('/dev/ttyUSB0', slaveaddress=1)`.
4. Read the desired Modbus registers: `response = await client.read_holding_registers(address, count)` or `value = instrument.read_register(register_address, number_of_decimals=0)`.
5. Process the received data: Extract the values from the response and perform any necessary computations or transformations.
6. Store the data in TimescaleDB: Use the TimescaleDB Python library to connect to the database and insert the data.


## 🔍 `pymodbus` and `minimalmodbus` in python
- **pymodbus**: pymodbus is a comprehensive Modbus protocol library that supports various Modbus variants[^1^]. It provides a wide range of features and has a larger community support[^1^][^6^].
- **minimalmodbus**: minimalmodbus is a lightweight and simpler Modbus library specifically designed for simple Modbus RTU and Modbus ASCII implementations in Python[^8^]. It is easy to use and suitable for basic Modbus communication[^8^].

## 🚀 Collecting Data from Solar Inverter using pymodbus
To collect data from a solar inverter using pymodbus library, you need to follow these steps:

1. Install the pymodbus library using pip: `pip install pymodbus`.
2. Import the necessary modules in your Python script: `from pymodbus.client.sync import ModbusSerialClient`.
3. Create a Modbus client object and connect it to the solar inverter: `client = ModbusSerialClient(method='rtu', port='/dev/ttyUSB0', baudrate=9600)`.
4. Read the desired Modbus registers from the solar inverter: `response = client.read_holding_registers(address, count)`.
5. Parse and process the retrieved data as per your requirements.

## 💾 Storing Data in TimescaleDB
To store the collected data in TimescaleDB, you can use the psycopg2 library to connect to the TimescaleDB database and execute SQL queries. Here are the steps to store the data:

1. Install the psycopg2 library using pip: `pip install psycopg2`.
2. Import the necessary modules in your Python script: `import psycopg2`.
3. Connect to the TimescaleDB database: `conn = psycopg2.connect(database="your_database", user="your_username", password="your_password", host="localhost", port="5432")`.
4. Create a cursor object to execute SQL queries: `cur = conn.cursor()`.
5. Insert the collected data into the TimescaleDB table using SQL insert queries: `cur.execute("INSERT INTO your_table (column1, column2, ...) VALUES (value1, value2, ...)")`.
6. Commit the changes to the database: `conn.commit()`.
7. Close the cursor and database connection: `cur.close()` and `conn.close()`.

> Note: The specific steps for connecting to and storing data in TimescaleDB may vary based on your setup and configuration.

## 🖥️ Code Sample - pymodbus + asyncio. 

Here's the updated Python code using dataclasses for YAML parsing and pandas for data formatting:

```python
import asyncio
import yaml
from dataclasses import dataclass
from pymodbus.client.sync import ModbusSerialClient
from pymodbus.constants import ModbusConstants
import pandas as pd
import psycopg2

@dataclass
class RegisterConfig:
    address: int
    count: int
    data_type: ModbusConstants
    unit: str = ""
    name: str = ""

@dataclass
class ModbusConfig:
    method: str
    port: str
    baudrate: int

@dataclass
class DatabaseConfig:
    name: str
    credentials: dict

@dataclass
class Config:
    modbus: ModbusConfig
    registers: list[RegisterConfig]
    database: DatabaseConfig
    interval: int

async def collect_data(config):
    with ModbusSerialClient(**config.modbus) as client:
        if not client.connect():
            return
        data = []
        for reg in config.registers:
            response = client.read_holding_registers(reg.address, reg.count)
            values = [convert_data(value, reg.data_type) for value in response.registers]
            data.extend(zip([reg.name] * reg.count, values))
        return pd.DataFrame(data, columns=["name", "value"])

def convert_data(value, data_type):
    if data_type == ModbusConstants.READ_HOLDING_REGISTERS:
        return value
    # Add conversion logic for other data types (e.g., READ_INPUT_REGISTERS, READ_COILS, etc.)
    # You can use libraries like `struct` for specific conversions.
    raise NotImplementedError(f"Data type conversion not implemented for {data_type}")

async def store_data(data, config):
    # ... (same logic as before, using pandas dataframe for data)

async def main():
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)
        config = Config(**config)  # Convert to dataclass object

    interval = config.interval
    while True:
        data = await collect_data(config)
        await store_data(data, config)
        await asyncio.sleep(interval)

if __name__ == "__main__":
    asyncio.run(main())
```

**Explanation:**

- **Dataclasses:** We define dataclasses for `RegisterConfig`, `ModbusConfig`, `DatabaseConfig`, and `Config` to hold configuration data with type hints.
- **`convert_data` function:** This function takes a register value and data type and converts it based on the Modbus constant. Currently, it only handles `READ_HOLDING_REGISTERS`, but you can add logic for other data types using libraries like `struct`.
- **Pandas Dataframe:** Collected data is formatted as a pandas dataframe with columns "name" and "value". This allows for easier manipulation and storage.
- **`store_data` function:** The logic for storing data needs modification to accept a pandas dataframe as input and iterate through it for insertion.

**Sample YAML (updated):**

```yaml
modbus:
    method: rtu
    port: /dev/ttyUSB0
    baudrate: 9600

registers:
  - address: 0
    count: 2
    data_type: 0x03  # READ_HOLDING_REGISTERS
    unit: "C"
    name: "Temperature"
  - address: 2
    count: 1
    data_type: 0x01  # READ_COILS (example of a different data type)
    name: "Switch Status"

database:
    name: your_database
    credentials:
        user: your_username
        password: your_password
        host: localhost
        port: 5432

interval: 10  # in seconds
```

**Note:**

- You'll need to modify the `store_data` function to work with the pandas dataframe.
- Add conversion logic for different Modbus data types in `convert_data`. 



## ⚡ Computing Total Energy Produced and Comparing Sunlight vs Power
To compute the total energy produced in a day and compare sunlight vs power during the day, you can use Python, pandas, scikit, numpy, and matplotlib libraries. Here are the steps:

1. Collect the data for sunlight and power measurements from the solar inverter.
2. Load the data into pandas DataFrame.
3. Preprocess the data by converting the timestamps to datetime objects and setting them as the index.
4. Compute the total energy produced by integrating the power values over time.
5. Visualize the comparison between sunlight and power using matplotlib.

> Note: The specific code implementation for computing total energy and comparing sunlight vs power may vary based on the structure and format of your data.

## 🤖 Comparison of OPC UA and MQTT for Data Collection in Industrial Settings
The research results provide new information on the comparison of OPC UA and MQTT for data collection in industrial settings. Here are the key findings:

- **OPC UA**: OPC UA (Unified Architecture) is a machine-to-machine communication protocol for industrial automation[^1^]. It provides a secure and reliable way to exchange data between different devices and systems in an industrial environment[^1^].
- **MQTT**: MQTT (Message Queuing Telemetry Transport) is a lightweight and publish-subscribe messaging protocol designed for constrained devices and low-bandwidth, high-latency networks[^1^]. It is widely used in IoT applications for efficient data transfer and real-time communication[^1^].

OPC UA and MQTT have different features and use cases in industrial settings. Here are some points of comparison:

- **Performance**: OPC UA offers higher performance and bandwidth efficiency compared to MQTT due to its binary encoding and optimized data transfer[^1^].
- **Scalability**: MQTT is more scalable as it follows a publish-subscribe model, allowing multiple clients to subscribe to relevant data topics[^1^].
- **Security**: OPC UA provides built-in security features such as authentication, encryption, and access control, making it suitable for secure industrial communication[^1^].
- **Data Exchange**: MQTT is lightweight and suitable for real-time data exchange, while OPC UA supports more complex data models and structured information exchange[^1^].

> Note: The specific comparison between OPC UA and MQTT may vary based on the industrial use case and requirements.

## REFERENCES:
[^1^]: [A Comparison of IIoT Protocols: MQTT Sparkplug vs OPC-UA | EMQ](https://www.emqx.com/en/blog/a-comparison-of-iiot-protocols-mqtt-sparkplug-vs-opc-ua)
[^2^]: [Semantic Interconnection Scheme for Industrial Wireless Sensor ...](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9606965/)
[^3^]: [Bridging OPC UA Data to MQTT for IIoT: A Step-by-Step Tutorial | EMQ](https://www.emqx.com/en/blog/bridging-opc-ua-data-to-mqtt-for-iiot)
[^4^]: [MQTT or OPC-UA | PLCS.net - Interactive Q & A](https://www.plctalk.net/threads/mqtt-or-opc-ua.124456/)
[^5^]: [OPC Unified Architecture Monitoring | InfluxData](https://www.influxdata.com/integration/opcua/)
[^6^]: [OPC UA alternatives (aka Kepserver)? - General Discussion ...](https://forum.inductiveautomation.com/t/opc-ua-alternatives-aka-kepserver/16962?page=2)
[^7^]: [A Comparison of OPC UA and MQTT Sparkplug](https://www.hivemq.com/resources/iiot-protocols-opc-ua-mqtt-sparkplug-comparison/)
[^8^]: [Performance Comparison Between OPC UA and MQTT for Data ...](https://www.semanticscholar.org/paper/Performance-Comparison-Between-OPC-UA-and-MQTT-for-Rocha-Sestito/f7fa37521cda4794e0401233a857950b16acfdfc)
[^9^]: [OPC UA, MQTT, and Apache Kafka - The Trinity of Data Streaming ...](https://www.kai-waehner.de/blog/2022/02/11/opc-ua-mqtt-apache-kafka-the-trinity-of-data-streaming-in-industrial-iot/)
[^10^]: [MQTT architecture - Ignition - Inductive Automation Forum](https://forum.inductiveautomation.com/t/mqtt-architecture/33441)

## 📚 Additional Resources
- A Google Groups post describes communication with a solar inverter and its smart meter via RS485 to obtain power, voltage, and current information [^2^].
- A Home Assistant community discussion provides configuration details for obtaining MODBUS data from an SMA inverter [^3^].
- An OpenHAB community thread discusses connecting a Goodwe solar panel inverter directly to OpenHAB using Python and asyncio [^3^].
- A Home Assistant community discussion mentions the use of a Python script to get data from Huawei solar inverters via Modbus [^3^].
- A Stack Overflow question asks about mimicking a Chint DDSU666 meter with Python and Modbus [^3^].
- A Domoticz forum thread discusses the local readout of a GoodWe inverter via Modbus using Python [^3^].
- The `sungrowinverter` library on PyPI enables communication with Sungrow inverters using Modbus TCP client [^3^].
- Stack Overflow has several questions and answers related to using pymodbus for asynchronous data writing to a Modbus device and working with solar inverters [^3^].
- A GitHub issue discusses the impact of adding GoodWe to Home Assistant on SEMS portal data uploads [^3^].
- The PyModbus documentation provides examples of how to parse Modbus messages using Python [^3^].

[^2^]: [Google Groups: async or sync clients and solar inverters](https://groups.google.com/g/pymodbus/c/ZS035SSbLk8)
[^3^]: [Research Result: GoogleSearchLinks "How to collect Modbus Data from Solar Panels/Inverters using Python and asyncio"]
[^6^]: [Research Result: GoogleSearchLinks "How to collect Modbus Data from Solar Panels/Inverters using Python and asyncio"]
