youtube-dl --ignore-errors --get-filename --skip-download  -o "%(upload_date)s;%(view_count)s;%(like_count)s;%(dislike_count)s;%(id)s;%(duration)s;%(title)s" $1 >> $2
