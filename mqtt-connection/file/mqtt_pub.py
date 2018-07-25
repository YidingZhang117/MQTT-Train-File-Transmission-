import paho.mqtt.publish as publish

HOST = "127.0.0.1"
PORT = 1883

if __name__ == '__main__':
    name = "1.png"
    # print(name)
    f = open(name, 'rb')
    print(f)
    msgs = []
    for l in f.readlines():
        l = l.strip()
        msgs.append({'topic':"file", 'payload': name+"###"+l})
    msgs.append({'topic':"file", 'payload': "end###"+name})
    print(msgs)
    msgs.reverse()
    f.close()
    publish.multiple(msgs, hostname=HOST, port=PORT)



