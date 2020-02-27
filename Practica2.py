import os
hostname = "www.itmorelia.edu.mx"
respuesta = os.system("ping -c 1 " + hostname)
if respuesta == 0:
    print(hostname + ": esta en funcionamiento")
else:
    print(hostname + ": no funciona")

red = "200.33.171.0/24"
os.system("nmap -sP " + red)


#PING denebvirtual.itmorelia.edu.mx (200.33.171.77) 56(84) bytes of data.
#64 bytes from denebvirtual.itmorelia.edu.mx (200.33.171.77): icmp_seq=1 ttl=63 time=5.97 ms

#--- denebvirtual.itmorelia.edu.mx ping statistics ---
#1 packets transmitted, 1 received, 0% packet loss, time 0ms
#rtt min/avg/max/mdev = 5.977/5.977/5.977/0.000 ms
#www.itmorelia.edu.mx: esta en funcionamiento


#Starting Nmap 7.60 ( https://nmap.org ) at 2020-02-27 11:45 CST
#Nmap scan report for mail.itmorelia.edu.mx (200.33.171.3)
#Host is up (0.0028s latency).
#Nmap scan report for 200.33.171.13
#Host is up (0.0046s latency).
#Nmap scan report for libra.itmorelia.edu.mx (200.33.171.54)
#Host is up (0.0026s latency).---------------
#Nmap scan report for sagitario.itmorelia.edu.mx (200.33.171.65)
#Host is up (0.0035s latency).
#Nmap scan report for 200.33.171.66
#Host is up (0.0033s latency).
#Nmap scan report for 200.33.171.86
#Host is up (0.0041s latency).
#Nmap scan report for 200.33.171.99
#Host is up (0.0057s latency).
#Nmap scan report for 200.33.171.115
#Host is up (0.0036s latency).
#Nmap scan report for 200.33.171.120
#Host is up (0.0040s latency).
#Nmap done: 256 IP addresses (9 hosts up) scanned in 4.04 seconds
