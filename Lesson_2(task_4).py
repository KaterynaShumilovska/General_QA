#Task 4.1
nat = 'ip nat inside source list ACL interface FastEthernet0/1 overload'
print(nat.replace('Fast', 'Gigabit'))

#Task 4.2
mac = 'AAAA:BBBB:CCCC'
print(mac.replace(':', '.'))

#Task 4.3
config = "switchport trunk allowed vlan 1,3,10,20,30,100"
vs = config.split()
result = vs[4].split(",")
print(result)

#Task 4.4
vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
u = list(set(vlans))
result = sorted(u)
print(result)

#Task 4.5
command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
vs1 = command1.split()
vs2 = command2.split()
vm1= vs1[-1].split(",")
vm2= vs2[-1].split(",")
result = sorted(list(set(vm1) & set(vm2)))
print(result)

#Task 4.6
names_par = ['Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface']
ospf_route = "10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
ospf_route_a = ospf_route.replace(',', '').split()
ospf_route_a.pop(2)
for n, o in zip(names_par, ospf_route_a):
    print(f'{n}'.ljust(20, ' '), f'{o}')

#Task 4.7
mac = "AAAA:BBBB:CCCC"
m = bin(int(mac.replace(':', ''), 16))
result = str(m.replace('0b', ''))
print(result)

#Task 4.8
ip = "192.168.3.1"
ip_1 = ip.split('.')
print(f'{ip_1[0]}'.ljust(10, ' '),f'{ip_1[1]}'.ljust(10, ' '), f'{ip_1[2]}'.ljust(10, ' '), f'{ip_1[3]}'.ljust(10, ' '))
print(f'{int(ip_1[0]):08b}'.ljust(10, ' '), f'{int(ip_1[1]):08b}'.ljust(10, ' '), f'{int(ip_1[2]):08b}'.ljust(10, ' '), f'{int(ip_1[3]):08b}'.ljust(10, ' '),)
