"""실제 기여 그래프 SVG에 움직임 최소화 지원과 정적 대안을 추가한다."""
from pathlib import Path
import xml.etree.ElementTree as ET

ns = '{http://www.w3.org/2000/svg}'
for filename in ('github-snake.svg', 'github-snake-dark.svg'):
    path = Path('dist') / filename
    text = path.read_text()
    ET.fromstring(text)
    # SVG 이미지 내부에서도 시스템의 움직임 최소화 설정을 존중한다.
    reduced = '<style>@media(prefers-reduced-motion:reduce){*{animation:none!important}}</style>'
    text = text.replace('</svg>', reduced + '</svg>')
    path.write_text(text)
    static = text.replace('</svg>', '<style>*{animation:none!important}</style></svg>')
    (path.parent / filename.replace('.svg', '-static.svg')).write_text(static)
    for version in (text, static):
        root = ET.fromstring(version)
        assert root.tag == ns + 'svg'
        assert not root.findall('.//' + ns + 'script')
        assert len(version.encode()) < 1_000_000
