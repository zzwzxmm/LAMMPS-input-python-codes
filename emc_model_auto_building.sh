#!/bin/bash

name = $1

while :
do
emc_linux64 $name.emc 2>&1 | tee build.out
grep "Program aborted" build.out
if [$? == 1]
then
echo "Success! Congrates!"
break
fi
echo "Not working, continuing ..."
sleep 10
done
