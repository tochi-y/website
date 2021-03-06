import os
from os import path
import shutil
import sys

"""
This script cannot add header to following files:
- en/installation_guide/*.md
- en/plugin-developer/Personium_AuthenticationPluginDeveloperManual.md
- en/server-operator/setup_percell.md
- en/server-operator/setup_virtual_image.md
- en/server-operator/setup.md
- en/unit-administrator/tutorial.md
- ja/app-developer/Personium_Apps.md
- ja/installation_guide/*.md
- ja/server-operator/setup_percell.md
- ja/server-operator/setup_virtual_image.md
- ja/server-operator/setup.md
- ja/unit-administrator/tutorial.md
"""

def add_header(dirpath, filename):
  fullpath = path.join(dirpath, filename)
  print(fullpath)

  with open(fullpath, encoding='utf-8') as f:
    line = f.readline()
    if not line.startswith('# '):
      print('Not start # ')
      return
    title = line[2:-1]
    print(title)
    temp = 'temp.md'
    with open(temp, encoding='utf-8', mode='w') as writer:
      header = [
        '---',
        'id: %s' % filename[:-3],
        'title: %s' % title,
        'sidebar_label: %s' % title,
        '---',
        ''
      ]
      writer.write('\n'.join(header))
      writer.write(f.read())
  shutil.move(temp, fullpath)

def main():
  args = sys.argv
  if len(args) < 2:
    print('Usage: python add_header.py <targetDirPath>')
    sys.exit(1)
  elif not path.exists(args[1]):
    print('Directory [%s] does not exist.' % args[1])
    sys.exit(2)

  targetDirPath = args[1]
  for curDir, dirs, files in os.walk(targetDirPath):
    for filename in files:
      if filename.endswith('.md'):
        add_header(curDir, filename)

if __name__ == "__main__":
    main()