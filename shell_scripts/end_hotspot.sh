#!/bin/sh


cat process.txt | while read line
do
  sudo kill $line
done

rm -f process.txt