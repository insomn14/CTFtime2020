while IFS= read -r line
do
	echo "Trying : $line";
	echo '3\n' | ./coffee_invocation  "$line"
done < file.txt
