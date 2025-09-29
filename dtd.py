from pico2d import *
import math
import time
import xml.etree.ElementTree as ET
import os
import pickle
import re
#
# Point class




def ramona_idle_ani():
    ramona = load_image('Ramona\\Ramona_idle.png')
    ramona_idle_coordinate = [
        (0, 0, 30, 64, 0, 0),
        (33, 0, 30, 64, 0, 0),
        (66, 0, 29, 64, 0, 0),
        (99, 0, 30, 64, 0, 0),
        (131, 0, 31, 64, 0, 0),
        (165, 0, 31, 64, 0, 0),
    ]
    x, y = 400, 300
    for i in range(2):
        for j in ramona_idle_coordinate:
            clear_canvas()
            left, bottom, width, height,jx,jy = j
            ramona.clip_composite_draw(left, bottom, width, height, 0, '', x, y, width*2, height*2)
            update_canvas()
            delay(0.1)
class Point:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id  # stroke ID to which this point belongs (1, 2, 3, etc.)
        self.int_x = 0  # for indexing into the LUT
        self.int_y = 0  # for indexing into the LUT


#
# PointCloud class
#
class PointCloud:
    def __init__(self, name, points):
        self.name = name
        self.points = resample(points, NUM_POINTS)
        self.points = scale(self.points)
        self.points = translate_to(self.points, ORIGIN)
        self.points = make_int_coords(self.points)  # fills in (int_x, int_y) values
        self.lut = compute_lut(self.points)


#
# Result class
#
class Result:
    def __init__(self, name, score, ms):
        self.name = name
        self.score = score
        self.time = ms


#
# QDollarRecognizer constants
#
NUM_POINT_CLOUDS = 16
NUM_POINTS = 32
ORIGIN = Point(0, 0, 0)
MAX_INT_COORD = 1024  # (int_x, int_y) range from [0, MAX_INT_COORD - 1]
LUT_SIZE = 64  # default size of the lookup table is 64 x 64
LUT_SCALE_FACTOR = MAX_INT_COORD / LUT_SIZE  # used to scale from (int_x, int_y) to LUT


#
# Private helper functions from here on down
#
def cloud_match(candidate, template, min_so_far):
    n = len(candidate.points)
    step = math.floor(n ** 0.5)

    lb1 = compute_lower_bound(candidate.points, template.points, step, template.lut)
    lb2 = compute_lower_bound(template.points, candidate.points, step, candidate.lut)

    for i, (val1, val2) in enumerate(zip(lb1, lb2)):
        j = i * step
        if val1 < min_so_far:
            min_so_far = min(min_so_far, cloud_distance(candidate.points, template.points, j, min_so_far))
        if val2 < min_so_far:
            min_so_far = min(min_so_far, cloud_distance(template.points, candidate.points, j, min_so_far))

    return min_so_far


def cloud_distance(pts1, pts2, start, min_so_far):
    n = len(pts1)
    unmatched = list(range(n))  # indices for pts2 that are not matched

    i = start  # start matching with point 'start' from pts1
    weight = n  # weights decrease from n to 1
    sum_dist = 0.0  # sum distance between the two clouds

    while True:
        u = -1
        b = float('inf')
        for j_idx, j in enumerate(unmatched):
            d = sqr_euclidean_distance(pts1[i], pts2[j])
            if d < b:
                b = d
                u = j_idx

        unmatched.pop(u)
        sum_dist += weight * b

        if sum_dist >= min_so_far:
            return sum_dist  # early abandoning

        weight -= 1
        i = (i + 1) % n
        if i == start:
            break

    return sum_dist


def compute_lower_bound(pts1, pts2, step, lut):
    n = len(pts1)
    lb = [0.0] * (math.floor(n / step) + 1)
    sat = [0.0] * n

    for i in range(n):
        x = round(pts1[i].int_x / LUT_SCALE_FACTOR)
        y = round(pts1[i].int_y / LUT_SCALE_FACTOR)
        index = lut[x][y]
        d = sqr_euclidean_distance(pts1[i], pts2[index])
        sat[i] = d if i == 0 else sat[i - 1] + d
        lb[0] += (n - i) * d

    for i in range(step, n, step):
        j = i // step
        lb[j] = lb[0] + i * sat[n - 1] - n * sat[i - 1]

    return lb


