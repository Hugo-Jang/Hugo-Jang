"""실제 커밋과 무관한 장식용 샘플 잔디와 Snake SVG를 생성한다."""
from collections import deque
from pathlib import Path
import math
import random
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'assets'
OUT.mkdir(exist_ok=True)
rng = random.Random(20261108)
grid = {}
for x in range(53):
    for y in range(7):
        density = .65 + .13 * math.sin(x / 5)
        grid[x, y] = rng.choices([1, 2, 3, 4], [3, 4, 3, 2])[0] if rng.random() < density else 0

food = {p for p, level in grid.items() if level}
remaining = set(food)
body = [(-1 - i, 3) for i in range(7)]
route = [(-8 + i, 3) for i in range(8)]
eaten = {}

def search(start, goals, blocked):
    queue = deque([start])
    previous = {start: None}
    while queue:
        point = queue.popleft()
        if point in goals:
            path = []
            while previous[point] is not None:
                path.append(point)
                point = previous[point]
            return list(reversed(path))
        x, y = point
        for nxt in ((x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)):
            if -8 <= nxt[0] <= 53 and -1 <= nxt[1] <= 7 and nxt not in blocked and nxt not in previous:
                previous[nxt] = point
                queue.append(nxt)
    raise RuntimeError('Snake path cannot reach remaining sample cells')

while remaining:
    path = search(body[0], remaining, set(body[:-1]))
    for point in path:
        # 한 칸 이동할 때마다 재탐색하여 몸통과 충돌하지 않게 한다.
        body = [point] + body[:-1]
        route.append(point)
        if point in remaining:
            remaining.remove(point)
            eaten[point] = len(route) - 1
        break

# 바깥쪽을 거쳐 시작 위치로 돌아온 뒤 자연스럽게 반복한다.
for point in search(body[0], {(-8, 3)}, set(body[:-1])):
    route.append(point)
assert route[0] == route[-1]
assert set(eaten) == food
assert all(abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1 for a, b in zip(route, route[1:]))

STEP = .19
DURATION = (len(route) - 1) * STEP
path_d = 'M' + 'L'.join(f'{24+x*16},{42+y*16}' for x, y in route)

def generate(dark, animated):
    palette = ['#161B22', '#0E4429', '#006D32', '#26A641', '#39D353'] if dark else ['#EBEDF0', '#9BE9A8', '#40C463', '#30A14E', '#216E39']
    muted = '#8B949E' if dark else '#57606A'
    css = []
    rects = []
    for index, ((x, y), level) in enumerate(grid.items()):
        cls = f'c{index}'
        if animated and level:
            t = eaten[x, y] / (len(route) - 1) * 100
            css.append('@keyframes e'+str(index)+'{0%,'+f'{max(0,t-.04):.4f}'+'%{fill:'+palette[level]+'}'+f'{t:.4f}'+'%,99.5%{fill:'+palette[0]+'}100%{fill:'+palette[level]+'}}.'+cls+'{animation:e'+f'{index} {DURATION:g}s'+' linear infinite}')
        rects.append(f'<rect class="cell {cls}" x="{18+x*16}" y="{36+y*16}" width="12" height="12" rx="2" fill="{palette[level]}"/>')
    segments = []
    if animated:
        for i in range(6, -1, -1):
            size = (13.2, 12.0, 10.8, 9.8, 8.8, 7.8, 6.8)[i]
            shape = f'<rect x="{-size/2:g}" y="{-size/2:g}" width="{size:g}" height="{size:g}" rx="3.5" fill="#FACC15"/>'
            if i == 0:
                shape += '<circle cx="2.5" cy="-2.3" r="1.1" fill="#14263D"/><circle cx="2.5" cy="2.3" r="1.1" fill="#14263D"/>'
            segments.append(f'<g class="snake">{shape}<animateMotion dur="{DURATION:g}s" begin="{-DURATION+i*STEP:g}s" repeatCount="indefinite" rotate="auto" calcMode="linear"><mpath href="#route"/></animateMotion></g>')
    else:
        segments.append('<path d="M18 151H102" stroke="#FACC15" stroke-width="10" stroke-linecap="round"/>')
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="174" viewBox="0 0 880 174" role="img" aria-labelledby="title desc">
<title id="title">HAGRO Snake</title>
<desc id="desc">골드 뱀이 초록색 잔디를 따라 움직이며 지나간 칸을 비우는 애니메이션입니다.</desc>
<defs><path id="route" d="{path_d}"/></defs>
<style>{''.join(css)}</style>
{''.join(rects)}{''.join(segments)}
<text x="18" y="165" font-family="Arial,sans-serif" font-size="10" fill="{muted}">HAGRO / IDEAS · ENGINEERING · ACTION</text>
</svg>'''
    ET.fromstring(svg)
    assert len(svg.encode()) < 150_000
    return svg

for dark in (False, True):
    theme = 'dark' if dark else 'light'
    for animated in (True, False):
        suffix = '' if animated else '-static'
        filename = OUT / f'snake-{theme}{suffix}.svg'
        filename.write_text(generate(dark, animated))
        print(filename.name, filename.stat().st_size)
print(f'Sample cells: {len(food)}/371; route: {len(route)}; loop: {DURATION:g}s')
