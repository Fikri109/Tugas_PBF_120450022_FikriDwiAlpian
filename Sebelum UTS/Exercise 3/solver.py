def euler(t, h, y, dy, Func): # defenisikan fungsi euler
    d2y = Func(t, y, dy)
    y_next = y + (h * dy)
    dy_next = dy + (h * d2y)
    return (y_next, dy_next)

def euler_cromer(t, h, y, dy, Func): # defenisikan funggsi euler_cromer
    d2y = Func(t, y, dy)
    dy_next = dy + (h * d2y)
    y_next = y + (h * dy_next)

    return (y_next, dy_next)