def resample(points, n):
    I = path_length(points) / (n - 1)
    D = 0.0
    new_points = [points[0]]

    i = 1
    while i < len(points):
        if points[i].id == points[i - 1].id:
            d = euclidean_distance(points[i - 1], points[i])
            if (D + d) >= I:
                qx = points[i - 1].x + ((I - D) / d) * (points[i].x - points[i - 1].x)
                qy = points[i - 1].y + ((I - D) / d) * (points[i].y - points[i - 1].y)
                q = Point(qx, qy, points[i].id)
                new_points.append(q)
                points.insert(i, q)
                D = 0.0
            else:
                D += d
        i += 1

    if len(new_points) == n - 1:
        last_point = points[-1]
        new_points.append(Point(last_point.x, last_point.y, last_point.id))

    return new_points


def scale(points):
    min_x, max_x = float('inf'), float('-inf')
    min_y, max_y = float('inf'), float('-inf')

    for p in points:
        min_x = min(min_x, p.x)
        min_y = min(min_y, p.y)
        max_x = max(max_x, p.x)
        max_y = max(max_y, p.y)

    size = max(max_x - min_x, max_y - min_y)
    new_points = []
    for p in points:
        qx = (p.x - min_x) / size
        qy = (p.y - min_y) / size
        new_points.append(Point(qx, qy, p.id))

    return new_points


def translate_to(points, pt):
    c = centroid(points)
    new_points = []
    for p in points:
        qx = p.x + pt.x - c.x
        qy = p.y + pt.y - c.y
        new_points.append(Point(qx, qy, p.id))

    return new_points


def centroid(points):
    x_sum, y_sum = 0.0, 0.0
    for p in points:
        x_sum += p.x
        y_sum += p.y

    return Point(x_sum / len(points), y_sum / len(points), 0)


def path_length(points):
    d = 0.0
    for i in range(1, len(points)):
        if points[i].id == points[i - 1].id:
            d += euclidean_distance(points[i - 1], points[i])
    return d


def make_int_coords(points):
    for p in points:
        p.int_x = round((p.x + 1.0) / 2.0 * (MAX_INT_COORD - 1))
        p.int_y = round((p.y + 1.0) / 2.0 * (MAX_INT_COORD - 1))
    return points


def compute_lut(points):
    lut = [[0 for _ in range(LUT_SIZE)] for _ in range(LUT_SIZE)]

    for x in range(LUT_SIZE):
        for y in range(LUT_SIZE):
            u = -1
            b = float('inf')
            for i, p in enumerate(points):
                row = round(p.int_x / LUT_SCALE_FACTOR)
                col = round(p.int_y / LUT_SCALE_FACTOR)
                d = ((row - x) ** 2) + ((col - y) ** 2)
                if d < b:
                    b = d
                    u = i
            lut[x][y] = u

    return lut


def sqr_euclidean_distance(pt1, pt2):
    dx = pt2.x - pt1.x
    dy = pt2.y - pt1.y
    return dx * dx + dy * dy


def euclidean_distance(pt1, pt2):
    return math.sqrt(sqr_euclidean_distance(pt1, pt2))


