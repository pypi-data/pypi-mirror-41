while ((1))
do
    python3 -u crawl_combasic.py >> crawl_combasic.log  &
    sleep 20s 
 
    python3 -u crawl_combasic.py >> crawl_combasic.log  
    sleep 20s 
done
