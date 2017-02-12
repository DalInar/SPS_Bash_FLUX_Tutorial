#!/bin/bash

for month in {Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec,Obi}; do
	days=0
	if [ $month = Jan -o $month = Mar -o $month = May -o $month = Jul -o $month = Aug -o $month = Oct -o $month = Dec ]; then
		days=31
	elif [ $month = Apr -o $month = Jun -o $month = Sep -o $month = Nov ]; then
		days=30
	elif [ $month = Feb ]; then
		days=28
	else
		echo "This is not a month: " $month
		continue 
	fi
	
	mkdir -p months/${month}
	echo ${month} has ${days} days > months/${month}/days.dat
	cat months/${month}/days.dat
done
