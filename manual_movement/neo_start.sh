sudo busybox devmem 0x0c303018 w 0xc458
sudo busybox devmem 0x0c303010 w 0xc400

sudo modprobe can
sudo modprobe can_raw
sudo modprobe mttcan

sudo ip link set can0 up type can bitrate 500000 dbitrate 1000000 berr-reporting on fd on

cansend can0 123#abcdabcd
