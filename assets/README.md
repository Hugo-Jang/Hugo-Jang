# HAGRO 프로필 에셋

- 팔레트: Midnight Navy `#112738`, 배너 `#0B1E30` → `#24465B`, Champagne Gold `#B89858`, Ivory `#F7F3EA`.
- `wave-banner.svg`, `hagro-wordmark.svg`: 사용자가 제공한 목업과 HAGRO 심볼을 바탕으로 새로 작성한 편집 가능한 SVG 근사 재현. 원본 로고 파일을 추출한 것은 아니며, 로고 원본이 확보되면 교체 가능.
- `developer.svg`: 이 프로필을 위해 직접 작성한 일반화된 로봇 개발자. 실제 인물의 외모를 표현하지 않음. 타이핑과 호흡만 작게 반복하며 외부 GIF를 복제하지 않음.
- `developer-static.svg`: 정적 대안. README의 `picture`와 SVG 내부 CSS에서 움직임 최소화 설정 지원.
- `higher-ground.svg`: 직접 작성한 정적 능선 그림.
- 외부 기술 아이콘: 기존 README의 [Skill Icons](https://github.com/tandpfun/skill-icons) 유지. 기술명은 본문 표에도 제공하여 이미지 실패 시에도 읽을 수 있음.
- Snake: [Platane/snk](https://github.com/Platane/snk), MIT 라이선스. 실행 버전을 커밋으로 고정. 실제 기여 캘린더에서 생성하고 `output` 브랜치에 게시. 녹색 기본 팔레트와 `#FACC15` 뱀을 사용.
- 기여 캘린더가 비어 있을 때에는 기록을 채우지 않고 뱀이 빈 그리드 둘레를 천천히 순회한다. 기여가 조회되면 snk의 기본 경로를 그대로 사용한다.

## 유지보수

Snake는 매일 04:17 JST/KST 또는 README 변경 시 갱신한다. Actions의 **Generate contribution snake**에서 수동 실행할 수도 있다. 사용자 지정 토큰은 필요 없으며 해당 작업의 `GITHUB_TOKEN`만 사용한다. `contents: write`는 생성 이미지를 게시하기 위해 필요하다. 원격 브랜치를 강제로 덮어쓰지 않는다.

README는 GitHub가 지원하는 Markdown, HTML 표, `img`, `picture`만 사용한다. 배경색과 임의 CSS를 본문에 적용할 수 없으므로 본문은 GitHub의 테마를 따른다. 배너·로고·캐릭터의 배경은 에셋 내부에 포함한다. 스크립트, 외부 폰트, 외부 SVG 참조는 없다. 애니메이션은 SVG의 CSS로 구동하며 정적 파일 링크도 제공한다.

## 애니메이션 수정

`wave-banner-animated.svg`는 공식 [capsule-render](https://github.com/kyechan99/capsule-render)의 `type=waving` API 출력에 기반한다. 배너 그라데이션은 `#0B1E30` → `#24465B`, 글자는 `#F7F3EA`이며 HAGRO 심볼·골드 선을 덧붙이고 파형의 불투명도를 조절했다. 두 물결의 20초 SMIL 반복을 유지한다. 원본 출력의 텍스트에 포함된 `&`는 유효한 XML이 되도록 이스케이프했다. 라이선스는 `capsule-render-LICENSE.txt`에 보관한다. 이전 `wave-banner.svg`는 최초의 정적 시안으로 보관한다.

사용자가 움직임을 명시적으로 요청했으므로 배너와 Snake는 기본으로 재생한다. README에서 시스템의 움직임 줄이기 설정으로 이 두 이미지를 정적 이미지로 바꾸지 않는다. 각각 별도 정적 보기 링크를 제공한다. 아바타의 기존 움직임 최소화 지원은 유지한다. Snake의 `-animated.svg` 파일명은 이전 정적 이미지 캐시와 구분하기 위해 사용한다.

## 기준 이미지에 맞춘 반투명 배너

현재 README는 `wave-banner-reference-animated.svg`를 사용한다. 사용자가 최종 지정한 배너의 짙은 네이비·청록빛 물결과 골드 곡선, H 심볼·타이포 배치를 새 SVG로 재구성했다. 이미지 생성 모델로 다시 그린 결과물이 아니라 편집 가능한 벡터 근사 재현이다. 상단 배경은 불투명, 청록 물결은 불투명도 0.78, 물결 밖은 알파 0으로 처리한다. 골드 띠는 중앙에서 약해지며 좌우에서 선명하게 보인다. GitHub의 라이트·다크 배경을 바꾸지 않고 실제 이미지 투명도로 합성한다.

세 곡선은 같은 18초 SMIL 주기로 부드럽게 변형되어 이음새가 벌어지지 않는다. 이름·설명·로고는 고정된다. 정적 대안은 `wave-banner-reference-static.svg`이며 동일한 첫 프레임과 투명도를 사용한다. 외부 폰트·스크립트·SVG 리소스 요청은 없다. 이전 capsule-render 배너 파일과 라이선스는 보관한다.

## 물결 움직임 가시성 보완

현재 배너는 `wave-banner-reference-motion-v2.svg`를 사용한다. 승인된 첫 프레임과 정적 보기, 색상·로고·글자·알파는 유지한다. 반복 주기를 18초에서 8초로 줄이고 후속 프레임의 곡선 변화량을 1.8배로 늘려 README 크기에서도 움직임을 알아볼 수 있게 했다. 새 파일명을 사용하여 이전 SVG 캐시와 구분한다. 채팅에 보여주는 PNG 비교 화면은 정적이므로 별도 GIF 미리보기로 실제 재생을 보여준다.
