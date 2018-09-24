Vagrant.configure("2") do |config|
  config.vm.box = "archlinux/archlinux"
  config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"
  config.vm.provision "shell", inline: <<-SHELL
    pacman -Syu --noconfirm
    pacman -Sy python python-pip git tmux --noconfirm
    git clone https://github.com/zred/toolbox
    python -m venv /home/vagrant/toolbox
    source /home/vagrant/toolbox/bin/activate
    pip install --upgrade pip
    pip install -r /home/vagrant/toolbox/requirements.txt
    tmux new-session -d
    tmux send-keys cd Space /home/vagrant/toolbox C-m source Space bin/activate C-m sudo Space python Space toolbox.py C-m
  SHELL
end
