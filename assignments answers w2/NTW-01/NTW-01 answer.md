# OSI stack
Study about the OSI model and the TCP/IP model.

## Key terminology
- i will explain most keyterms in sources




## Exercise
### Sources
1. [OSI layers](https://linuxhint.com/network-osi-layers-explained/#:~:text=Open%20System%20Interconnection%20OSI%20model,performed%20on%20each%20abstract%20layer.)
2. ![SS of layers](../../00_includes/NTW-01/7layers.png)
3. [OSI model](https://www.linux.org/threads/open-systems-interconnect-osi-model.9095/)
4. [Intranet](https://www.techtarget.com/whatis/definition/intranet)


### Overcome challenges
Deze opdracht is voor mij alleen maar lezen. Voor mezelf de opdracht gemaakt schrijf op en leg uit wat je begrijpt. Dat zijn alle 2 niet mijn sterkste punten. Ik leer veel beter met praktische opdrachten.


### Results

- ### The OSI model
1. **Layer 7 (Application layer):** This is the layer closest to the user and as the name of the layer suggests, it is the layer that displays the data, it is also the only layer that has direct interaction with the user. Layer 7 creates connections between the end to end users, a example for this is "HTTP". HTTP enables internet connection.

2. **Layer 6 (presentation layer):** This layer Compresses date it gets from layer 7 making the data smaller and creating more efficient communincation. This also goes the other way, when this layer receives compressed data it translates/converts it and makes it presentable for layer 7.

3. **Layer 5 (Session layer):** This layer is the control  layer of the connetions, these connections between devices are called "sessions". The session layer works efficiently by only keeping a session open when data is being exchanged and closing it when the exchange is done. To make this safe the layer applies checkpoints to the data exchange, when the exchange is interupted it can continue from a checkpoint instead of starting over. The layer also determs if the transmission is "full or half duplex". 
- Full duplex means that both ends can send and receive at the same time, think about phone conversation, both persons can talk and listen at the same time.
- Half duplex means that only 1 end can talk and the other end can only receive at the same time, think about a walkie talkie, when one talks the other one can only listen.

4. **Layer 4 (Transport layer):** This layer as the name suggests is in control of data transport, this works in 2 ways. When it receives data from layer 6 is breaks this data into smaller bits called "segments" and sends these to layer 3 (the network layer). The other way around is when it receives segments from layer 3 it reassembles these segments before sending them to layer 5. This layer applies Flow and Error control.
- Error control, on the receivers end this makes sure the data is send and received correctly, if not it will request a re transmission.
- Flow control, on the senders end flow control makes sure the receiver is not flooded. For example when the sender has a quicker connection than the receiver the flow control will match the transmission speed to the speed of the receiver. This creates a optimal data transmission.

    Layer 4 is also where the adressing occurs, this in done in protocols TCP/IP is a example protocol more about this later.

5. **Layer 3 (Network layer):** When this layer receives segments from layer 4 it splits them into even smaller units called "packets", the destination is also in these packets. When this layer receiver packets it will reasemmble then into segments again. The network layer ALWAYS ensures data is transported in the most efficient way. Out of a billion options this layer will identify the most efficient one, this is called routing. The destinations for these packets can be "LAN" or "WAN".
- LAN, Local Area Network. If the destination is same LAN the destination adress will be copied from layer 4.
- WAN, Wide Area Network. If the destination is WAN the packets will be send to a gateway (for example a router), in this case the destination should always be the receivers gateway adress since it has to go to a different LAN. When the destinated "router" receives the packets it will transmit them to the LAN.

6. **layer 2 (Data Link):** 