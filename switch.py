import json
import time
from env import ENDPOINT, ACCESS_ID, ACCESS_KEY, USERNAME, PASSWORD, DEVICE_ID, DEVICE_ID2, DEVICE_ID3
from tuya_iot import TuyaOpenAPI
from datetime import datetime
from requests import get

openapi = TuyaOpenAPI(ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.login(USERNAME, PASSWORD)

while True:
    try:
        result = openapi.get("/v1.0/iot-03/devices/{}/status".format(DEVICE_ID))
        cur_power = result['result'][4]
        current_time = datetime.now()
        time_stamp = current_time
        str_date_time = time_stamp.strftime("- %d-%m-%Y, %H:%M:%S")
        print(cur_power, str_date_time)

        with open('result_log.json', 'a') as f:
            f.write(json.dumps(cur_power))
            f.write(json.dumps(str_date_time) + '\n')
    except Exception as e:
        print("Erro ao obter o resultado do dispositivo 1:", str(e))

    try:
        result2 = openapi.get("/v1.0/iot-03/devices/{}/status".format(DEVICE_ID2))
        cur_power2 = result2['result'][4]
        current_time2 = datetime.now()
        time_stamp2 = current_time2
        str_date_time2 = time_stamp.strftime("- %d-%m-%Y, %H:%M:%S")
        print(cur_power2, str_date_time2)

        with open('result_log.json2', 'a') as f:
            f.write(json.dumps(cur_power2))
            f.write(json.dumps(str_date_time2) + '\n')
    except Exception as e:
        print("Erro ao obter o resultado do dispositivo 2:", str(e))

    try:
        result3 = openapi.get("/v1.0/iot-03/devices/{}/status".format(DEVICE_ID3))
        cur_power3 = result3['result'][4]
        current_time3 = datetime.now()
        time_stamp3 = current_time3
        str_date_time3 = time_stamp.strftime("- %d-%m-%Y, %H:%M:%S")
        print(cur_power3, str_date_time3)

        with open('result_log.json3', 'a') as f:
            f.write(json.dumps(cur_power3))
            f.write(json.dumps(str_date_time3) + '\n')
    except Exception as e:
        print("Erro ao obter o resultado do dispositivo 3:", str(e))

    time.sleep(10)
