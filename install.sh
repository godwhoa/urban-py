#Install pip package manager
#Change based on distro/os
sudo apt-get install python-pip python-dev build-essential
#Install dep.
sudo pip install requests beautifulsoup4
#Move to bin for easy $ urban command
sudo mv urban.py /usr/bin/urban 
#Make it executable 
sudo chmod +x /usr/bin/urban
#Done!