#!/usr/bin/env python


from __future__ import division, print_function
import pandas as pd
import glob


def parse_calendar(filename):
    '''Parse each calendar file'''
    columns = ['Date', 'Case Number', 'Title', 'Event', 'Court', 'Status']
    df = pd.DataFrame(columns=columns)
    with open(filename, 'r') as f:
        file_contents = f.read()
    file_contents_array = file_contents.split('<td class="Data">')[1:]
    new_row = {}
    i = 0
    for element in file_contents_array:
        value = element.split('<', 1)[0].strip()
        name = columns[i%6]
        new_row[name] = value
        if i%6 == 5:
            df = df.append(new_row, ignore_index=True)
            new_row = {}
        i+=1
    return df


def parse_calendars():
    '''Parse all the available calendar files'''
    df_full = pd.DataFrame()
    for calendar in glob.glob('./calendars/calendar_day_*_year_*.html'):
        print('Parsing file', calendar, '...')
        df = parse_calendar(calendar)
        df_full = df_full.append(df, ignore_index=True)
        print('...done.')
    return df_full


if __name__ == '__main__':
    df = parse_calendars()
    df.to_csv('calendars_parsed.csv', index=False)
