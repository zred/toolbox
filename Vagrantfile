Vagrant.configure("2") do |config|
  config.vm.box = "archlinux/archlinux"
  config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"
  config.vm.provision "shell", inline: <<-SHELL
    pacman -Syu --noconfirm
    pacman -Sy python python-pip git --noconfirm
  SHELL
end
