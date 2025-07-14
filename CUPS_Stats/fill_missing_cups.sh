#!/bin/bash
#link fesc 10 with stdin
exec 10<&0
#declare arrays
declare -a cup_cnt
declare -a cup_cid
declare -a fcid
declare -a fcnt
declare -a acid1
declare -a acid2
declare -a acid
#file supplied as a first argument
exec < $1

let count=1

while read cnt cid; do
   cup_cnt[$count]=$cnt
   cup_cid[$count]=$cid
   ((count++))
done

acid2=(221 222 295 296 297 298 299 300 301 302 303 304 305 358)
for ((i=1;i<=166;i++)); do
   acid1[i]=$i
done
acid=("${acid1[@]}" "${acid2[@]}")
#echo ${acid[@]} ${#acid[@]}

#printf '%s\n' "${cup_cnt[@]}"
#printf '%s\n' "${cup_cid[@]}"
elements=${#cup_cid[@]}
echo  $elements 'lines'

for (( i=1; i<=180; i++ )); do
### decimal umbers with leading zeros # i=$((10#$i))
declare -a arr
    if (( $((10#${cup_cid[$i]})) != $i )); then 

	echo "${cup_cid[$i]}",,,$i
          arr=("${cup_cid[@]:0:i-1}")           ### take the start of the array.

	if (( $i <= 9 )); then
          arr+=( "00$i" )                       ### add a new value
	elif (( $i <= 99 )); then
	  arr+=( "0$i" )
	else
	  arr+=( "$i" )
	fi

          arr+=( "${cup_cid[@]:i}" )             ### copy the tail of the array.

          echo "head $i ${cup_cid[@]:0:i-1}"    ### see the array.
#          echo "tail $i ${cup_cid[@]:i}"        ### see the array.

          cup_cid=( "${arr[@]}" )                ### transfer the corrected array.
#	echo  "${#cup_cid[@]}"
    fi
done

#
#if [[ $((10#${cup_cid[$i]})) -le 166 ]]; then
#   if [[ "${cup_cid[@]}" =~ "$i" ]]; then
#      fcid+=($i)
#   else
#      fcid+=("0")
#   fi
#else  fcid+=(${cup_cid[$i]})
#fi
#

element2=${#fcid[@]}
#printf '<%s>\n' "${fcid[@]}"
echo $element2 'lines'


#restore stdin from fdesc 10 and close fdesc 10
exec 0<&10 10<&-

