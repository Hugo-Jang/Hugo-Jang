"""실제 기여 그래프 SVG에 움직임 최소화 지원과 정적 대안을 추가한다."""
from pathlib import Path
import xml.etree.ElementTree as ET

ns = '{http://www.w3.org/2000/svg}'
for filename in ('github-snake.svg', 'github-snake-dark.svg'):
    path = Path('dist') / filename
    text = path.read_text()
    ET.fromstring(text)
    # snk는 빈 기여 캘린더에서 1프레임만 생성한다. 기록을 추가하지 않고
    # 빈 그리드 둘레만 순회하게 하여 애니메이션의 동작을 유지한다.
    if '@keyframes s0{0%{transform:translate(0px,-16px)}}' in text:
        width = float(ET.fromstring(text).get('width')) - 48
        empty_motion = (
            '<style>@keyframes empty-calendar{'
            '0%,100%{transform:translate(0px,-16px)}'
            f'35%{{transform:translate({width:g}px,-16px)}}'
            f'50%{{transform:translate({width:g}px,112px)}}'
            '85%{transform:translate(0px,112px)}}'
            + ''.join(f'.s.s{i}{{animation:empty-calendar 32s linear -{i * .3:g}s infinite}}' for i in range(4))
            + '</style>'
        )
        text = text.replace('</svg>', empty_motion + '</svg>')
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
