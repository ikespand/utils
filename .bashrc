#!/bin/bash

## Mapping up and down arrow in the bash for history
bind '"\e[A": history-search-backward'
bind '"\e[B": history-search-forward'

## Aliases for simpler life
# Always open spyder in current directory
alias spyder='spyder -w .'
alias gs='git status'

## Echo few things which I often forget
echo -e "-------------------------------System Information----------------------------"
echo -e "Hostname:\t\t"`hostname`
echo -e "Kernel:\t\t\t"`uname -r`
echo -e "Architecture:\t\t"`arch`
echo -e "Processor Name:\t\t"`awk -F':' '/^model name/ {print $2}' /proc/cpuinfo | uniq | sed -e 's/^[ \t]*//'`
echo ""
echo -e "-------------------------------CPU/Memory Usage------------------------------"
echo -e "CPU Usage:\t"`cat /proc/stat | awk '/cpu/{printf("%.2f%\n"), ($2+$4)*100/($2+$4+$5)}' |  awk '{print $0}' | head -1`
echo ""
echo -e "-------------------------------Disk Usage-------------------------------"
df -Ph | sed s/%//g | awk '{ if($5 > 80) print $0;}'
echo ""
echo -e "-------------------------------Present Directory-------------------------------"
echo $PWD
echo ""


## API KEYS
export MAPBOX_API_KEY="MAPBOX_API_KEY" 