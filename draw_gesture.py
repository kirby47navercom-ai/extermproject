from pico2d import *
import os
from QDollarRecognizer import QDollarRecognizer, Point
from canvas_size import *

BLACK = (0, 0, 0)  # 선과 글자 모두 검은색으로 통일

font = load_font('Font\\경기천년제목_Medium.ttf', 20)


def draw_point(x, y):
    draw_rectangle(x, y, x + 1, y + 1)


def draw_line(x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    steps = max(abs(dx), abs(dy))
    if steps == 0:
        draw_point(x1, y1)
        return
    x_inc, y_inc = dx / steps, dy / steps
    x, y = x1, y1
    for i in range(int(steps) + 1):
        draw_point(int(x), int(y))
        x += x_inc
        y += y_inc


def draw_text_on_screen(x, y, text):
    font.draw(x, y, text, BLACK)



class GestureRecognizer:
    def __init__(self):
        CACHE_PATH = 'gesture_cache.pkl'
        self.recognizer = QDollarRecognizer()
        if os.path.exists(CACHE_PATH):
            self.recognizer.load_gesture_cache(CACHE_PATH)
        else:
            self.recognizer.load_gesture_from_xml('10-stylus-MEDIUM')
            self.recognizer.load_gesture_from_xml('11-stylus-MEDIUM')
            self.recognizer.load_gesture_from_xml('NewGestures')
            self.recognizer.save_gesture_cache(CACHE_PATH)


        self.drawing = False
        self.points = []
        self.stroke_id = 0
        self.result = None


    def update(self, frame_time, events):
        for e in events:
            if e.type == SDL_KEYDOWN and e.key == SDLK_c:
                self.points = []
                self.result = None
                self.stroke_id = 0
            elif e.type == SDL_MOUSEBUTTONDOWN and e.button == SDL_BUTTON_LEFT:
                self.points, self.result, self.drawing = [], None, True
                self.stroke_id += 1
            elif e.type == SDL_MOUSEBUTTONUP and e.button == SDL_BUTTON_LEFT:
                self.drawing = False
                if len(self.points) > 10:
                    self.result = self.recognizer.recognize(self.points)
            elif e.type == SDL_MOUSEMOTION and self.drawing:
                self.points.append(Point(e.x, e.y, self.stroke_id))

    def draw(self):
        if len(self.points) > 1:
            for i in range(1, len(self.points)):
                if self.points[i].id == self.points[i - 1].id:
                    draw_line(self.points[i - 1].x, canvasheight - self.points[i - 1].y,
                              self.points[i].x, canvasheight - self.points[i].y)

        draw_text_on_screen(10, canvasheight - 30, "그림을 그리고 마우스를 떼세요.")
        if self.result:
            draw_text_on_screen(10, canvasheight - 60,
                                f"인식 결과: {self.result.name} (Score: {self.result.score:.2f})")