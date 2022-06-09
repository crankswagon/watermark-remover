## brew install coreutils

for i in $(seq 1 5000 | shuf)
do
    photo_id=9374420
    cur_id=$(expr $photo_id + $i)
    echo "getting photo $cur_id"
    wget -d --header="User-Agent: Mozilla/5.0" https://images.pexels.com/photos/$cur_id/pexels-photo-$cur_id.jpeg -P ./dataset/train/
done
