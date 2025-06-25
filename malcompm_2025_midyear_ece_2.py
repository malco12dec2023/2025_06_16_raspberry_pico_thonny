#Final Step. Development Procedure
"""
Steps 1 - 3: Thonny IDE and Postman IDE
Steps 4 - 6: Android Studio IDE
"""

#1.	Open your code in Thonny IDE, and “Save As” main.py in your Pico W.
#2.	Modify the python code related to the following block of codes …

WIFI_SSID = "HUAWEI-411C"
WIFI_PASS = "a0yy8334"

ip = connect_to_wifi(WIFI_SSID, WIFI_PASS)
kimi_no_nawa = "MP MALCO"
print("\n")
print("Performer:", kimi_no_nawa)
if(ip is not None):
    print("\nConnected ka na sa network!")
    print("Ang iyong IP address ay:", ip, "\n")
else:
    print("\nDi konektado!\n")
    while(ip is None):
        print("\nKonekting ulit...\n")
        ip = connect_to_wifi(WIFI_SSID, WIFI_PASS)
        delay(3)

#3.	Add the new block of codes before server.run() and test via Postman IDE.

hw_main = led_internal_main
""" dataMain, dataUna, dataPangalawa"""
@server.route("/api/pagsend-ng-tatlong-data", methods=["POST"])
def dalawangDataSignal(request):
    print("\nHTTP POST request received.")
    
    try:
        aking_data_main = request.data["dataMain"]
        print("\tPico received data (dataMain):", aking_data_main)
        if(aking_data_main == "On"):
            hw_main.value(1)
        else:
            hw_main.value(0)
    except:
        print("\tPico received data (dataMain):", "Wala talaga, as in wala.")

    try:
        aking_data_una=request.data["dataUna"]
        print("\tPico received data (dataUna):", aking_data_una)
        if(aking_data_una == "On"):
            hw_uno.value(1)
        else:
            hw_uno.value(0)
    except:
        print("\tPico received data (dataUna):", "Wala talaga, as in wala.")

    try:
        aking_data_pangalawa=request.data["dataPangalawa"]
        print("\tPico received data (main):", aking_data_pangalawa)
        if(aking_data_pangalawa == "On"):
            hw_dos.value(1)
        else:
            hw_dos.value(0)
    except:
        print("\tPico received data (dataPangalawa):", "Wala talaga, as in wala.")
        
        #return json.dumps({"message" : "Command sent successfully!"}), 200, {"Content-Type": "application/json"}
    
    diksyonaryo = dict()
    try:
        diksyonaryo["msg_"]= "Command sent successfully!"
        diksyonaryo["msg_0"]= aking_data_main
        diksyonaryo["msg_1"]= aking_data_una
        diksyonaryo["msg_2"]= aking_data_pangalawa
    except:
        diksyonaryo["msg_"]= "Command not processed!"
        
    print("\nSending response.", diksyonaryo, "\n")
        
    return json.dumps(diksyonaryo), 200, {"Content-Type": "application/json"}
