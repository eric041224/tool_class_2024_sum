#!/bin/bash

number=$(shuf -i 1-10 -n 1)
while [[ $num -ne $number ]] do
echo "请输入1-10之间的数字"
read num
if [[ $num -eq $number ]];then
	echo "恭喜你猜对了"
elif [[ $num -lt $number ]];then
	echo "猜小了"
else
	echo "猜大了"
fi
done