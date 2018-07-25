from functools import partial
import paho.mqtt.publish as publish

HOST = "127.0.0.1"
PORT = 1883
if __name__ == '__main__':
    name = "1.png"
    f = open(name, 'rb')
    # print(f)
    print(type(f))
    content = iter(partial(f.read, 20), b'')    
    msgs = []
    s = bytes(name+"###")
    for l in content:
        print(l)
        msgs.append({'topic':"file", 'payload': s+l})
    msgs.append({'topic':"file", 'payload': "end###"+name})
    # print(msgs)
    msgs.reverse()
    f.close()
    # publish.multiple(msgs, hostname=HOST, port=PORT)