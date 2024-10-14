#input för vilken dator som ska service(användaren skriver med sifforr)
#efter 3 datorer ska programmet avslutas
import time
computer_list = [
    "stationär dator 1",
    "stationär dator 2",
    "server",
    "receptions dator",
    "mötesrumsdator",
    "testdator",
    "grafikdator",
    "skrivardator",
    "utvecklingsdator",
    "backup dator",
]
service_list = []

pc_serviced = 0
while pc_serviced < 3:
    service_choice = input (f"vilken dator ska få service? {computer_list} ")
    time.sleep(1)
    service_list.append(service_choice)
    computer_list.remove(service_choice)
    print (f"\n\ncomputers in the service list: {service_list}\n")
    time.sleep(3)
    print (f"all computers: {computer_list}\n\n")
    time.sleep(3)
    pc_serviced+=1
    if pc_serviced > 1:
        service_choice = input (f"vill du ta bort en dator från service list")


