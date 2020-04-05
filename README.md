# toolbox

### Linux Install Notes
```
git clone https://github.com/zred/toolbox.git
cd toolbox
python -m venv .
source bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python toolbox.py
```

### PowerShell Install Notes
```
git clone https://github.com/zred/toolbox.git
cd toolbox
python -m venv .
.\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r .\requirements.txt
.\toolbox.py
```

### Vagrant Notes
```
wget https://raw.githubusercontent.com/zred/toolbox/master/Vagrantfile
vagrant up
```
