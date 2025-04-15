import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2=pg.transform.flip(bg_img, True, False)
    image=pg.image.load("fig/3.png")
    image=pg.transform.flip(image, True, False)
    image_rct=image.get_rect()
    image_rct.center=300,200
    tmr = 0
    


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        image_rct.move_ip((-1,0))
        key_lst=pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            image_rct.move_ip((0,-1))
        if key_lst[pg.K_DOWN]:
            image_rct.move_ip((0,1))
        if key_lst[pg.K_LEFT]:
            image_rct.move_ip((-1,0))
        if key_lst[pg.K_RIGHT]:
            image_rct.move_ip((1,0))
        tmr=tmr%3200
        screen.blit(bg_img,[-tmr,0])
        screen.blit(bg_img2, [-tmr+1600,0])
        screen.blit(bg_img,[-tmr+3200,0])
        screen.blit(image,image_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200)
    


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()