from pico2d import *
import os
from dtd import QDollarRecognizer, Point

SCREEN_WIDTH, SCREEN_HEIGHT = 1536, 864
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

open_canvas(SCREEN_WIDTH, SCREEN_HEIGHT)

# 한글 지원 폰트 로드
font = load_font('Font\\경기천년제목_Medium.ttf', 20)

CACHE_PATH = 'gesture_cache.pkl'
recognizer = QDollarRecognizer()
if os.path.exists(CACHE_PATH):
    recognizer.load_gesture_cache(CACHE_PATH)
else:
    recognizer.load_gesture_from_xml('10-stylus-MEDIUM')
    recognizer.load_gesture_from_xml('11-stylus-MEDIUM')
    recognizer.load_gesture_from_xml('NewGestures')
    recognizer.save_gesture_cache(CACHE_PATH)

running = True
drawing = False
points = []
stroke_id = 0
result = None

# --------------------------
# 점 그리기
# --------------------------
def draw_point(x, y):
    draw_rectangle(x, y, x + 1, y + 1)

# --------------------------
# 선 그리기
# --------------------------
def draw_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    if steps == 0:
        draw_point(x1, y1)
        return
    x_inc = dx / steps
    y_inc = dy / steps
    x, y = x1, y1
    for i in range(int(steps) + 1):
        draw_point(int(x), int(y))
        x += x_inc
        y += y_inc

# --------------------------
# 텍스트 출력
# --------------------------
def draw_text_on_screen(x, y, text):
    font.draw(x, y, text, BLACK)

# --------------------------
# 메인 루프
# --------------------------
while running:
    clear_canvas()

    # 선 그리기
    if len(points) > 1:
        for i in range(1, len(points)):
            if points[i].id == points[i - 1].id:
                draw_line(points[i - 1].x, SCREEN_HEIGHT - points[i - 1].y,
                          points[i].x, SCREEN_HEIGHT - points[i].y)

    # 안내 문구
    draw_text_on_screen(10, SCREEN_HEIGHT - 30, "그림을 그리고 마우스를 떼세요. (C: 초기화)")

    if result:
        draw_text_on_screen(10, SCREEN_HEIGHT - 60,
                            f"인식 결과: {result.name} (Score: {result.score:.2f})")

    update_canvas()

    # 이벤트 처리
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_c:
                points = []
                result = None
                stroke_id = 0
        elif e.type == SDL_MOUSEBUTTONDOWN:
            if e.button == SDL_BUTTON_LEFT:
                points = []
                result = None
                stroke_id = 0
                drawing = True
                stroke_id += 1
        elif e.type == SDL_MOUSEBUTTONUP:
            if e.button == SDL_BUTTON_LEFT:
                drawing = False
                # 마우스를 떼면 인식만
                if len(points) > 10:
                    result = recognizer.recognize(points)
        elif e.type == SDL_MOUSEMOTION:
            if drawing:
                x, y = e.x, e.y
                points.append(Point(x, y, stroke_id))

close_canvas()
