import math

cookie_id = ['ID', 'Cookie Type' ,'Portion Eggs','Portion Butter','Portion Sugar','Portion Flour' ]

cookie_info = [[ 1 , 'Shortbread'  ,     0.14     ,       0.14     ,      0.28     ,     0.44      ],
[ 2  , 'Shortbread'  ,     0.10     ,       0.18     ,      0.28     ,     0.44      ],
[ 3  , 'Shortbread'  ,     0.12     ,       0.10     ,      0.33     ,     0.45      ],
[ 4  , 'Shortbread'  ,     0.10     ,       0.25     ,      0.25     ,     0.40      ],
[ 5  , 'Sugar'       ,     0.00     ,       0.10     ,      0.40     ,     0.50      ],
[ 6  , 'Sugar'       ,     0.00     ,       0.20     ,      0.40     ,     0.40      ],
[ 7  , 'Sugar'       ,     0.10     ,       0.08     ,      0.35     ,     0.47      ],
[ 8  , 'Sugar'       ,     0.00     ,       0.05     ,      0.30     ,     0.65      ],
[ 9  , 'Fortune'     ,     0.20     ,       0.00     ,      0.40     ,     0.40      ],
[ 10 , 'Fortune'     ,     0.25     ,       0.10     ,      0.30     ,     0.35      ],
[ 11 , 'Fortune'     ,     0.22     ,       0.15     ,      0.50     ,     0.13      ],
[ 12 , 'Fortune'     ,     0.15     ,       0.20     ,      0.35     ,     0.30      ],
[ 13 , 'Fortune'     ,     0.22     ,       0.00     ,      0.40     ,     0.38      ]]



def cookie_distance(cookie_info, points):
    all_distances = {}
    for cookie in cookie_info:
        distance_sum = 0
        for i in range(len(points)):
            distance_sum += (points[i] - cookie[i+2])**2
        cookie_index = cookie_info.index(cookie)
        all_distances.update({cookie_info[cookie_index][0]:distance_sum**(0.5)})
    return all_distances

    


cookie_distances = cookie_distance(cookie_info, [0.1, 0.15, 0.3, 0.45])
# print(cookie_distances)
sort_cookies = sorted(cookie_distances.items(), key=lambda x: x[1])
print(sort_cookies)


cookies = ['Fortune', 'Shortbread', 'Sugar']
cookies_avg = []
for j in range(3):
    cookie_sum = 0
    cookie_amount = 0
    for i in range(len(sort_cookies)):
        if cookies[j] in cookie_info[sort_cookies[i][0] - 1]:
            cookie_amount+= 1
            cookie_sum += sort_cookies[i][1]
            print(cookie_info[sort_cookies[i][0] - 1])
    cookies_avg.append(cookie_sum/cookie_amount)
print(cookies_avg)
