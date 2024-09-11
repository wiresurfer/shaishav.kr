# Data Ingestion in Industrial IoT

## From Edge to Cloud data warehouses

### Understanding data ingestion

Data Ingestion != Data collection.  Collection teaches us how to talk industrial protocols.  Ingestion defines when and how much to collect and where to send/store it afterwards.

Sampling of data requirement.  Nyquist-Shannon sampling theorem and its impact on datapoints recorded based on application

- Constant rate collection at low frequency - energy consumption
- High freq collection  for short duration  at  repeating intervals.  For eg motor/gearbox rotational wear/tear
- event triggered collection.

Tradeoffs and impact on network bandwidth/storage.

Storage/transport considerations
- Tackling collector failures/power outages.  How much are we ok with loosing data points.  mission critical [for alerts] or vanity/accounting metric [like kwh in 10mins]
- Edge caching on collector, on edge server or fire-and-forget to cloud.
- FS at collector is always a good place to write first.  Many a slip between the cup and the lip.
- Compression, batching and transmission.  Transmission requires network and consumes power. the lesser times we emit, and the more compact our emission, the more efficient our pipeline
- Energy consumption becomes vitally important when your collector runs on battery, or needs to use battery as a backup power source.

Retransmission and ACKS - Protocol to glue cloud and device.
- protocol level retries and acknowledges. MQTT QoS, or use Kafka/RabbitMQ/Cloud PubSub.
- Mqtt gives flexibility, support even on embedded devices and OTB support in lots of industrial Iot equipment.
- Other MQs your milege may wary.
- Don't sweat this detail out, protocol conversion is possible, off the shelf components can handle workable scales. like telegraph, fluentd, etc.
- Message queues on the cloud-receiving end.
  - Can take large throughput, offer acks on receive, have different guarantees that can be enforces, atmost once, atleast once delivery.  Can be sharded and scaled
  - Same data, multiple consumers - for eg. data warehouse writer + alerts engine +  live dashboards could use the same stream but for different outcomes.

This phase ends at collection and one key decision is the protocol used for transmission between edge and cloud. and possibly a message queue to spread incoming messages to your consumers.
MQTT is a good starting point. Don't sweat this too much.   MQTT between edge/cloud,  Dumb Protocol conversion and routing on cloud boundary to a Pub/Sub message queue,  Datawarehouse writers as consumers of PubSub channels.

### Build vs Buy

Talk about complexity of building all these components inhouse. atleast an edge collector, a receiving infra, and a datawarehouse consumer.

Cloud offerings by  Public cloud players.
- Cloud IoT offerings - ties you to the product spec. Good to launch quickly, can be constraining if you have niche collection requirements.
- Custom edge collection with Cloud MessageQueue + DataWarehouse ala-carte. Best of both worlds.  Use something like Google PubSub with Google BigQuery/Cloud Storage.  You control ingestion and storage schema, Cloud gives you scale.  Can outlast most companies 3-5 year requirements if done right.
- Custom everything - You better have a good development as well as devops teams. Preferable if you are in your post PMF, scaling phase.

## 🤖 Advantages and Disadvantages of Using MQTT in Industrial Automation

-   MQTT (Message Queuing Telemetry Transport) is a lightweight messaging
    protocol used in IoT applications, which can also be utilized in industrial
    automation systems.
-   Advantages of using MQTT in industrial automation include [^1^]:
    -   Low Bandwidth: MQTT is designed to be efficient in terms of bandwidth
        usage, making it suitable for low-power and low-bandwidth environments.
    -   Asynchronous Communication: MQTT enables asynchronous communication
        between devices, allowing for better scalability and responsiveness.
    -   Flexibility: MQTT supports both point-to-point and publish-subscribe
        communication models, providing flexibility in system architecture
        design.
    -   Decoupling: MQTT decouples the sender and receiver, allowing devices to
        communicate without being directly connected.
-   Disadvantages of using MQTT in industrial automation include [^1^]:
    -   Reliability: MQTT relies on the underlying network infrastructure, and
        if the network connection is unstable, message delivery may be affected.
    -   QoS Trade-off: MQTT offers different levels of Quality of Service (QoS),
        but higher QoS levels may result in increased network traffic and
        latency.
    -   Security Considerations: MQTT does not inherently provide encryption or
        authentication mechanisms, so additional security measures must be
        implemented to ensure secure communication.

## Footnotes

🔖 References 
[^1^]: [Vladimir Romanov on LinkedIn: #software #automation #mqtt ...](https://www.linkedin.com/posts/vladromanov_software-automation-mqtt-activity-7100461748494704640-Ju-l)
