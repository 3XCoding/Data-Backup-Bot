if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/HeyAdithya/Data-Backup-Bot /Data-Backup-Bot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Data-Backup-Bot
fi
cd /Data-Backup-Bot
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
