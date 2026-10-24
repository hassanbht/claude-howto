import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# 이란의 청사진: Claude Code

이 문서는 Claude Code의 청사진으로서, 프로젝트 구조, 편집 모범 사례, 기여 방법 및 릴리스 분류 버전을 설명합니다.

## 프로젝트 구조

```
claude-howto/
├── .github/                     # GitHub 작업 흐름 및 템플릿
├── 01-slash-commands/           # 슬래시 명령어
├── 02-memory/                   # 메모리 시스템
├── 03-skills/                   # 에이전트 스킬
├── 04-subagents/                # 서브에이전트
├── 05-mcp/                      # MCP 통합
├── 06-hooks/                    # 훅
├── 07-plugins/                  # 플러그인
├── 08-checkpoints/              # 체크포인트 및 리와인드
├── 09-advanced-features/        # 고급 기능
├── 10-cli/                      # 명령줄 참조
├── docs/                        # 보조 문서
├── prompts/                     # 에이전트 프롬프트
├── resources/                   # 브랜드 자산
├── scripts/                     # 빌드 및 유틸리티 스크립트
├── CONTRIBUTING.md              # 기여 가이드
├── CODE_OF_CONDUCT.md           # 행동 강령
├── SECURITY.md                  # 보안 정책
├── STYLE_GUIDE.md               # 스타일 가이드
├── CLAUDE.md                    # 프로젝트 수준의 AI 지침
├── README.md                    # 메인 문서
└── ...
```

각 하위 디렉토리에는 해당 디렉토리의 문서, 스킬 또는 명령어가 포함된 자체 README.md가 있습니다.

## 저장소 설정

```bash
# 저장소 클론
git clone https://github.com/hassanbht/claude-howto.git
cd claude-howto

# 종속성 설치
pip install -r scripts/requirements.txt  # 선택 사항

# 개발용 가상 환경 설정 (선택 사항)
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

## 편집 모범 사례

- **일관성**: 이 저장소 전반에 걸친 스타일 가이드를 따르세요.
- **명확성**: 전문 용어에 의존하지 않고 코드가 없는 사람에게도 이해되도록 하세요.
- **구조**: 헤더와 코드 블록에 일관된 마크다운 형식을 사용하세요.
- **코드 블록**: 언어 태그를 포함하세요: `bash`, `json`, `md`, `yaml`, `mermaid`, `text`.
- **링크**: 절대 경로를 사용하세요. 내부 링크는 앵커나 상대 경로를 사용하세요.

### 코드 블록 예시

```bash
# 올바른 예
```bash
echo "Hello"
```

# 잘못된 예
```bash
echo "Hello"
```
```

### 헤더

```markdown
## 주요 섹션 제목

### 하위 섹션 제목
```

### 체크리스트

```markdown
- [ ] 항목 1
- [ ] 항목 2
```

## 기여 방법

### 이슈 제출

이슈를 제출하기 전에 [TESTING.md](.github/TESTING.md)를 읽으세요.

1. 기존 이슈를 검색하세요
2. 문제가 재현 가능한지 확인하세요
3. 의 취약점을 이용해 이슈를 생성하세요
4. 가능하면 재현 가능한 최소 저장소를 첨부하세요

### 풀 리퀘스트

1. 기능 브랜치를 작성하세요: `git checkout -b feature/my-feature`
2. 변경 사항을 커밋하세요: `git commit -m "feat: add my feature"`
3. 브랜치를 푸시하세요: `git push origin feature/my-feature`
4. 풀 리퀘스트를 생성하세요

### PR 템플릿

`.github/pull_request_template.md`를 준수하세요. 변경 사항을 위에 나열된 섹션으로 설명하세요.

### 코드 스타일

- 들여쓰기: 2개 공백
- 줄 바꿈 문자: LF
- 파일 끝: 줄 바꿈
- 명령어 `prettier --write .`로 스타일을 검사하세요

## 릴리스 분류 버전 관리

이 프로젝트는 아래 규칙에 따라 버전을 분류합니다:

```text
MAJOR.MINOR.PATCH
```

- **MAJOR**: 비호환성 변경 사항
- **MINOR**: 하위 호환 기능을 추가함 (새로운 섹션, 새로운 문서)
- **PATCH**: 버그 수정

### 버전 파일

- `RELEASE_NOTES.md` - 주요 릴리스 노트
- `CHANGELOG.md` - 전체 변경 로그
- `VERSION` - 현재 버전

현재 버전: `1.0.0`

### 릴리스 작업 흐름

1. 변경 사항 검토
2. `RELEASE_NOTES.md` 업데이트
3. `CHANGELOG.md` 업데이트
4. 태그 생성: `git tag -a v1.0.1 -m "Release v1.0.1"`
5. 푸시: `git push origin v1.0.1`
6. GitHub에서 릴리스 생성

## 업데이트 및 유지 관리

이 저장소는 정기적으로 업데이트됩니다:

- **매월**: 새로운 섹션 리뷰 및 추가
- **분기별**: 오래된 콘텐츠 검토
- **릴리스 시**: 리비전 및 CHANGELOG 업데이트

### 콘텐츠 업데이트 확인

```bash
git pull origin main
```

## 적용 및 지원

이 프로젝트에 대한 질문이나 문의 사항이 있으시면, `CONTRIBUTING.md` 또는 `CODE_OF_CONDUCT.md`를 참조하세요.

웹사이트: https://github.com/hassanbht/claude-howto
"""
with open(os.path.join(fa_dir, "CONTRIBUTING.md"), "w", encoding="utf-8") as f:
    f.write(content)

print("CONTRIBUTING.md written!")