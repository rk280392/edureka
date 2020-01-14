#!/bin/bash

if [ ! grep puppet /etc/hosts | head -2  ]
then
	echo "*******************Inserting into hosts file***********************"
	cat <<EOT>> /etc/hosts
	192.168.0.109 puppet project.edu.com
	192.168.0.120 puppetslave
EOT
echo "**************************updated hosts file******************************"
else
	echo "************************hosts file up to date******************************************"
fi

if [ ! grep 'project.edu.com' /etc/puppet/puppet.conf | head -1 ]
then
	echo "inserting into config file"
	cat <<EOT>> /etc/puppet/puppet.conf
	[main]
	server = project.edu.com
EOT
	echo "****************************updated puppet.conf****************************************"
else
	echo "****************************puppet.conf up to date****************************************"
fi

find /var/lib/puppet/ssl -name vagrant.vm.pem -delete

echo "starting puppet agent"
sudo systemctl restart puppet.service

echo "enabling puppet agent"
sudo systemctl enable puppet
