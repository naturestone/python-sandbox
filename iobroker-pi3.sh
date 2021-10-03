# Quelle: https://technikkram.net/blog/2020/11/16/io-broker-auf-dem-raspberry-pi-installieren/

sudo apt-get update und sudo apt-get dist-upgrade		

# Vor der Installation sollte der Raspberry Pi auf den neusten Stand gebracht werden

curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash –		

# Für die Nutzung von ioBroker wird wie bei vielen anderen Anwendung auch nodejs benötigt da die installation als nom Paket zur Verfügung gestellt wird

sudo apt install -y nodejs		

# Mit dem folgenden Befehlt wird alles nötige installiert

curl -sL https://iobroker.net/install.sh | bash –		

# Nach dem herunterladen wir ioBroker installiert und direkt geöffnet

echo 'http://192.168.178.174:8081' 

# Aufruf im Heimnetz über Port 8021 - IP Adresse ist anzupassen.
