current_pat=$(pwd)

export PYTHONPATH =$PYTHONPATH:$current_pat"/lib/"

echo "run the morse env"
morse run ./env/multi_copter_env.py &

if [[ $? -ne 0 ]]; then
	echo "morse run ERR!"	
	exit 1
fi

echo "run the copter sim firmware"
./firmware/bin/ubuntu/arducopter -S -I0 --home -35.363261,149.165230,584,353 --model morse-quad --speedup 1 --defaults ../../uav-param/mav.parm  & 

if [[ $? -ne 0 ]]; then
	echo "arducopter run ERR!"	
	exit 1
fi

echo "run the mavproxy"
mavproxy.py --master tcp:127.0.0.1:5760 --sitl 127.0.0.1:5501 --out 127.0.0.1:14550 --out 127.0.0.1:14551 