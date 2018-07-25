import paho.mqtt.publish as publish

HOST = "127.0.0.1"
PORT = 1883

if __name__ == '__main__':
    a = [1,2,3,4,5]
    b = [6,7,8,9,10]
    #save a and b as a dictionary with key of "list1" and "list2"
    all_list = {"list1":a, "list2":b}
    #key represents key of the dictionary while l is th value
    for key, l in all_list.items():
        #construct a list msgs in which the elements are dictionary for every value in list a or b
        msgs = []
        #reverse the list l 
        l.reverse()
        #num is a element in a or b
        for num in l:
            #add additional information to each element in a list 
            #then connect all the elements of the list a or b
            msgs.append({'topic':"sensor", 'payload': key+"###"+str(num)})
        #now msgs is a list containning all the element of the list a or b
        print(msgs)
        #publish the list a or b in one time
        #hence, to publish the two list a and b, we need to publish twice.
        publish.multiple(msgs, hostname=HOST, port=PORT)