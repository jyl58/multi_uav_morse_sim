current_pat=$(pwd)

export PYTHONPATH=$PYTHONPATH:$current_pat/lib/

echo "run the morse env"
screen -d -m morse run ./env/multi_copter_env.py 

if [[ $? -ne 0 ]]; then
	echo "morse run ERR!"	
	exit 1
fi

pid=$(ps -ef | grep "arducopter" | grep -v grep | awk '{print $2}')
if [ -n "$pid" ]; then
	echo "arducopter is already running , auto kill it "
	kill "$pid"
fi

echo "run the copter sim firmware at background "
./firmware/bin/ubuntu/arducopter -S -I0 --home -35.363261,149.165230,584,353 --model morse-quad --speedup 1 --defaults ./firmware/uav-param/mav.parm 1>/dev/null & 

if [[ $? -ne 0 ]]; then
	echo "arducopter run ERR!"	
	exit 1
fi

echo "run the mavproxy"
mavproxy.py --master tcp:127.0.0.1:5760  --sitl 127.0.0.1:5501 --aircraft MyCopter --out 127.0.0.1:14550 --out 127.0.0.1:14551 