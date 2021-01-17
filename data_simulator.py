import os
import time
import random
import schedule
import pandas as pd

obd_data = pd.read_csv("obd_data.csv")

data_index = 0
data = {}
images = {}


def data_sim():
    global data_index
    global data
    data = obd_data.iloc[data_index].to_dict()
    print(data)


def main():
    global data_index
    schedule.every(random.randint(10, 50)).seconds.do(data_sim)

    while True:
        schedule.run_pending()
        time.sleep(1)
        data_index += 1


main()
