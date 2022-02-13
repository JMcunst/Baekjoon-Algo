from ipaddress import collapse_addresses


# color = ["RG", "WR", "BW", "GG"]
# prices = [5000, 6000]
# color = ["RG", "WR", "BW", "GG"]
# prices = [2000, 6000]
# color = ["BW", "RY", "BY"]
# prices = [9000, 10000]	
color = ["YW", "RY", "WG", "BW"]
prices = [7561, 8945]


def solution(color, prices):
    answer = 0
    color_dict = {}
    cost_all = []

    color_dict['up_blue'] = 0
    color_dict['up_red'] = 0
    color_dict['up_green'] = 0
    color_dict['up_white'] = 0
    color_dict['down_blue'] = 0
    color_dict['down_red'] = 0
    color_dict['down_green'] = 0
    color_dict['down_white'] = 0

    cnt_red_l = 0
    cnt_blue_l = 0
    cnt_green_l = 0
    cnt_white_l = 0

    cnt_red_m = 0
    cnt_blue_m = 0
    cnt_green_m = 0
    cnt_white_m = 0

    for col in color:
        up, down = col[0], col[1]
        print(up, down)

        if up == 'R':
            color_dict['up_red'] += 1
        elif up == 'G':
            color_dict['up_green'] += 1
        elif up == 'W':
            color_dict['up_white'] += 1
        elif up == 'B':
            color_dict['up_blue'] += 1

        if down == 'R':
            color_dict['down_red'] += 1
        elif down == 'G':
            color_dict['down_green'] += 1
        elif down == 'W':
            color_dict['down_white'] += 1
        elif down == 'B':
            color_dict['down_blue'] += 1

    print(color_dict)

    if color_dict['up_red'] >= color_dict['down_red']:
        cnt_red_l = color_dict['down_red']
        cnt_red_m = color_dict['up_red']
    else:
        cnt_red_l = color_dict['up_red']
        cnt_red_m = color_dict['down_red']

    if color_dict['up_blue'] >= color_dict['down_blue']:
        cnt_blue_l = color_dict['down_blue']
        cnt_blue_m = color_dict['up_blue']
    else:
        cnt_blue_l = color_dict['up_blue']
        cnt_blue_m = color_dict['down_blue']

    if color_dict['up_green'] >= color_dict['down_green']:
        cnt_green_l = color_dict['down_green']
        cnt_green_m = color_dict['up_green']
    else:
        cnt_green_l = color_dict['up_red']
        cnt_green_m = color_dict['down_green']

    if color_dict['up_white'] >= color_dict['down_white']:
        cnt_white_l = color_dict['down_white']
        cnt_white_m = color_dict['up_white']
    else:
        cnt_white_l = color_dict['up_white']
        cnt_white_m = color_dict['down_white']

    cnt_set_m = cnt_red_m + cnt_blue_m + cnt_green_m + cnt_white_m
    print('mcount::',cnt_red_m, cnt_blue_m, cnt_green_m, cnt_white_m )
    cost_set_m = cnt_set_m * prices[0]
    print('cnt_set_m::', cnt_set_m, cost_set_m)
    cost_all.append(cost_set_m)

    cnt_set_l = cnt_red_l + cnt_blue_l + cnt_green_l + cnt_white_l
    cost_set_l = cnt_set_l * prices[0]
    print('cnt_set_l::',cnt_set_l, cost_set_l)

    if color_dict['down_red'] > color_dict['up_red']:
        cnt_red_alone = color_dict['down_red'] - cnt_red_l
    elif color_dict['down_red'] < color_dict['up_red']:
        cnt_red_alone = color_dict['up_red'] - cnt_red_l
    else:
        cnt_red_alone = 0

    if color_dict['down_blue'] > color_dict['up_blue']:
        cnt_blue_alone = color_dict['down_blue'] - cnt_blue_l
    elif color_dict['down_blue'] < color_dict['up_blue']:
        cnt_blue_alone = color_dict['up_blue'] - cnt_blue_l
    else:
        cnt_blue_alone = 0

    if color_dict['down_green'] > color_dict['up_green']:
        cnt_green_alone = color_dict['down_green'] - cnt_green_l
    elif color_dict['down_green'] < color_dict['up_green']:
        cnt_green_alone = color_dict['up_green'] - cnt_green_l
    else:
        cnt_green_alone = 0

    if color_dict['down_white'] > color_dict['up_white']:
        cnt_white_alone = color_dict['down_white'] - cnt_white_l
    elif color_dict['down_white'] < color_dict['up_white']:
        cnt_white_alone = color_dict['up_white'] - cnt_white_l
    else:
        cnt_white_alone = 0

    cnt_alone = cnt_red_alone + cnt_blue_alone + cnt_green_alone + cnt_white_alone - 1
    cost_alone = cnt_alone * prices[1]
    print(cnt_alone, cost_alone)

    answer = cost_set_l + cost_alone
    print(answer)
    cost_all.append(answer)
    
    return min(cost_all)

solution(color,prices)