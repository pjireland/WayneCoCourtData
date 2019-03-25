#!/bin/bash

if [ "$#" -ne 1 ]
then
  echo "The following value needs to be passed when calling this script:"
  echo "bash get_court_reports.sh <YEAR>"
  exit 1
fi

year="$1"

# Account for leap years
if [ $(( $year % 4 )) -eq 0 ]
then
    days=366
else
    days=365
fi

declare -a courtIds=("181908911" "181908931" "181908932" "181908933")
echo "Downloading calendars"
echo "---------------------"
for day in $(seq 1 $days)
do
    echo "Day=${day}"
    dayFormatted=$(printf "%03d" $day)

    for courtId in "${courtIds[@]}"
    do
        file_in="https://www.doxpop.com/prod/in/court/Calendar?action=GET-VIEW-COURT&period=DAY&day=${day}&year=${year}&court_id=${courtId}"
        file_out="./calendars/calendar_day_${dayFormatted}_year_${year}_${courtId}.html"
        curl $file_in > $file_out
    done
done

echo "Done."
