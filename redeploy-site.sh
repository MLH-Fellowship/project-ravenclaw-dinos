tmux kill-server
cd /root/project-ravenclaw-dinos
git fetch && git reset origin/main --hard
source python3-virtualenv/bin/activate
pip3 install -r requirements.txt
TSESH="site-autodeploy"
WIN=0
tmux new -d -s $TSESH
tmux send-keys -t $TSESH:$WIN 'export FLASK_ENV=development' Enter
tmux send-keys -t $TSESH:$WIN 'flask run --host=0.0.0.0' Enter
exit 0
