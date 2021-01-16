FILENAME=$1
OUTPUTFOLDER=$2

while read line

do

arrIN=(${line//;/ })
python dwl_comments.py --youtubeid  "${arrIN[4]}" --output "${OUTPUTFOLDER}/${arrIN[4]}.json"

done < $FILENAME