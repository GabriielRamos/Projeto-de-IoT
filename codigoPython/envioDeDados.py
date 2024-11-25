import serial
import requests
import time

portaArduino = "COM4"
taxaBauds = 9600
apiKey = "YAGJVNL351FCX6XY"
urlThingSpeak = "https://api.thingspeak.com/update"

try:
    ser = serial.Serial(portaArduino, taxaBauds)
    print("Conexão com Arduino estabelecida na porta", portaArduino)

    while True:
        if ser.in_waiting > 0:
            dadoSerial = ser.readline().decode('utf-8').strip()
            print("Dado recebido do Arduino:", dadoSerial)

            if "Nível do Gás:" in dadoSerial:
                nivelGas = int(dadoSerial.split(":")[1].strip())
                print("Nível do Gás extraído:", nivelGas)

                parametros = {
                    "api_key": apiKey,
                    "field1": nivelGas
                }

                resposta = requests.get(urlThingSpeak, params=parametros)

                if resposta.status_code == 200:
                    print("Dados enviados para o ThingSpeak com sucesso!")
                else:
                    print("Erro ao enviar dados para o ThingSpeak:", resposta.status_code)
            
            time.sleep(5)

except serial.SerialException as e:
    print("Erro ao conectar ao Arduino:", e)

except KeyboardInterrupt:
    print("Programa interrompido pelo usuário.")

finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print("Conexão com o Arduino fechada.")