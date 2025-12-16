sh +x clean.sh

echo $PWD
arg=0
if [ $# -ne 0 ]
  then
    echo "arguments supplied using supplied value"
	arg=$1
fi
python27 $PWD/main.py $arg
