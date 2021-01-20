# AutoMouse

일정시간 동안 마우스의 움직임을 입력 받은 뒤, 그대로 반복해서 움직여주는 프로그램

---

## Feature

- GUI를 통한 조작
- 시작 버튼을 누르면 2초 뒤부터 기록됨
- 기록된 마우스 움직임이 반복재생됨
- 실행 중 `Q` 버튼을 누르면 종료됨


---

## Change Log

[CHANGELOG.MD](https://github.com/syki66/auto-mouse/blob/master/CHANGELOG.MD)

---

## Build

```
pyinstaller --icon mouse.ico --onefile --noconsole auto_mouse.py
```