__author__ = 'ben'
import billboard
import time
import csv
import datetime
chart = billboard.ChartData('hot-100')
print(chart)


def get_every_week():
    time_start = datetime.datetime(year=2000, month=1, day=1)
    time_inc = datetime.timedelta(days=7)
    time_now = datetime.datetime.now()
    current_time = time_start
    times = []
    while current_time < time_now:
        times.append(current_time)
        current_time += time_inc
    return times

def get_and_save_all_songs():
    with open('MusioDatabase.csv', 'wb') as csvfile:
        data_writer = csv.writer(csvfile, delimiter='\t')
        query_weeks = get_every_week()
        for weeknum, week in enumerate(query_weeks):
            query_week = week.strftime('%Y-%m-%d')
            chart = billboard.ChartData('hot-100', query_week)
            for song in chart:
                row = [song.title,song.artist, song.weeks, song.rank, query_week,weeknum]
                data_writer.writerow(row)
    csvfile.close()



get_and_save_all_songs()











