cd /root/project-ravenclaw-dinos
git fetch && git reset origin/main --hard
source python3-virtualenv/bin/activate
pip3 install -r requirements.txt
RUN="flask run --host=0.0.0.0"
systemctl daemon-reload
systemctl restart myportfolio
