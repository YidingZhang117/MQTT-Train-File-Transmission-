# coding: utf-8
import paho.mqtt.client as mqtt

result = {}


def on_connect(client, userdata, flags, rc):
    print("Connected")
    client.subscribe("file")


def on_message(client, userdata, msg):
    # print(msg.topic + " " + str(msg.payload))
    content = str(msg.payload)#[2:-1]
    symbol = content.split("###")[0]
    if symbol == "end":
        text = content.split("###")[1]
        f = open("result/"+text, "wb")
        for l in result[text]:
            f.write(l)
        f.close()
        return
    elif symbol not in result:
        result[symbol] = []
    num = len(symbol)+3
    text = msg.payload[num:]
    print(text)
    result[symbol].append(text)


if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect("127.0.0.1", 1883, 60)
        client.loop_forever()
    except KeyboardInterrupt:
        print(result)
        client.disconnect()