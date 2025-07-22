url = input()

protocol_split = url.split("://")

protocol = protocol_split[0]
del_protocol = protocol_split[1]

host = del_protocol.split("/")[0]
others = del_protocol.split("/", 1)[1]

print("protocol:", protocol)
print("host:", host)
print("others:", others)