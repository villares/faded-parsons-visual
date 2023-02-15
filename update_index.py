from pathlib import Path
from bs4 import BeautifulSoup
from collections import defaultdict
 
puzzles_cat = defaultdict(list)  # puzzle category: [puzzle0, ...]
# This script should run from the same directory as the index.html file
index_html = 'index.html'
parsons_probs = Path.cwd() / 'parsons_probs'      # the puzzles dir
# Get a list of the parsons_probs subdir contents
subdir_contents = list(parsons_probs.iterdir())
# Get only the yaml files
puzzle_files = [f for f in subdir_contents if f.suffix.lower() == '.yaml']

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
    puzzles_cat[category].append((yaml_file.stem, title, sub_title))
    print(category, yaml_file.stem, title, sub_title)
 
with open(index_html) as index_file:
    html = index_file.read()

soup = BeautifulSoup(html, 'lxml')
div = soup.find('div', {'id': 'problem-list'})  # adicionei essa div pra facilitar
div.clear()
for cat, puzzle_list in sorted(puzzles_cat.items()):
    div.append(BeautifulSoup(f'<h5>{cat}</h5>', 'html.parser'))   
    new_list = ''
    for file_name, title, sub_title in puzzle_list:
        new_list += f'<li><a href="problem.html?name={file_name}">{title}</a> {sub_title}</li>\n'
    div.append(BeautifulSoup('<ul>\n' + new_list + '\n</ul>', 'html.parser'))
     
with open(index_html, 'w') as index_file:
    index_file.write(str(soup))
