for i in {1..10}; do
    tr -dc "01" < /dev/urandom | head -c 2000000 > "oinbnvcfe$i.css"
done
