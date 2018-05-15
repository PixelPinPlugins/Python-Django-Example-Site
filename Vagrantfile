Vagrant.configure("2") do |config|
    config.vm.box = "ubuntu/trusty64"
    config.vm.network :private_network, ip: '192.168.33.14'

    config.vm.provider :virtualbox do |vb|
        vb.customize ["setextradata", :id, "VBoxInternal2/SharedFoldersEnableSymlinksCreate/v-root", "1"]
        vb.customize ["modifyvm", :id, "--memory", "512"]
    end
	
	config.vm.provision "shell", inline: <<-SHELL
	
	#echo "CREATE DATABASE gfirst;" | MYSQL_PWD=root mysql --user=root
	#zcat /vagrant/db/init/initial-database.sql.gz | MYSQL_PWD=root mysql --user=root gfirst
	
	curl https://www.openssl.org/source/openssl-1.1.0h.tar.gz | tar xz && cd openssl-1.1.0h && sudo ./config && sudo make && sudo make install
	
	sudo ln -sf /usr/local/ssl /usr/bin/openssl
	
	cd /usr/local/lib
	
	sudo cp -R libssl.so.1.1 /usr/lib && sudo cp -R libcrypto.so.1.1 /usr/lib && sudo cp -R libcrypto.a /usr/lib

	cd
	apt-get update
	apt-get install zlib1g-dev 
	apt-get install libpq-dev 
	apt-get install libsqlite3-dev
	apt-get install python-dev
	
	apt-get install python3-dev libffi-dev libssl-dev
	wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz  
	tar xvf Python-3.6.5.tgz
	cd Python-3.6.5
	./configure --enable-optimizations --enable-loadable-sqlite-extensions && make OFLAGS=-O1 && make altinstall
	
	cd 
	
	python3.6 -m venv testenv
	source testenv/bin/activate
	
	SHELL
  
  config.vm.provision "shell", run: "always", inline: "mount /vagrant/node_modules"
end
