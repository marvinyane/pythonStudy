rm *.c
rm *.h
./generate_lib_files.py $1 $2
./generate_serialize.py $1 $2
./generate_unserialize.py $1 $2
rm *.pyc
