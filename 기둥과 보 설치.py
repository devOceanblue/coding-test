'''
기둥과 보 설치
'''


def solution(build_frame):
    def is_buildable(f, m):
        '''
        1. 기둥은 바닥위에있거나 보의 한쪽 끝부분 위에 있거나, 또는 다른 기둥 위에 있어야한다
        2. 보는 한쪽 끝부분이 기둥 위에 있거나 또는 양쪽 끝부분이 다른 보와 동시에 연결되어있어야 한다
        '''
        if f[3] == 0:
            if f[1] == 0 or [f[0] - 1, f[1], 1] in m or [f[0] + 1, f[1], 1] in m or [f[0], f[1] - 1, 0] in m:
                return True
            else:
                return False
        elif f[3] == 1:
            if [f[0], f[1] - 1, 0] in m or [f[0] + 1, f[1] - 1, 0] in m or (
                    [f[0] - 1, f[1], 1] in m and [f[0] + 1, f[1], 1] in m):
                return True
            else:
                return False

    def is_tearable(f, m):
        '''
        1. 기둥을 삭제할 경우 다른 기둥을 지탱하고 있는지 또는 다른 보가 붙어있는지 체크
        2. 보를 삭제할 경우 다른 기둥을 지탱하고 있는지 또는 다른 보를 지탱하고 있는지 체크
        '''

    def build(f, m):
        m.append(f[:-1])
        return

    def teardown(f, m):
        m.remove(f[:-1])
        return

    current_map = []
    for f in build_frame:
        if f[3] == 1:
            if is_buildable(f):
                build(f, current_map)
        elif f[3] == 0:
            if is_tearable(f):
                teardown(f, current_map)
