def lefttop(tx, ty, bx, by):
    return [tx + ty * (4096/4) + bx * 32 + by * (4096/4)*32, \
        tx + (4096/4) + ty * (4096/4) + bx * 32 + by * (4096/4)*32, \
        tx + (4096/4)*2 + ty * (4096/4) + bx * 32 + by * (4096/4)*32, \
        tx + (4096/4)*3 + ty * (4096/4) + bx * 32 + by * (4096/4)*32 \
        ]


def righttop(tx, ty, bx, by):
    return [tx + ty * (4096/4) + bx * 32 + by * (4096/4)*32 + 16, \
        tx + (4096/4) + ty * (4096/4) + bx * 32 + by * (4096/4)*32 + 16, \
        tx + (4096/4)*2 + ty * (4096/4) + bx * 32 + by * (4096/4)*32 + 16, \
        tx + (4096/4)*3 + ty * (4096/4) + bx * 32 + by * (4096/4)*32 + 16\
            ]

def leftbottom(tx, ty, bx, by):
    return [tx + ty * (4096/4) + bx * 32 + by * (4096/4)*32 + 16 * (4096/4), \
        tx + (4096/4) + ty * (4096/4) + bx * 32 + by * (4096/4)*32 + 16 * (4096/4), \
        tx + (4096/4)*2 + ty * (4096/4) + bx * 32 + by * (4096/4)*32 + 16 * (4096/4), \
        tx + (4096/4)*3 + ty * (4096/4) + bx * 32 + by * (4096/4)*32 + 16 * (4096/4)\
            ]

def rightbottom(tx, ty, bx, by):
    return [tx + ty * (4096/4) + bx * 32 + by * (4096/4)*32 + 16 * (4096/4) + 16, \
        tx + (4096/4) + ty * (4096/4) + bx * 32 + by * (4096/4)*32 + 16 * (4096/4) + 16, \
        tx + (4096/4)*2 + ty * (4096/4) + bx * 32 + by * (4096/4)*32 + 16 * (4096/4) + 16, \
        tx + (4096/4)*3 + ty * (4096/4) + bx * 32 + by * (4096/4)*32 + 16 * (4096/4) + 16\
            ]


print lefttop(1,1,1,1), righttop(1,1,1,1), leftbottom(1,1,1,1), rightbottom(1,1,1,1)
