# https://paste.ee/r/P4gE8

mkdir christmas_tree
cd christmas_tree
wget https://raw.githubusercontent.com/mikeesto/christmas-tree-cli/master/tree.py
wget https://raw.githubusercontent.com/mikeesto/christmas-tree-cli/master/config.json
sudo apt update -y && sudo apt install python3-pip -y
pip3 install colored
echo "~~~ Christmas tree ready ~~~"