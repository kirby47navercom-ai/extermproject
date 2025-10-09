from pico2d import *
import canvas_size

stage1width = 1980
stage1height = 1080

blocks = []

start=False

class Background:
    def __init__(self, stage):
        global blocks
        self.stage = stage
        blocks.clear()
        if stage == '1':
            self.background = [load_image('1stage\\1.png'), load_image('1stage\\2.png'),
                                   load_image('1stage\\3.png'),
                                   load_image('1stage\\4.png'), load_image('1stage\\5.png'),
                                   load_image('1stage\\6.png'),
                                   load_image('1stage\\7.png'), load_image('1stage\\8.png'), ]
            self.x = [0,0,0,0]
            self.speed=300
        elif stage == '2':
            self.background = [load_image('2stage\\1.png'), load_image('2stage\\2.png'),
                                   load_image('2stage\\3.png')]
            self.background_size=[(872, 479), (726, 574), (1280*1.5, 2048*1.5)]
            self.floor1 = load_image('2stage\\floor_1.png')
            self.floor2 = load_image('2stage\\floor_2.png')

            self.floor_pos = [(80, 24), (200, 24), (80, 170), (80, 340), (80, 510)]
            self.floor_width=[274,int(48*1.5)]
            self.floor_height=[63,int(32*1.2)]

            for i in range(3):
                blocks.append((self.floor_pos[i+2][0], self.floor_pos[i+2][1], self.floor_width[1], self.floor_height[1]))

            self.background_num=0
            self.background_change_time=0
            self.background_change_timer=4.0
            self.speed=100
            self.background_magnification = [1.6, 1.8, 1.0]

            self.scroll_y = 0
        pass

    def update(self, frame_time,events=None):
        global start
        if self.stage == '1':
            for i in range(self.x.__len__()):
                self.x[i] += self.speed * frame_time * (i+1) * 0.2
                if self.x[i] >= stage1width * 0.7:
                    self.x[i] = 0
        elif self.stage == '2':
            if self.background_change_time < self.background_change_timer:
                self.background_change_time += frame_time
            if start:
                self.scroll_y += self.speed * frame_time*20

                image_height = self.background_size[2][1] * self.background_magnification[2]

                if self.scroll_y >= image_height:
                    self.scroll_y = 0

            pass
        pass

    def draw(self):
        if self.stage == '1':
            for i in range(self.background.__len__()):
                if i==2 or i==3 or i==4:
                    self.background[i].clip_draw(0, 0, stage1width, stage1height, canvas_size.canvaswidth // 2 + self.x[i-2]-(stage1width * 0.7)-canvas_size.camera_x,canvas_size.canvasheight // 2-canvas_size.camera_y, stage1width * 0.7, stage1height * 0.7)
                    self.background[i].clip_draw(0, 0, stage1width, stage1height, canvas_size.canvaswidth//2+self.x[i-2]-canvas_size.camera_x,canvas_size.canvasheight//2 -canvas_size.camera_y, stage1width*0.7, stage1height*0.7)
                else:
                    self.background[i].clip_draw(0, 0, stage1width, stage1height, canvas_size.canvaswidth//2-canvas_size.camera_x,canvas_size.canvasheight//2-canvas_size.camera_y, stage1width*0.7, stage1height*0.7)
        elif self.stage == '2':
            self.stage2_start()

            for i in range(2):
                self.floor1.clip_composite_draw(0, 0, self.floor_width[0], self.floor_height[0],0,'h',self.floor_pos[i][0],self.floor_pos[i][1],self.floor_width[0], self.floor_height[0])

            for i in range(3):
                self.floor2.clip_composite_draw(0, 0, self.floor_width[1], self.floor_height[1],0,'',self.floor_pos[i+2][0],self.floor_pos[i+2][1],self.floor_width[1], self.floor_height[1])
    def stage2_start(self):
        global start
        if not start:
            image_A = self.background[0]  # 사라질 이미지 (1.png)
            image_B = self.background[1]  # 나타날 이미지 (2.png)

            # 2. 페이드 진행률 계산 (0.0 ~ 1.0)
            progress = self.background_change_time / self.background_change_timer
            progress = min(1.0, progress)  # 값이 1.0을 넘지 않도록 고정

            # 3. 그리기
            if progress < 1.0:  # 페이드가 진행 중일 때
                # 3-1. image_A를 점점 투명하게 그림
                image_A.clip_draw(0, 0, self.background_size[0][0], self.background_size[0][1],
                                  canvas_size.canvaswidth // 2 - canvas_size.camera_x,
                                  canvas_size.canvasheight // 2 - canvas_size.camera_y,
                                  self.background_size[0][0] * self.background_magnification[0],
                                  self.background_size[0][1] * self.background_magnification[0])

                # 3-2. image_B를 점점 선명하게 겹쳐서 그림
                opacity_B = progress
                image_B.opacify(opacity_B)
                image_B.clip_draw(0, 0, self.background_size[1][0], self.background_size[1][1],
                                  canvas_size.canvaswidth // 2 - canvas_size.camera_x,
                                  canvas_size.canvasheight // 2 - canvas_size.camera_y,
                                  self.background_size[1][0] * self.background_magnification[1],
                                  self.background_size[1][1] * self.background_magnification[1])

            else:  # 페이드가 끝났을 때 (progress >= 1.0)
                # image_B만 완전히 선명하게 그림
                image_B.opacify(1.0)
                image_B.clip_draw(0, 0, self.background_size[1][0], self.background_size[1][1],
                                  canvas_size.canvaswidth // 2 - canvas_size.camera_x,
                                  canvas_size.canvasheight // 2 - canvas_size.camera_y,
                                  self.background_size[1][0] * self.background_magnification[1],
                                  self.background_size[1][1] * self.background_magnification[1])
        else:
            image = self.background[2]
            width = self.background_size[2][0] * self.background_magnification[2]
            height = self.background_size[2][1] * self.background_magnification[2]

            # 2. 첫 번째 이미지 그리기
            image.draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2 + self.scroll_y, width, height)

            # 3. 두 번째 이미지를 첫 번째 이미지 바로 위에 이어 붙여 그리기
            image.draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2 + self.scroll_y - height,width, height)

            pass
