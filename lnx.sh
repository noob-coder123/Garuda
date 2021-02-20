if [ "$EUID" -ne 0 ]
then
  echo "nonroot" > root.txt
else
  echo "rooted" > root.txt
fi
