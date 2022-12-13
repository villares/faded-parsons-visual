from pathlib import Path
from bs4 import BeautifulSoup

# This script should run from the same directory as the index.html file
index_html = 'index.html'
parsons_probs = Path.cwd() / 'parsons_probs'      # the puzzles dir
puzzle_files = [f for f in parsons_probs.iterdir()
                if f.suffix.lower() == '.yaml']

puzzle_list = []   # (file-name-without-yaml-extension, problem-title)
for yaml_file in sorted(puzzle_files):
    with open(yaml_file) as file:
        title = [li[14:].strip() for li in file.readlines() if li.startswith('problem_name: ')]
    title = title[0] if title else '-no title-'
    puzzle_list.append((yaml_file.stem, title))  # nome do arquivo sem extensão, nome dentro do yaml
    
with open(index_html) as index_file:
    html = index_file.read()

soup = BeautifulSoup(html, 'lxml')
div = soup.find('div', {'id': 'problem-list'})  # adicionei essa div pra facilitar
ul = div.find('ul')
ul.decompose()  # destroi/apaga a lista original

new_list = ''
for file_name, title in puzzle_list:
    new_list += f'<li><a href="problem.html?name={file_name}">{title}</a></li>\n'
div.append(BeautifulSoup('<ul>\n' + new_list + '\n</ul>', 'html.parser'))

with open(index_html, 'w') as index_file:
    index_file.write(str(soup))
