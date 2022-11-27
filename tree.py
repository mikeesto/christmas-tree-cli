from random import randrange
from colored import fg, style
import json

try:
  f = open("./config.json")
except FileNotFoundError:
  print("Could not find a config.json file in current working directory")
  exit(1)

try:
  config = json.load(f)
except json.JSONDecodeError as e:
  print(f"config.json file is not formatted correctly - {e}")
  exit(1)

balls = [f"ball{i}" for i in range(1, 40)]
required_keys = ["message", "star", *balls]

if not all(key in config for key in required_keys):
  print('Missing the following keys in config.json file: ')
  print(list(set(required_keys).difference(config)))
  exit(1)


'''
The code below was adapted from F. L. S. Bustamante, terminal-christmas-tree, 2020 - Available at: https://github.com/chicolucio/terminal-christmas-tree
Licensed as MIT
'''

STAR = '★'
BALL = '●'
HEIGHT = 13
SCREEN_WIDTH = 80
ball_id = 1


def change_char(string):
  global ball_id
  string = list(string)
  for idx in range(0, len(string)):
    if string[idx] != ' ' and string[idx] == '_':
      # rand = randrange(256)
      color = config[f"ball{ball_id}"]
      string[idx] = f"{fg(color)}●{style.RESET}"
      ball_id += 1
  return ''.join(string)


def add_balls(tree):
  for idx, _ in enumerate(tree[: -2], 1):
    tree[idx] = change_char(tree[idx])
  return tree


def create_tree():
  body = ['/_\\', '/_\_\\']
  trunk = '[___]'
  begin = '/'
  end = '\\'
  pattern = '_/'

  j = 5
  for i in range(7, HEIGHT + 1, 2):
    middle = pattern + (i - j) * pattern
    line = ''.join([begin, middle[:-1], end])
    body.append(line)
    middle = middle.replace('/', '\\')
    line = ''.join([begin, middle[:-1], end])
    body.append(line)
    j += 1

  star_color = config["star"]
  star_colored = f"{fg(star_color)}{STAR}{style.RESET}"
  star_padded = star_colored.center(SCREEN_WIDTH + (len(star_colored) - 2))
  return [line.center(SCREEN_WIDTH) for line in (star_padded, *body, trunk)]


def main():
  tree = create_tree()
  tree_with_balls = add_balls(tree)
  print('\n'.join(tree_with_balls))
  print("\n")
  message = config["message"]
  print(message.center(SCREEN_WIDTH))


if __name__ == "__main__":
  main()
