
def select_resolution( ScreenWhidthHeight: list[int] ):

    if ScreenWhidthHeight[0] == 1920 and ScreenWhidthHeight[1] == 1080:
        ScreenWhidthHeight[0] = 1680
        ScreenWhidthHeight[1] = 1050
    elif ScreenWhidthHeight[0] == 1680 and ScreenWhidthHeight[1] == 1050:
        ScreenWhidthHeight[0] = 1280
        ScreenWhidthHeight[1] = 1024
    elif ScreenWhidthHeight[0] == 1280 and ScreenWhidthHeight[1] == 1024:
        ScreenWhidthHeight[1] = 960
    elif ScreenWhidthHeight[0] == 1280 and ScreenWhidthHeight[1] == 960:
        ScreenWhidthHeight[1] = 720
    elif ScreenWhidthHeight[0] == 1280 and ScreenWhidthHeight[1] == 720:
        ScreenWhidthHeight[0] = 1024
        ScreenWhidthHeight[1] = 768
    elif ScreenWhidthHeight[0] == 1024 and ScreenWhidthHeight[1] == 768:
        ScreenWhidthHeight[0] = 800
        ScreenWhidthHeight[1] = 600
    elif ScreenWhidthHeight[0] == 800 and ScreenWhidthHeight[1] == 600:
        ScreenWhidthHeight[0] = 1920
        ScreenWhidthHeight[1] = 1080 
        