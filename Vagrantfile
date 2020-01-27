# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  config.vm.box_check_update = false
  config.vm.network :forwarded_port, guest: 8000, host: 8006
  
  config.vm.provision :shell, path: "bootstrap.sh"
  
  config.trigger.after [:provision] do |t|
	  t.name = "Reboot after provisioning"
	  t.run = { :inline => "vagrant reload" }
  end
  
  config.vm.provider "virtualbox" do |v|
    v.name = "eat-delivery-backend-monolith"
	  v.memory = 1024 * 2
	  v.cpus = 2
	  v.customize [ "modifyvm", :id, "--uartmode1", "disconnected" ]
  end
end