#
# QDollarRecognizer class
#
class QDollarRecognizer:
    def __init__(self):
        self.point_clouds = []

        # one predefined point-cloud for each gesture
        self.point_clouds.append(PointCloud("T", [
            Point(30, 7, 1), Point(103, 7, 1),
            Point(66, 7, 2), Point(66, 87, 2)
        ]))
        self.point_clouds.append(PointCloud("N", [
            Point(177, 92, 1), Point(177, 2, 1),
            Point(182, 1, 2), Point(246, 95, 2),
            Point(247, 87, 3), Point(247, 1, 3)
        ]))
        self.point_clouds.append(PointCloud("D", [
            Point(345, 9, 1), Point(345, 87, 1),
            Point(351, 8, 2), Point(363, 8, 2), Point(372, 9, 2), Point(380, 11, 2), Point(386, 14, 2),
            Point(391, 17, 2), Point(394, 22, 2), Point(397, 28, 2), Point(399, 34, 2), Point(400, 42, 2),
            Point(400, 50, 2), Point(400, 56, 2), Point(399, 61, 2), Point(397, 66, 2), Point(394, 70, 2),
            Point(391, 74, 2), Point(386, 78, 2), Point(382, 81, 2), Point(377, 83, 2), Point(372, 85, 2),
            Point(367, 87, 2), Point(360, 87, 2), Point(355, 88, 2), Point(349, 87, 2)
        ]))
        self.point_clouds.append(PointCloud("P", [
            Point(507, 8, 1), Point(507, 87, 1),
            Point(513, 7, 2), Point(528, 7, 2), Point(537, 8, 2), Point(544, 10, 2), Point(550, 12, 2),
            Point(555, 15, 2), Point(558, 18, 2), Point(560, 22, 2), Point(561, 27, 2), Point(562, 33, 2),
            Point(561, 37, 2), Point(559, 42, 2), Point(556, 45, 2), Point(550, 48, 2), Point(544, 51, 2),
            Point(538, 53, 2), Point(532, 54, 2), Point(525, 55, 2), Point(519, 55, 2), Point(513, 55, 2),
            Point(510, 55, 2)
        ]))
        self.point_clouds.append(PointCloud("X", [
            Point(30, 146, 1), Point(106, 222, 1),
            Point(30, 225, 2), Point(106, 146, 2)
        ]))
        self.point_clouds.append(PointCloud("H", [
            Point(188, 137, 1), Point(188, 225, 1),
            Point(188, 180, 2), Point(241, 180, 2),
            Point(241, 137, 3), Point(241, 225, 3)
        ]))
        self.point_clouds.append(PointCloud("I", [
            Point(371, 149, 1), Point(371, 221, 1),
            Point(341, 149, 2), Point(401, 149, 2),
            Point(341, 221, 3), Point(401, 221, 3)
        ]))
        self.point_clouds.append(PointCloud("exclamation", [
            Point(526, 142, 1), Point(526, 204, 1),
            Point(526, 221, 2)
        ]))
        self.point_clouds.append(PointCloud("line", [
            Point(12, 347, 1), Point(119, 347, 1)
        ]))
        self.point_clouds.append(PointCloud("five-point star", [
            Point(177, 396, 1), Point(223, 299, 1), Point(262, 396, 1), Point(168, 332, 1), Point(278, 332, 1),
            Point(184, 397, 1)
        ]))
        self.point_clouds.append(PointCloud("null", [
            Point(382, 310, 1), Point(377, 308, 1), Point(373, 307, 1), Point(366, 307, 1), Point(360, 310, 1),
            Point(356, 313, 1), Point(353, 316, 1), Point(349, 321, 1), Point(347, 326, 1), Point(344, 331, 1),
            Point(342, 337, 1), Point(341, 343, 1), Point(341, 350, 1), Point(341, 358, 1), Point(342, 362, 1),
            Point(344, 366, 1), Point(347, 370, 1), Point(351, 374, 1), Point(356, 379, 1), Point(361, 382, 1),
            Point(368, 385, 1), Point(374, 387, 1), Point(381, 387, 1), Point(390, 387, 1), Point(397, 385, 1),
            Point(404, 382, 1), Point(408, 378, 1), Point(412, 373, 1), Point(416, 367, 1), Point(418, 361, 1),
            Point(419, 353, 1), Point(418, 346, 1), Point(417, 341, 1), Point(416, 336, 1), Point(413, 331, 1),
            Point(410, 326, 1), Point(404, 320, 1), Point(400, 317, 1), Point(393, 313, 1), Point(392, 312, 1),
            Point(418, 309, 2), Point(337, 390, 2)
        ]))
        self.point_clouds.append(PointCloud("arrowhead", [
            Point(506, 349, 1), Point(574, 349, 1),
            Point(525, 306, 2), Point(584, 349, 2), Point(525, 388, 2)
        ]))
        self.point_clouds.append(PointCloud("pitchfork", [
            Point(38, 470, 1), Point(36, 476, 1), Point(36, 482, 1), Point(37, 489, 1), Point(39, 496, 1),
            Point(42, 500, 1), Point(46, 503, 1), Point(50, 507, 1), Point(56, 509, 1), Point(63, 509, 1),
            Point(70, 508, 1), Point(75, 506, 1), Point(79, 503, 1), Point(82, 499, 1), Point(85, 493, 1),
            Point(87, 487, 1), Point(88, 480, 1), Point(88, 474, 1), Point(87, 468, 1),
            Point(62, 464, 2), Point(62, 571, 2)
        ]))
        self.point_clouds.append(PointCloud("six-point star", [
            Point(177, 554, 1), Point(223, 476, 1), Point(268, 554, 1), Point(183, 554, 1),
            Point(177, 490, 2), Point(223, 568, 2), Point(268, 490, 2), Point(183, 490, 2)
        ]))
        self.point_clouds.append(PointCloud("asterisk", [
            Point(325, 499, 1), Point(417, 557, 1),
            Point(417, 499, 2), Point(325, 557, 2),
            Point(371, 486, 3), Point(371, 571, 3)
        ]))
        self.point_clouds.append(PointCloud("half-note", [
            Point(546, 465, 1), Point(546, 531, 1),
            Point(540, 530, 2), Point(536, 529, 2), Point(533, 528, 2), Point(529, 529, 2), Point(524, 530, 2),
            Point(520, 532, 2), Point(515, 535, 2), Point(511, 539, 2), Point(508, 545, 2), Point(506, 548, 2),
            Point(506, 554, 2), Point(509, 558, 2), Point(512, 561, 2), Point(517, 564, 2), Point(521, 564, 2),
            Point(527, 563, 2), Point(531, 560, 2), Point(535, 557, 2), Point(538, 553, 2), Point(542, 548, 2),
            Point(544, 544, 2), Point(546, 540, 2), Point(546, 536, 2)
        ]))

    #
    # The $Q Point-Cloud Recognizer API begins here -- 3 methods
    #
    def save_gesture_cache(self, cache_path):
        with open(cache_path, 'wb') as f:
            pickle.dump(self.point_clouds, f)

    def load_gesture_cache(self, cache_path):
        with open(cache_path, 'rb') as f:
            self.point_clouds = pickle.load(f)

    def recognize(self, points):
        t0 = time.time()
        candidate = PointCloud("", points)

        u = -1
        b = float('inf')

        for i, template in enumerate(self.point_clouds):
            d = cloud_match(candidate, template, b)
            if d < b:
                b = d  # best (least) distance
                u = i  # point-cloud index

        t1 = time.time()

        if u == -1:
            return Result("No match.", 0.0, (t1 - t0) * 1000)
        else:
            score = 1.0 / b if b > 1.0 else 1.0
            return Result(self.point_clouds[u].name, score, (t1 - t0) * 1000)

    def add_gesture(self, name, points):
        self.point_clouds.append(PointCloud(name, points))
        num = sum(1 for pc in self.point_clouds if pc.name == name)
        return num

    def delete_user_gestures(self):
        self.point_clouds = self.point_clouds[:NUM_POINT_CLOUDS]
        return NUM_POINT_CLOUDS

    def load_gesture_from_xml(self, path, gesture_name=None):
        """
        XML 파일에서 제스처를 읽어와 recognizer에 추가합니다.
        gesture_name을 지정하지 않으면 XML의 Name 속성을 사용합니다.
        """
        if os.path.isdir(path):
            for filename in os.listdir(path):
                if filename.lower().endswith('.xml'):
                    #ramona_idle_ani()
                    xml_path = os.path.join(path, filename)
                    self.load_gesture_from_xml(xml_path)
        else:
            tree = ET.parse(path)
            root = tree.getroot()
            file_base = os.path.splitext(os.path.basename(path))[0]
            name = gesture_name or root.attrib.get('Name') or file_base
            points = []
            for stroke_id, stroke in enumerate(root.findall('Stroke'), start=1):
                for pt in stroke.findall('Point'):
                    x = float(pt.attrib['X'])
                    y = float(pt.attrib['Y'])
                    points.append(Point(x, y, stroke_id))
            return self.add_gesture(name, points)

