while ((1))
do
    python3 -u crawl_expander.py >> crawl_expander.log  & 
    sleep 60s 
    python3 -u crawl_expander.py >> crawl_expander.log   
    sleep 60s 
done
