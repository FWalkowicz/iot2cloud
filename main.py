# Importowanie bibliotek
import Adafruit_DHT
import time
from azure.iot.device import IoTHubDeviceClient, Message

# Definiowanie czujnika
sensor = Adafruit_DHT.DHT11
pin = 17

# Zmienne do polaczenia z chmura
CONNECTION_STRING = " XXXX "
MSG_SND = '{{" temperature ": { temperature } ," humidity ": { humidity }}}'


# Tworzenie klienta
def iothub_client_init():
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client


# Zczytywanie danych z czujnika oraz wysylanie
def iothub_client_telemetry_sample_run():
    try:
        client = iothub_client_init()
        print(" Sending data to IoT Hub , press Ctrl - C to exit ")
        while True:
            humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
            msg_txt_formatted = MSG_SND.format(
                temperature=temperature, humidity=humidity
            )
            message = Message(msg_txt_formatted)
            print("Sending message : {} ".format(message))
            client.send_message(message)
            print("Message successfully sent")
            time.sleep(10)
    except KeyboardInterrupt:
        print("IoTHubClient stopped")


# Start programu
if __name__ == "__main__":
    print("Press Ctrl - C to exit")
    iothub_client_telemetry_sample_run()