#
# Example of how to use the recognizer
#
if __name__ == "__main__":
    # 1. Create a recognizer object
    recognizer = QDollarRecognizer()

    # 2. Define a gesture to be recognized (e.g., a simple horizontal line)
    #    In a real application, these points would come from a mouse or touch input.
    test_gesture_points = [
        Point(20, 200, 1),
        Point(35, 202, 1),
        Point(50, 199, 1),
        Point(70, 201, 1),
        Point(90, 200, 1),
        Point(110, 198, 1)
    ]

    # 3. Recognize the gesture
    result = recognizer.recognize(test_gesture_points)

    # 4. Print the result
    print(f"Gesture Recognized: {result.name}")
    print(f"Score (Confidence): {result.score:.2f}")
    print(f"Time taken: {result.time:.2f} ms")

    print("-" * 20)

    # Example of adding a new gesture
    print("Adding a new custom gesture: 'circle'")
    circle_points = []
    for i in range(0, 361, 10):
        rad = math.radians(i)
        x = 100 + 50 * math.cos(rad)
        y = 100 + 50 * math.sin(rad)
        circle_points.append(Point(x, y, 1))

    num_circles = recognizer.add_gesture("circle", circle_points)
    print(f"Number of 'circle' gestures stored: {num_circles}")

    result_circle = recognizer.recognize(circle_points)
    print(f"Recognizing the added gesture: {result_circle.name}")
    print(f"Score: {result_circle.score:.2f}")