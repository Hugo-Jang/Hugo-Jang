# HAGRO 프로필 에셋

- 팔레트: Midnight Navy `#112738`, 배너 `#0B1E30` → `#24465B`, Champagne Gold `#B89858`, Ivory `#F7F3EA`.
- `wave-banner.svg`, `hagro-wordmark.svg`: 사용자가 제공한 목업과 HAGRO 심볼을 바탕으로 새로 작성한 편집 가능한 SVG 근사 재현. 원본 로고 파일을 추출한 것은 아니며, 로고 원본이 확보되면 교체 가능.
- `developer.svg`: 이 프로필을 위해 직접 작성한 일반화된 로봇 개발자. 실제 인물의 외모를 표현하지 않음. 타이핑과 호흡만 작게 반복하며 외부 GIF를 복제하지 않음.
- `developer-static.svg`: 정적 대안. README의 `picture`와 SVG 내부 CSS에서 움직임 최소화 설정 지원.
- `higher-ground.svg`: 직접 작성한 정적 능선 그림.
- 외부 기술 아이콘: 기존 README의 [Skill Icons](https://github.com/tandpfun/skill-icons) 유지. 기술명은 본문 표에도 제공하여 이미지 실패 시에도 읽을 수 있음.
- Snake: [Platane/snk](https://github.com/Platane/snk), MIT 라이선스. 실행 버전을 커밋으로 고정. 실제 기여 캘린더에서 생성하고 `output` 브랜치에 게시. 녹색 기본 팔레트와 `#FACC15` 뱀을 사용.

## 유지보수

Snake는 매일 04:17 JST/KST 또는 README 변경 시 갱신한다. Actions의 **Generate contribution snake**에서 수동 실행할 수도 있다. 사용자 지정 토큰은 필요 없으며 해당 작업의 `GITHUB_TOKEN`만 사용한다. `contents: write`는 생성 이미지를 게시하기 위해 필요하다. 원격 브랜치를 강제로 덮어쓰지 않는다.

README는 GitHub가 지원하는 Markdown, HTML 표, `img`, `picture`만 사용한다. 배경색과 임의 CSS를 본문에 적용할 수 없으므로 본문은 GitHub의 테마를 따른다. 배너·로고·캐릭터의 배경은 에셋 내부에 포함한다. 스크립트, 외부 폰트, 외부 SVG 참조는 없다. 애니메이션은 SVG의 CSS로 구동하며 정적 파일 링크도 제공한다.
