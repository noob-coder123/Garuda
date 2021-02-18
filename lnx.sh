if [ whoami -ne 'root' ]
then
  echo "nonroot" > root.txt
else
  echo "rooted" > root.txt
fi
