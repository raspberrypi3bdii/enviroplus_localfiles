#!/usr/bin/env python3
import time
# Name of the data_file is timestamp when script is executed
filename: str = time.strftime("%Y%m%d_%H%M%S")

print("Press Ctrl+C to exit\n")
variables = ["temperature",
             "pressure",
             "humidity",
             "light",
             "oxidised",
             "reduced",
             "nh3",
             "pm1",
             "pm25",
             "pm10",
             "time"]

# The main loop
try:
    muestra: int
    for muestra in range(3599):
        if muestra == 1:
            with open(filename, 'w') as f:
                f.write(variables.__str__()[1:-1])
                f.write("\n")

        else:
            # Cogemos los datos de los sensores (INT FIJOS PARA PRUEBA)
            temp = 35.12
            pressure = 935
            humidity = 30
            oxidising = 13
            reducing = 16
            nh3 = 66
            pm1 = 1
            pm25 = 2.5
            pm10 = 10
            sampletime = time.strftime("%Y%m%d_%H%M%S")
            #
            datos =[temp,
                    pressure,
                    humidity,
                    oxidising,
                    reducing,
                    nh3,
                    pm1,
                    pm25,
                    pm10,
                    sampletime]
            print(muestra)
            time.sleep(1)
            with open(filename, 'a') as f:
                f.write(datos.__str__()[1:-1])
                f.write("\n")
            f.close()

# Exit cleanly
except KeyboardInterrupt:
    sys.exit(0)