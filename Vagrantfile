Vagrant.configure("2") do |config|
  config.vm.box = "archlinux/archlinux"
  config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"
  config.vm.provision "shell", inline: <<-SHELL
    sudo pacman -Syu --noconfirm
    sudo pacman -Sy python python-pip git tmux gcc --noconfirm
    git clone https://github.com/zred/toolbox
    python -m venv /home/vagrant/toolbox
    source /home/vagrant/toolbox/bin/activate
    sudo pip install --upgrade pip
    sudo pip install -r /home/vagrant/toolbox/requirements.txt
    tmux new-session -d
    tmux send-keys cd Space /home/vagrant/toolbox C-m source Space bin/activate C-m sudo Space python Space toolbox.py C-m
  SHELL
end
