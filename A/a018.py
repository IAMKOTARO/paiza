import math

def is_inside_sector(center_x, center_y, target_x, target_y, start_angle, end_angle, radius):
    dx = target_x - center_x
    dy = target_y - center_y
    sx = math.cos(math.radians(start_angle))
    sy = math.sin(math.radians(start_angle))
    ex = math.cos(math.radians(end_angle))
    ey = math.sin(math.radians(end_angle))

    if dx ** 2 + dy ** 2 > radius ** 2:
        return False

    if sx * ey - ex * sy > 0:
        if sx * dy - dx * sy < 0:
            return False
        if ex * dy - dx * ey > 0:
            return False
        return True
    else:
        if sx * dy - dx * sy >= 0:
            return True
        if ex * dy - dx * ey <= 0:
            return True
        return False


W, H, M, N = map(int, input().split())
cameras = []
for i in range(M):
    cameras.append(list(map(int, input().split())))
objects = []
for i in range(N):
    objects.append(list(map(int, input().split())))
for obj in objects:
    a, b = obj
    is_under_surveillance = False
    for cam in cameras:
        x, y, t, d, r = cam
        if is_inside_sector(
            center_x=x,
            center_y=y,
            target_x=a,
            target_y=b,
            start_angle=t-d/2,
            end_angle=t+d/2,
            radius=r
            ):
            is_under_surveillance=True
            print('yes')
            break
    if not is_under_surveillance:
        print('no')
