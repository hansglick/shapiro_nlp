FILENAME=$1
#OUTPUTFOLDER=$2

while read line

do

arrIN=(${line//;/ })
#myurl="https://www.youtube.com/watch?v=${arrIN[1]}"
#files_array+=($myurl)

echo "${arrIN[4]}"

done < $FILENAME