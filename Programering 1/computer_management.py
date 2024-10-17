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
        

def change_service_choice():
    service_choice = input (f"vill du ta bort en dator från service list? ")
    if service_choice == "ja":
        service_choice = input (f"vilken dator vill du ta bort {service_list} ")
        if service_choice in service_list:
            service_list.remove(service_choice)
            computer_list.append(service_choice)
            pc_serviced -=1
        else:
            service_choice = input (f"denna dator existerar inte vilken dator vill du ta bort {service_list} ")
        return computer_list, service_choice, service_list


pc_serviced = 0

while pc_serviced < 2:
    service_choice = input (f"vilken dator ska få service? {computer_list} ")
    if service_choice in service_list or service_choice in computer_list:
        time.sleep(1)
        service_list.append(service_choice)
        computer_list.remove(service_choice)
        pc_serviced +=1
    else:
        service_choice = input (f"denn dator existerar inte vilken dator ska få service? {computer_list} ")
    print (f"\n\ncomputers in the service list: {service_list}\n")
    time.sleep(3)
    print (f"all computers: {computer_list}\n\n")
    time.sleep(3)

    if pc_serviced >= 1:
        change_service_choice()
        time.sleep(1)


