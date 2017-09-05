import csv
from datetime import datetime
from matplotlib import pyplot as plt


filename = 'death_valley_2014.csv'
with open(filename) as f:
    # get highest temperature from csv file
    reader = csv.reader(f)
    header_row = next(reader)

    # first row title
    # print("The first row:")
    # for index,column_header in enumerate(header_row):
    #     print(index, column_header)

    # highest temperature every day
    dates, highs, lows = [], [], []
    current_date = ''
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # create figure with data
    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(dates, highs, c='red')
    plt.plot(dates, lows, c='blue')
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # format the figure
    plt.title("Daily high and low temperatures,2014\nDeath Vally", fontsize=24)
    plt.xlabel('',fontsize=14)
    fig.autofmt_xdate() #日期倾斜
    plt.ylabel('Temperature (F)', fontsize=14)
    plt.tick_params(axis='both', which='major', labelsize=14)

    plt.show()


