"""
Update the index.html file adding problems
found in the 'parsons_probs' folder.
"""

from collections import defaultdict
from pathlib import Path

from bs4 import BeautifulSoup  # pip install beautifulsoup4
 
puzzles_cat = defaultdict(list)  # puzzle category: [puzzle0, ...]
# This script should run from the same directory as the index.html file
index_html = 'index.html'
parsons_probs = Path.cwd() / 'parsons_probs'      # the puzzles dir
# Get a list of the parsons_probs subdir contents
subdir_contents = list(parsons_probs.iterdir())
# Get only the yaml files
puzzle_files = [f for f in subdir_contents if f.suffix.lower() == '.yaml']

def get_img_file(li):
    start = li.find('img src="parsons_probs/') + 23
    end = li.find('"', start)
    return li[start:end]

for yaml_file in sorted(puzzle_files):
    with open(yaml_file) as file:
        lines = list(file.readlines())
        # nome/título vem do yaml
        tl = [line[14:].strip() for line in lines if line.startswith('problem_name: ')]
        title = tl[0] if tl else 'Unnamed Problem'
        # subtítulo/descrição curto vem do yaml
        stl = [line[18:].strip() for line in lines if line.startswith('problem_subtitle: ')]
        sub_title = stl[0] if stl else ''
        cl = [line[18:].strip() for line in lines if line.startswith('problem_category: ')]
        category = cl[0].lower() if cl else 'geral'
        il = [get_img_file(line) for line in lines if 'img src=' in line]
        img_file = il[0] if il else ''
    puzzles_cat[category].append((yaml_file.stem, title, sub_title, img_file))
    print(category, yaml_file.stem, img_file, title, sub_title, sep=' | ')
 
with open(index_html) as index_file:
    html = index_file.read()

soup = BeautifulSoup(html, 'lxml')
div = soup.find('div', {'id': 'problem-list'})  # adicionei essa div pra facilitar
div.clear()
for cat, puzzle_list in sorted(puzzles_cat.items()):
    div.append(BeautifulSoup(f'<h5>{cat}</h5>', 'html.parser'))   
    new_list = ''
    for file_name, title, sub_title, img_file in puzzle_list:
        new_list += (f'<li><a href="problem.html?name={file_name}" class="thumbnail">' 
                     f'<img src="parsons_probs/{img_file}" alt="{title}" class="thumbnail">'
                     f'{title}</a></br> {sub_title}</li>\n')
    div.append(BeautifulSoup('<ul>\n' + new_list + '\n</ul>', 'html.parser'))
     
with open(index_html, 'w') as index_file:
    index_file.write(str(soup))
