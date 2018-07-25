# coding: utf-8
import paho.mqtt.client as mqtt

result = {}#result is a dicitonary
print(type(result))

def on_connect(client, userdata, flags, rc):
    print("Connected")
    client.subscribe("sensor")


def on_message(client, userdata, msg):
    # print(msg.topic + " " + str(msg.payload))
    # print(type(msg.payload))    
    # print(str(msg.payload))
    # content = str(msg.payload)[2:-1]   # if use linux
    #convert msg.payload to str so that splict function can be used
    #content = str(msg.payload)    
    content = msg.payload
    #print(content)
    symbol = content.split("###")[0]#symbol tells you where the element are from (namely list1 or list2)
    #print(symbol)
    if symbol not in result:
        result[symbol] = []#construct a key for dictionary 
    num = content.split("###")[1]
    #print(num)
    result[symbol].append(num)#add num to result[symbol]
    print(result)


if __name__ == '__main__':
    #
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect("127.0.0.1", 1883, 60)
        client.loop_forever()
    except KeyboardInterrupt:
        print(result)
        client.disconnect()