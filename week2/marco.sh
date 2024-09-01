#!/bin/bash

marco(){
	echo "$(pwd)" > C:/Users/19355/Desktop/大二暑假/系统开发工具基础/1/tool_class_2024_sum/week2/history.log
	echo "已保存目录"
}

polo(){
	cd "$(cat  C:/Users/19355/Desktop/大二暑假/系统开发工具基础/1/tool_class_2024_sum/week2/history.log)"
}
