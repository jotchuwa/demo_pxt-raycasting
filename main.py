def spawnCoin():
    global mySprite
    mySprite = sprites.create(img("""
            . . b b b b . . 
                    . b 5 5 5 5 b . 
                    b 5 d 3 3 d 5 b 
                    b 5 3 5 5 1 5 b 
                    c 5 3 5 5 1 d c 
                    c d d 1 1 d d c 
                    . f d d d d f . 
                    . . f f f f . .
        """),
        SpriteKind.food)
    Render.takeover_scene_sprites()
    mySprite.scale = 0.5
    mySprite.set_bounce_on_wall(True)
    mySprite.set_velocity(15, 16)
    Render.set_offset_z(mySprite, -24)
    tiles.place_on_random_tile(mySprite, assets.tile("""
        transparency16
    """))
    Render.set_sprite_animations(mySprite,
        Render.create_animations(150,
            [img("""
                    . . b b b b . . 
                            . b 5 5 5 5 b . 
                            b 5 d 3 3 d 5 b 
                            b 5 3 5 5 1 5 b 
                            c 5 3 5 5 1 d c 
                            c d d 1 1 d d c 
                            . f d d d d f . 
                            . . f f f f . .
                """),
                img("""
                    . . b b b . . . 
                            . b 5 5 5 b . . 
                            b 5 d 3 d 5 b . 
                            b 5 3 5 1 5 b . 
                            c 5 3 5 1 d c . 
                            c 5 d 1 d d c . 
                            . f d d d f . . 
                            . . f f f . . .
                """),
                img("""
                    . . . b b . . . 
                            . . b 5 5 b . . 
                            . b 5 d 1 5 b . 
                            . b 5 3 1 5 b . 
                            . c 5 3 1 d c . 
                            . c 5 1 d d c . 
                            . . f d d f . . 
                            . . . f f . . .
                """),
                img("""
                    . . . b b . . . 
                            . . b 5 5 b . . 
                            . . b 1 1 b . . 
                            . . b 5 5 b . . 
                            . . b d d b . . 
                            . . c d d c . . 
                            . . c 3 3 c . . 
                            . . . f f . . .
                """),
                img("""
                    . . . b b . . . 
                            . . b 5 5 b . . 
                            . b 5 1 d 5 b . 
                            . b 5 1 3 5 b . 
                            . c d 1 3 5 c . 
                            . c d d 1 5 c . 
                            . . f d d f . . 
                            . . . f f . . .
                """),
                img("""
                    . . . b b b . . 
                            . . b 5 5 5 b . 
                            . b 5 d 3 d 5 b 
                            . b 5 1 5 3 5 b 
                            . c d 1 5 3 5 c 
                            . c d d 1 d 5 c 
                            . . f d d d f . 
                            . . . f f f . .
                """)]))
    return mySprite

def on_b_pressed():
    while controller.B.is_pressed() and Render.get_attribute(Render.attribute.FOV) > Render.get_default_fov() - 0.6:
        Render.set_attribute(Render.attribute.FOV,
            Render.get_attribute(Render.attribute.FOV) - 0.06)
        pause(20)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . 6 6 6 6 . . . . . . 
                    . . . . 6 6 6 5 5 6 6 6 . . . . 
                    . . . 7 7 7 7 6 6 6 6 6 6 . . . 
                    . . 6 7 7 7 7 8 8 8 1 1 6 6 . . 
                    . . 7 7 7 7 7 8 8 8 1 1 5 6 . . 
                    . 6 7 7 7 7 8 8 8 8 8 5 5 6 6 . 
                    . 6 7 7 7 8 8 8 6 6 6 6 5 6 6 . 
                    . 6 6 7 7 8 8 6 6 6 6 6 6 6 6 . 
                    . 6 8 7 7 8 8 6 6 6 6 6 6 6 6 . 
                    . . 6 8 7 7 8 6 6 6 6 6 8 6 . . 
                    . . 6 8 8 7 8 8 6 6 6 8 6 6 . . 
                    . . . 6 8 8 8 8 8 8 8 8 6 . . . 
                    . . . . 6 6 8 8 8 8 6 6 . . . . 
                    . . . . . . 6 6 6 6 . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        Render.get_render_sprite_instance(),
        Render.get_attribute(Render.attribute.DIR_X) * 44,
        Render.get_attribute(Render.attribute.DIR_Y) * 44)
    projectile.scale = 0.5
    music.ba_ding.play()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    music.ba_ding.play()
    info.change_score_by(1)
    sprite.destroy()
    otherSprite.destroy()
sprites.on_overlap(SpriteKind.enemy, SpriteKind.projectile, on_on_overlap)

def on_menu_pressed():
    Render.toggle_view_mode()
controller.menu.on_event(ControllerButtonEvent.PRESSED, on_menu_pressed)

def on_b_released():
    while Render.get_attribute(Render.attribute.FOV) < Render.get_default_fov():
        Render.set_attribute(Render.attribute.FOV,
            Render.get_attribute(Render.attribute.FOV) + 0.06)
        pause(20)
controller.B.on_event(ControllerButtonEvent.RELEASED, on_b_released)

def on_on_overlap2(sprite2, otherSprite2):
    music.ba_ding.play()
    info.change_life_by(1)
    otherSprite2.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap2)

def spawnEnemy():
    global listAni, listImg, index, mySprite
    listAni = [Render.create_animations(150,
            [img("""
                    . . . . f f f f f f . . . . . . 
                            . . . f 2 f e e e e f f . . . . 
                            . . f 2 2 2 f e e e e f f . . . 
                            . . f e e e e f f e e e f . . . 
                            . f e 2 2 2 2 e e f f f f . . . 
                            . f 2 e f f f f 2 2 2 e f . . . 
                            . f f f e e e f f f f f f f . . 
                            . f e e 4 4 f b e 4 4 e f f . . 
                            . . f e d d f 1 4 d 4 e e f . . 
                            . . . f d d d d 4 e e e f . . . 
                            . . . f e 4 4 4 e e f f . . . . 
                            . . . f 2 2 2 e d d 4 . . . . . 
                            . . . f 2 2 2 e d d e . . . . . 
                            . . . f 5 5 4 f e e f . . . . . 
                            . . . . f f f f f f . . . . . . 
                            . . . . . . f f f . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                            . . . . f f f f f f . . . . . . 
                            . . . f 2 f e e e e f f . . . . 
                            . . f 2 2 2 f e e e e f f . . . 
                            . . f e e e e f f e e e f . . . 
                            . f e 2 2 2 2 e e f f f f . . . 
                            . f 2 e f f f f 2 2 2 e f . . . 
                            . f f f e e e f f f f f f f . . 
                            . f e e 4 4 f b e 4 4 e f f . . 
                            . . f e d d f 1 4 d 4 e e f . . 
                            . . . f d d d e e e e e f . . . 
                            . . . f e 4 e d d 4 f . . . . . 
                            . . . f 2 2 e d d e f . . . . . 
                            . . f f 5 5 f e e f f f . . . . 
                            . . f f f f f f f f f f . . . . 
                            . . . f f f . . . f f . . . . .
                """),
                img("""
                    . . . . f f f f f f . . . . . . 
                            . . . f 2 f e e e e f f . . . . 
                            . . f 2 2 2 f e e e e f f . . . 
                            . . f e e e e f f e e e f . . . 
                            . f e 2 2 2 2 e e f f f f . . . 
                            . f 2 e f f f f 2 2 2 e f . . . 
                            . f f f e e e f f f f f f f . . 
                            . f e e 4 4 f b e 4 4 e f f . . 
                            . . f e d d f 1 4 d 4 e e f . . 
                            . . . f d d d d 4 e e e f . . . 
                            . . . f e 4 4 4 e e f f . . . . 
                            . . . f 2 2 2 e d d 4 . . . . . 
                            . . . f 2 2 2 e d d e . . . . . 
                            . . . f 5 5 4 f e e f . . . . . 
                            . . . . f f f f f f . . . . . . 
                            . . . . . . f f f . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                            . . . . f f f f f f . . . . . . 
                            . . . f 2 f e e e e f f . . . . 
                            . . f 2 2 2 f e e e e f f . . . 
                            . . f e e e e f f e e e f . . . 
                            . f e 2 2 2 2 e e f f f f . . . 
                            . f 2 e f f f f 2 2 2 e f . . . 
                            . f f f e e e f f f f f f f . . 
                            . f e e 4 4 f b e 4 4 e f f . . 
                            . . f e d d f 1 4 d 4 e e f . . 
                            . . . f d d d d 4 e e e f . . . 
                            . . . f e 4 4 4 e d d 4 . . . . 
                            . . . f 2 2 2 2 e d d e . . . . 
                            . . f f 5 5 4 4 f e e f . . . . 
                            . . f f f f f f f f f f . . . . 
                            . . . f f f . . . f f . . . . .
                """)],
            [img("""
                    . . . . . . f f f f . . . . . . 
                            . . . . f f f 2 2 f f f . . . . 
                            . . . f f f 2 2 2 2 f f f . . . 
                            . . f f f e e e e e e f f f . . 
                            . . f f e 2 2 2 2 2 2 e e f . . 
                            . . f e 2 f f f f f f 2 e f . . 
                            . . f f f f e e e e f f f f . . 
                            . f f e f b f 4 4 f b f e f f . 
                            . f e e 4 1 f d d f 1 4 e e f . 
                            . . f e e d d d d d d e e f . . 
                            . . . f e e 4 4 4 4 e e f . . . 
                            . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                            . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                            . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                            . . . . . f f f f f f . . . . . 
                            . . . . . f f . . f f . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                            . . . . . . f f f f . . . . . . 
                            . . . . f f f 2 2 f f f . . . . 
                            . . . f f f 2 2 2 2 f f f . . . 
                            . . f f f e e e e e e f f f . . 
                            . . f f e 2 2 2 2 2 2 e e f . . 
                            . f f e 2 f f f f f f 2 e f f . 
                            . f f f f f e e e e f f f f f . 
                            . . f e f b f 4 4 f b f e f . . 
                            . . f e 4 1 f d d f 1 4 e f . . 
                            . . . f e 4 d d d d 4 e f e . . 
                            . . f e f 2 2 2 2 e d d 4 e . . 
                            . . e 4 f 2 2 2 2 e d d e . . . 
                            . . . . f 4 4 5 5 f e e . . . . 
                            . . . . f f f f f f f . . . . . 
                            . . . . f f f . . . . . . . . .
                """),
                img("""
                    . . . . . . f f f f . . . . . . 
                            . . . . f f f 2 2 f f f . . . . 
                            . . . f f f 2 2 2 2 f f f . . . 
                            . . f f f e e e e e e f f f . . 
                            . . f f e 2 2 2 2 2 2 e e f . . 
                            . . f e 2 f f f f f f 2 e f . . 
                            . . f f f f e e e e f f f f . . 
                            . f f e f b f 4 4 f b f e f f . 
                            . f e e 4 1 f d d f 1 4 e e f . 
                            . . f e e d d d d d d e e f . . 
                            . . . f e e 4 4 4 4 e e f . . . 
                            . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                            . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                            . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                            . . . . . f f f f f f . . . . . 
                            . . . . . f f . . f f . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                            . . . . . . f f f f . . . . . . 
                            . . . . f f f 2 2 f f f . . . . 
                            . . . f f f 2 2 2 2 f f f . . . 
                            . . f f f e e e e e e f f f . . 
                            . . f e e 2 2 2 2 2 2 e f f . . 
                            . f f e 2 f f f f f f 2 e f f . 
                            . f f f f f e e e e f f f f f . 
                            . . f e f b f 4 4 f b f e f . . 
                            . . f e 4 1 f d d f 1 4 e f . . 
                            . . e f e 4 d d d d 4 e f . . . 
                            . . e 4 d d e 2 2 2 2 f e f . . 
                            . . . e d d e 2 2 2 2 f 4 e . . 
                            . . . . e e f 5 5 4 4 f . . . . 
                            . . . . . f f f f f f f . . . . 
                            . . . . . . . . . f f f . . . .
                """)],
            [img("""
                    . . . . . . f f f f f f . . . . 
                            . . . . f f e e e e f 2 f . . . 
                            . . . f f e e e e f 2 2 2 f . . 
                            . . . f e e e f f e e e e f . . 
                            . . . f f f f e e 2 2 2 2 e f . 
                            . . . f e 2 2 2 f f f f e 2 f . 
                            . . f f f f f f f e e e f f f . 
                            . . f f e 4 4 e b f 4 4 e e f . 
                            . . f e e 4 d 4 1 f d d e f . . 
                            . . . f e e e 4 d d d d f . . . 
                            . . . . f f e e 4 4 4 e f . . . 
                            . . . . . 4 d d e 2 2 2 f . . . 
                            . . . . . e d d e 2 2 2 f . . . 
                            . . . . . f e e f 4 5 5 f . . . 
                            . . . . . . f f f f f f . . . . 
                            . . . . . . . f f f . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                            . . . . . . f f f f f f . . . . 
                            . . . . f f e e e e f 2 f . . . 
                            . . . f f e e e e f 2 2 2 f . . 
                            . . . f e e e f f e e e e f . . 
                            . . . f f f f e e 2 2 2 2 e f . 
                            . . . f e 2 2 2 f f f f e 2 f . 
                            . . f f f f f f f e e e f f f . 
                            . . f f e 4 4 e b f 4 4 e e f . 
                            . . f e e 4 d 4 1 f d d e f . . 
                            . . . f e e e e e d d d f . . . 
                            . . . . . f 4 d d e 4 e f . . . 
                            . . . . . f e d d e 2 2 f . . . 
                            . . . . f f f e e f 5 5 f f . . 
                            . . . . f f f f f f f f f f . . 
                            . . . . . f f . . . f f f . . .
                """),
                img("""
                    . . . . . . f f f f f f . . . . 
                            . . . . f f e e e e f 2 f . . . 
                            . . . f f e e e e f 2 2 2 f . . 
                            . . . f e e e f f e e e e f . . 
                            . . . f f f f e e 2 2 2 2 e f . 
                            . . . f e 2 2 2 f f f f e 2 f . 
                            . . f f f f f f f e e e f f f . 
                            . . f f e 4 4 e b f 4 4 e e f . 
                            . . f e e 4 d 4 1 f d d e f . . 
                            . . . f e e e 4 d d d d f . . . 
                            . . . . f f e e 4 4 4 e f . . . 
                            . . . . . 4 d d e 2 2 2 f . . . 
                            . . . . . e d d e 2 2 2 f . . . 
                            . . . . . f e e f 4 5 5 f . . . 
                            . . . . . . f f f f f f . . . . 
                            . . . . . . . f f f . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                            . . . . . . f f f f f f . . . . 
                            . . . . f f e e e e f 2 f . . . 
                            . . . f f e e e e f 2 2 2 f . . 
                            . . . f e e e f f e e e e f . . 
                            . . . f f f f e e 2 2 2 2 e f . 
                            . . . f e 2 2 2 f f f f e 2 f . 
                            . . f f f f f f f e e e f f f . 
                            . . f f e 4 4 e b f 4 4 e e f . 
                            . . f e e 4 d 4 1 f d d e f . . 
                            . . . f e e e 4 d d d d f . . . 
                            . . . . 4 d d e 4 4 4 e f . . . 
                            . . . . e d d e 2 2 2 2 f . . . 
                            . . . . f e e f 4 4 5 5 f f . . 
                            . . . . f f f f f f f f f f . . 
                            . . . . . f f . . . f f f . . .
                """)],
            [img("""
                    . . . . . . f f f f . . . . . . 
                            . . . . f f e e e e f f . . . . 
                            . . . f e e e f f e e e f . . . 
                            . . f f f f f 2 2 f f f f f . . 
                            . . f f e 2 e 2 2 e 2 e f f . . 
                            . . f e 2 f 2 f f 2 f 2 e f . . 
                            . . f f f 2 2 e e 2 2 f f f . . 
                            . f f e f 2 f e e f 2 f e f f . 
                            . f e e f f e e e e f e e e f . 
                            . . f e e e e e e e e e e f . . 
                            . . . f e e e e e e e e f . . . 
                            . . e 4 f f f f f f f f 4 e . . 
                            . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                            . . 4 4 f 4 4 4 4 4 4 f 4 4 . . 
                            . . . . . f f f f f f . . . . . 
                            . . . . . f f . . f f . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                            . . . . . . f f f f . . . . . . 
                            . . . . f f e e e e f f . . . . 
                            . . . f e e e f f e e e f . . . 
                            . . . f f f f 2 2 f f f f . . . 
                            . . f f e 2 e 2 2 e 2 e f f . . 
                            . . f e 2 f 2 f f f 2 f e f . . 
                            . . f f f 2 f e e 2 2 f f f . . 
                            . . f e 2 f f e e 2 f e e f . . 
                            . f f e f f e e e f e e e f f . 
                            . f f e e e e e e e e e e f f . 
                            . . . f e e e e e e e e f . . . 
                            . . . e f f f f f f f f 4 e . . 
                            . . . 4 f 2 2 2 2 2 e d d 4 . . 
                            . . . e f f f f f f e e 4 . . . 
                            . . . . f f f . . . . . . . . .
                """),
                img("""
                    . . . . . . f f f f . . . . . . 
                            . . . . f f e e e e f f . . . . 
                            . . . f e e e f f e e e f . . . 
                            . . f f f f f 2 2 f f f f f . . 
                            . . f f e 2 e 2 2 e 2 e f f . . 
                            . . f e 2 f 2 f f 2 f 2 e f . . 
                            . . f f f 2 2 e e 2 2 f f f . . 
                            . f f e f 2 f e e f 2 f e f f . 
                            . f e e f f e e e e f e e e f . 
                            . . f e e e e e e e e e e f . . 
                            . . . f e e e e e e e e f . . . 
                            . . e 4 f f f f f f f f 4 e . . 
                            . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                            . . 4 4 f 4 4 4 4 4 4 f 4 4 . . 
                            . . . . . f f f f f f . . . . . 
                            . . . . . f f . . f f . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                            . . . . . . f f f f . . . . . . 
                            . . . . f f e e e e f f . . . . 
                            . . . f e e e f f e e e f . . . 
                            . . . f f f f 2 2 f f f f . . . 
                            . . f f e 2 e 2 2 e 2 e f f . . 
                            . . f e f 2 f f f 2 f 2 e f . . 
                            . . f f f 2 2 e e f 2 f f f . . 
                            . . f e e f 2 e e f f 2 e f . . 
                            . f f e e e f e e e f f e f f . 
                            . f f e e e e e e e e e e f f . 
                            . . . f e e e e e e e e f . . . 
                            . . e 4 f f f f f f f f e . . . 
                            . . 4 d d e 2 2 2 2 2 f 4 . . . 
                            . . . 4 e e f f f f f f e . . . 
                            . . . . . . . . . f f f . . . .
                """)]),
        Render.create_animations(150,
            [img("""
                    . . . f 4 4 f f f f . . . . . . 
                            . . f 4 5 5 4 5 f b f f . . . . 
                            . . f 5 5 5 5 4 e 3 3 b f . . . 
                            . . f e 4 4 4 e 3 3 3 3 b f . . 
                            . . f 3 3 3 3 3 3 3 3 3 3 f . . 
                            . f 3 3 e e 3 b e 3 3 3 3 f . . 
                            . f 3 3 e e e f f 3 3 3 3 f . . 
                            . f 3 e e e f b f b b b b f . . 
                            . . f e 4 4 f 1 e b b b b f . . 
                            . . . f 4 4 4 4 f b b b b f f . 
                            . . . f e e e f f f b b b b f . 
                            . . . f d d d e 4 4 f b b f . . 
                            . . . f d d d e 4 4 e f f . . . 
                            . . f b d b d b e e b f . . . . 
                            . . f f 1 d 1 d 1 d f f . . . . 
                            . . . . f f b b f f . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                            . . . f 4 4 f f f f . . . . . . 
                            . . f 4 5 5 4 5 f b f f . . . . 
                            . . f 5 5 5 5 4 e 3 3 b f . . . 
                            . . f e 4 4 4 e 3 3 3 3 b f . . 
                            . f 3 3 3 3 3 3 3 3 3 3 3 f . . 
                            . f 3 3 e e 3 b e 3 3 3 3 f . . 
                            . f 3 3 e e e f f 3 3 3 3 f . . 
                            . . f e e e f b f b b b b f f . 
                            . . . e 4 4 f 1 e b b b b b f . 
                            . . . f 4 4 4 4 f b b b b b f . 
                            . . . f d d d e 4 4 b b b f . . 
                            . . . f d d d e 4 4 f f f . . . 
                            . . f d d d b b e e b b f . . . 
                            . . f b d 1 d 1 d d b f . . . . 
                            . . . f f f b b f f f . . . . .
                """)],
            [img("""
                    . . . . . f f 4 4 f f . . . . . 
                            . . . . f 5 4 5 5 4 5 f . . . . 
                            . . . f e 4 5 5 5 5 4 e f . . . 
                            . . f b 3 e 4 4 4 4 e 3 b f . . 
                            . . f 3 3 3 3 3 3 3 3 3 3 f . . 
                            . f 3 3 e b 3 e e 3 b e 3 3 f . 
                            . f 3 3 f f e e e e f f 3 3 f . 
                            . f b b f b f e e f b f b b f . 
                            . f b b e 1 f 4 4 f 1 e b b f . 
                            f f b b f 4 4 4 4 4 4 f b b f f 
                            f b b f f f e e e e f f f b b f 
                            . f e e f b d d d d b f e e f . 
                            . . e 4 c d d d d d d c 4 e . . 
                            . . e f b d b d b d b b f e . . 
                            . . . f f 1 d 1 d 1 d f f . . . 
                            . . . . . f f b b f f . . . . .
                """),
                img("""
                    . . . . . . . f f . . . . . . . 
                            . . . . . f f 4 4 f f . . . . . 
                            . . . . f 5 4 5 5 4 5 f . . . . 
                            . . . f e 4 5 5 5 5 4 e f . . . 
                            . . f b 3 e 4 4 4 4 e 3 b f . . 
                            . f e 3 3 3 3 3 3 3 3 3 3 e f . 
                            . f 3 3 e b 3 e e 3 b e 3 3 f . 
                            . f b 3 f f e e e e f f 3 b f . 
                            f f b b f b f e e f b f b b f f 
                            f b b b e 1 f 4 4 f 1 e b b b f 
                            . f b b e e 4 4 4 4 4 f b b f . 
                            . . f 4 4 4 e d d d b f e f . . 
                            . . f e 4 4 e d d d d c 4 e . . 
                            . . . f e e d d b d b b f e . . 
                            . . . f f 1 d 1 d 1 1 f f . . . 
                            . . . . . f f f b b f . . . . .
                """),
                img("""
                    . . . . . f f 4 4 f f . . . . . 
                            . . . . f 5 4 5 5 4 5 f . . . . 
                            . . . f e 4 5 5 5 5 4 e f . . . 
                            . . f b 3 e 4 4 4 4 e 3 b f . . 
                            . . f 3 3 3 3 3 3 3 3 3 3 f . . 
                            . f 3 3 e b 3 e e 3 b e 3 3 f . 
                            . f 3 3 f f e e e e f f 3 3 f . 
                            . f b b f b f e e f b f b b f . 
                            . f b b e 1 f 4 4 f 1 e b b f . 
                            f f b b f 4 4 4 4 4 4 f b b f f 
                            f b b f f f e e e e f f f b b f 
                            . f e e f b d d d d b f e e f . 
                            . . e 4 c d d d d d d c 4 e . . 
                            . . e f b d b d b d b b f e . . 
                            . . . f f 1 d 1 d 1 d f f . . . 
                            . . . . . f f b b f f . . . . .
                """),
                img("""
                    . . . . . . . f f . . . . . . . 
                            . . . . . f f 4 4 f f . . . . . 
                            . . . . f 5 4 5 5 4 5 f . . . . 
                            . . . f e 4 5 5 5 5 4 e f . . . 
                            . . f b 3 e 4 4 4 4 e 3 b f . . 
                            . f e 3 3 3 3 3 3 3 3 3 3 e f . 
                            . f 3 3 e b 3 e e 3 b e 3 3 f . 
                            . f b 3 f f e e e e f f 3 b f . 
                            f f b b f b f e e f b f b b f f 
                            f b b b e 1 f 4 4 f 1 e b b b f 
                            . f b b f 4 4 4 4 4 e e b b f . 
                            . . f e f b d d d e 4 4 4 f . . 
                            . . e 4 c d d d d e 4 4 e f . . 
                            . . e f b b d b d d e e f . . . 
                            . . . f f 1 1 d 1 d 1 f f . . . 
                            . . . . . f b b f f f . . . . .
                """)],
            [img("""
                    . . . . . . f f f f 4 4 f . . . 
                            . . . . f f b f 5 4 5 5 4 f . . 
                            . . . f b 3 3 e 4 5 5 5 5 f . . 
                            . . f b 3 3 3 3 e 4 4 4 e f . . 
                            . . f 3 3 3 3 3 3 3 3 3 3 f . . 
                            . . f 3 3 3 3 e b 3 e e 3 3 f . 
                            . . f 3 3 3 3 f f e e e 3 3 f . 
                            . . f b b b b f b f e e e 3 f . 
                            . . f b b b b e 1 f 4 4 e f . . 
                            . f f b b b b f 4 4 4 4 f . . . 
                            . f b b b b f f f e e e f . . . 
                            . . f b b f 4 4 e d d d f . . . 
                            . . . f f e 4 4 e d d d f . . . 
                            . . . . f b e e b d b d b f . . 
                            . . . . f f d 1 d 1 d 1 f f . . 
                            . . . . . . f f b b f f . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                            . . . . . . f f f f 4 4 f . . . 
                            . . . . f f b f 5 4 5 5 4 f . . 
                            . . . f b 3 3 e 4 5 5 5 5 f . . 
                            . . f b 3 3 3 3 e 4 4 4 e f . . 
                            . . f 3 3 3 3 3 3 3 3 3 3 3 f . 
                            . . f 3 3 3 3 e b 3 e e 3 3 f . 
                            . . f 3 3 3 3 f f e e e 3 3 f . 
                            . f f b b b b f b f e e e f . . 
                            . f b b b b b e 1 f 4 4 e . . . 
                            . f b b b b b f 4 4 4 4 f . . . 
                            . . f b b b 4 4 e d d d f . . . 
                            . . . f f f 4 4 e d d d f . . . 
                            . . . f b b e e b b d d d f . . 
                            . . . . f b d d 1 d 1 d b f . . 
                            . . . . . f f f b b f f f . . .
                """)],
            [img("""
                    . . . . . f f 4 4 f f . . . . . 
                            . . . . f 5 4 5 5 4 5 f . . . . 
                            . . . f e 3 3 3 3 3 3 e f . . . 
                            . . f b 3 3 3 3 3 3 3 3 b f . . 
                            . . f 3 3 3 3 3 3 3 3 3 3 f . . 
                            . f 3 3 3 3 3 3 3 3 3 3 3 3 f . 
                            . f b 3 3 3 3 3 3 3 3 3 3 b f . 
                            . f b b 3 3 3 3 3 3 3 3 b b f . 
                            . f b b b b b b b b b b b b f . 
                            f c b b b b b b b b b b b b c f 
                            f b b b b b b b b b b b b b b f 
                            . f c c b b b b b b b b c c f . 
                            . . e 4 c f f f f f f c 4 e . . 
                            . . e f b d b d b d b b f e . . 
                            . . . f f 1 d 1 d 1 d f f . . . 
                            . . . . . f f b b f f . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                            . . . . . f f 4 4 f f . . . . . 
                            . . . . f 5 4 5 5 4 5 f . . . . 
                            . . . f e 3 3 3 3 3 3 e f . . . 
                            . . f b 3 3 3 3 3 3 3 3 b f . . 
                            . . f 3 3 3 3 3 3 3 3 3 3 f . . 
                            . f b 3 3 3 3 3 3 3 3 3 3 b f . 
                            . f b b 3 3 3 3 3 3 3 3 b b f . 
                            . f b b b b b b b b b b b b f . 
                            f c b b b b b b b b b b b b f . 
                            f b b b b b b b b b b b b c f . 
                            f f b b b b b b b b b b c f . . 
                            . f c c c f f f f f f f e c . . 
                            . . . f b b d b d d e 4 4 e . . 
                            . . . f f 1 1 d 1 d e e f . . . 
                            . . . . . f b b f f f . . . . .
                """),
                img("""
                    . . . . . f f 4 4 f f . . . . . 
                            . . . . f 5 4 5 5 4 5 f . . . . 
                            . . . f e 3 3 3 3 3 3 e f . . . 
                            . . f b 3 3 3 3 3 3 3 3 b f . . 
                            . . f 3 3 3 3 3 3 3 3 3 3 f . . 
                            . f 3 3 3 3 3 3 3 3 3 3 3 3 f . 
                            . f b 3 3 3 3 3 3 3 3 3 3 b f . 
                            . f b b 3 3 3 3 3 3 3 3 b b f . 
                            . f b b b b b b b b b b b b f . 
                            f c b b b b b b b b b b b b c f 
                            f b b b b b b b b b b b b b b f 
                            . f c c b b b b b b b b c c f . 
                            . . e 4 c f f f f f f c 4 e . . 
                            . . e f b d b d b d b b f e . . 
                            . . . f f 1 d 1 d 1 d f f . . . 
                            . . . . . f f b b f f . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                            . . . . . f f 4 4 f f . . . . . 
                            . . . . f 5 4 5 5 4 5 f . . . . 
                            . . . f e 3 3 3 3 3 3 e f . . . 
                            . . f b 3 3 3 3 3 3 3 3 b f . . 
                            . . f 3 3 3 3 3 3 3 3 3 3 f . . 
                            . f b 3 3 3 3 3 3 3 3 3 3 b f . 
                            . f b b 3 3 3 3 3 3 3 3 b b f . 
                            . f b b b b b b b b b b b b f . 
                            . f b b b b b b b b b b b b c f 
                            . f c b b b b b b b b b b b b f 
                            . . f c b b b b b b b b b b f f 
                            . . c e f f f f f f f c c c f . 
                            . . e 4 4 e d d b d b b f . . . 
                            . . . f e e d 1 d 1 1 f f . . . 
                            . . . . . f f f b b f . . . . .
                """)]),
        Render.create_animations(150,
            [img("""
                    . . 4 4 4 . . . . 4 4 4 . . . . 
                            . 4 5 5 5 e . . e 5 5 5 4 . . . 
                            4 5 5 5 5 5 e e 5 5 5 5 5 4 . . 
                            4 5 5 4 4 5 5 5 5 4 4 5 5 4 . . 
                            e 5 4 4 5 5 5 5 5 5 4 4 5 e . . 
                            . e e 5 5 5 5 5 5 5 5 e e . . . 
                            . . e 5 f 5 5 5 5 f 5 e . . . . 
                            . . f 5 5 5 4 4 5 5 5 f . . f f 
                            . . f 4 5 5 f f 5 5 6 f . f 5 f 
                            . . . f 6 6 6 6 6 6 4 4 f 5 5 f 
                            . . . f 4 5 5 5 5 5 5 4 4 5 f . 
                            . . . f 5 5 5 5 5 4 5 5 f f . . 
                            . . . f 5 f f f 5 f f 5 f . . . 
                            . . . f f . . f f . . f f . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                            . . 4 4 4 . . . . 4 4 4 . . . . 
                            . 4 5 5 5 e . . e 5 5 5 4 . . . 
                            4 5 5 5 5 5 e e 5 5 5 5 5 4 . . 
                            4 5 5 4 4 5 5 5 5 4 4 5 5 4 . . 
                            e 5 4 4 5 5 5 5 5 5 4 4 5 e . . 
                            . e e 5 5 5 5 5 5 5 5 e e . . . 
                            . . e 5 f 5 5 5 5 f 5 e . . . . 
                            . . f 5 5 5 4 4 5 5 5 f . f f . 
                            . . . 4 5 5 f f 5 5 6 f f 5 f . 
                            . . . f 6 6 6 6 6 6 4 4 4 5 f . 
                            . . . f 5 5 5 5 5 5 5 f f f . . 
                            . . . f 5 4 5 f f f 5 f . . . . 
                            . . . f f f f f . . f f . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                            . . 4 4 4 . . . . 4 4 4 . . . . 
                            . 4 5 5 5 e . . e 5 5 5 4 . . . 
                            4 5 5 5 5 5 e e 5 5 5 5 5 4 . . 
                            4 5 5 4 4 5 5 5 5 4 4 5 5 4 . . 
                            e 5 4 4 5 5 5 5 5 5 4 4 5 e . . 
                            . e e 5 5 5 5 5 5 5 5 e e . . . 
                            . . e 5 f 5 5 5 5 f 5 e . . . . 
                            . . f 5 5 5 4 4 5 5 5 f . f f . 
                            . . . 4 5 5 f f 5 5 6 f f 5 f . 
                            . . . f 6 6 6 6 6 6 4 f 5 5 f . 
                            . . . f 5 5 5 5 5 5 5 4 5 f . . 
                            . . . . f 5 4 5 f 5 f f f . . . 
                            . . . . . f f f f f f f . . . .
                """)],
            [img("""
                    . . . . 4 4 4 . . . . 4 4 4 . . 
                            . . . 4 5 5 5 e . . e 5 5 5 4 . 
                            . . 4 5 5 5 5 5 e e 5 5 5 5 5 4 
                            . . 4 5 5 4 4 5 5 5 5 4 4 5 5 4 
                            . . e 5 4 4 5 5 5 5 5 5 4 4 5 e 
                            . . . e e 5 5 5 5 5 5 5 5 e e . 
                            . . . . e 5 f 5 5 5 5 f 5 e . . 
                            f f . . f 5 5 5 4 4 5 5 5 f . . 
                            f 5 f . f 6 5 5 f f 5 5 4 f . . 
                            f 5 5 f 4 4 6 6 6 6 6 6 f . . . 
                            . f 5 4 4 5 5 5 5 5 5 4 f . . . 
                            . . f f 5 5 4 5 5 5 5 5 f . . . 
                            . . . f 5 f f 5 f f f 5 f . . . 
                            . . . f f . . f f . . f f . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                            . . . . 4 4 4 . . . . 4 4 4 . . 
                            . . . 4 5 5 5 e . . e 5 5 5 4 . 
                            . . 4 5 5 5 5 5 e e 5 5 5 5 5 4 
                            . . 4 5 5 4 4 5 5 5 5 4 4 5 5 4 
                            . . e 5 4 4 5 5 5 5 5 5 4 4 5 e 
                            . . . e e 5 5 5 5 5 5 5 5 e e . 
                            . . . . e 5 f 5 5 5 5 f 5 e . . 
                            . f f . f 5 5 5 4 4 5 5 5 f . . 
                            . f 5 f f 6 5 5 f f 5 5 4 . . . 
                            . f 5 4 4 4 6 6 6 6 6 6 f . . . 
                            . . f f f 5 5 5 5 5 5 5 f . . . 
                            . . . . f 5 f f f 5 4 5 f . . . 
                            . . . . f f . . f f f f f . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                            . . . . 4 4 4 . . . . 4 4 4 . . 
                            . . . 4 5 5 5 e . . e 5 5 5 4 . 
                            . . 4 5 5 5 5 5 e e 5 5 5 5 5 4 
                            . . 4 5 5 4 4 5 5 5 5 4 4 5 5 4 
                            . . e 5 4 4 5 5 5 5 5 5 4 4 5 e 
                            . . . e e 5 5 5 5 5 5 5 5 e e . 
                            . . . . e 5 f 5 5 5 5 f 5 e . . 
                            . f f . f 5 5 5 4 4 5 5 5 f . . 
                            . f 5 f f 6 5 5 f f 5 5 4 . . . 
                            . f 5 5 f 4 6 6 6 6 6 6 f . . . 
                            . . f 5 4 5 5 5 5 5 5 5 f . . . 
                            . . . f f f 5 f 5 4 5 f . . . . 
                            . . . . f f f f f f f . . . . .
                """)]),
        Render.create_animations(150,
            [img("""
                    . . . . . . . . . . . . . . . . 
                            . . . . . . . . c c c c . . . . 
                            . . . . . . c c d d d d c . . . 
                            . . . . . c c c c c c d c . . . 
                            . . . . c c 4 4 4 4 d c c . . . 
                            . . . c 4 d 4 4 4 4 4 1 c . c c 
                            . . c 4 4 4 1 4 4 4 4 d 1 c 4 c 
                            . c 4 4 4 4 1 4 4 4 4 4 1 c 4 c 
                            f 4 4 4 4 4 1 4 4 4 4 4 1 4 4 f 
                            f 4 4 4 f 4 1 c c 4 4 4 1 f 4 f 
                            f 4 4 4 4 4 1 4 4 f 4 4 d f 4 f 
                            . f 4 4 4 4 1 c 4 f 4 d f f f f 
                            . . f f 4 d 4 4 f f 4 c f c . . 
                            . . . . f f 4 4 4 4 c d b c . . 
                            . . . . . . f f f f d d d c . . 
                            . . . . . . . . . . c c c . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                            . . . . . . . c c c c c . . . . 
                            . . . . . . c d d d d d c . . . 
                            . . . . . . c c c c c d c . . . 
                            . . . . . c 4 4 4 4 d c c . . . 
                            . . . . c d 4 4 4 4 4 1 c . . . 
                            . . . c 4 4 1 4 4 4 4 4 1 c . . 
                            . . c 4 4 4 4 1 4 4 4 4 1 c c c 
                            . c 4 4 4 4 4 1 c c 4 4 1 4 4 c 
                            . c 4 4 4 4 4 1 4 4 f 4 1 f 4 f 
                            f 4 4 4 4 f 4 1 c 4 f 4 d f 4 f 
                            f 4 4 4 4 4 4 1 4 f f 4 f f 4 f 
                            . f 4 4 4 4 1 4 4 4 4 c b c f f 
                            . . f f f d 4 4 4 4 c d d c . . 
                            . . . . . f f f f f c c c . . . 
                            . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . c c c c . . . . 
                            . . . . . . c c d d d d c . . . 
                            . . . . . c c c c c c d c . . . 
                            . . . . c c 4 4 4 4 d c c . c c 
                            . . . c 4 d 4 4 4 4 4 1 c c 4 c 
                            . . c 4 4 4 1 4 4 4 4 d 1 c 4 f 
                            . c 4 4 4 4 1 4 4 4 4 4 1 4 4 f 
                            f 4 4 4 4 4 1 1 c f 4 4 1 f 4 f 
                            f 4 4 4 f 4 1 c 4 f 4 4 1 f 4 f 
                            f 4 4 4 4 4 1 4 4 f 4 4 d f f f 
                            . f 4 4 4 4 1 c c 4 4 d f f . . 
                            . . f f 4 d 4 4 4 4 4 c f . . . 
                            . . . . f f 4 4 4 4 c d b c . . 
                            . . . . . . f f f f d d d c . . 
                            . . . . . . . . . . c c c . . . 
                            . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                            . . . . . . . . . c c c c . . . 
                            . . . . . . . c c d d d d c . . 
                            . . . . . c c c c c c d d c . . 
                            . . . c c c 4 4 4 4 d c c c c c 
                            . . c 4 4 1 4 4 4 4 4 1 c c 4 f 
                            . c 4 4 4 4 1 4 4 4 4 d 1 f 4 f 
                            f 4 4 4 4 4 1 4 4 4 4 4 1 f 4 f 
                            f 4 4 f 4 4 1 4 c f 4 4 1 4 4 f 
                            f 4 4 4 4 4 1 c 4 f 4 4 1 f f f 
                            . f 4 4 4 4 1 4 4 f 4 4 d f . . 
                            . . f 4 4 1 4 c c 4 4 d f . . . 
                            . . . f d 4 4 4 4 4 4 c f . . . 
                            . . . . f f 4 4 4 4 c d b c . . 
                            . . . . . . f f f f d d d c . . 
                            . . . . . . . . . . c c c . . .
                """)],
            [img("""
                    . . . . . . . . . . . . . . . . 
                            . . . . c c c c . . . . . . . . 
                            . . . c d d d d c c . . . . . . 
                            . . . c d c c c c c c . . . . . 
                            . . . c c d 4 4 4 4 c c . . . . 
                            c c . c 1 4 4 4 4 4 d 4 c . . . 
                            c 4 c 1 d 4 4 4 4 1 4 4 4 c . . 
                            c 4 c 1 4 4 4 4 4 1 4 4 4 4 c . 
                            f 4 4 1 4 4 4 4 4 1 4 4 4 4 4 f 
                            f 4 f 1 4 4 4 c c 1 4 f 4 4 4 f 
                            f 4 f d 4 4 f 4 4 1 4 4 4 4 4 f 
                            f f f f d 4 f 4 c 1 4 4 4 4 f . 
                            . . c f c 4 f f 4 4 d 4 f f . . 
                            . . c b d c 4 4 4 4 f f . . . . 
                            . . c d d d f f f f . . . . . . 
                            . . . c c c . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                            . . . . c c c c c . . . . . . . 
                            . . . c d d d d d c . . . . . . 
                            . . . c d c c c c c . . . . . . 
                            . . . c c d 4 4 4 4 c . . . . . 
                            . . . c 1 4 4 4 4 4 d c . . . . 
                            . . c 1 4 4 4 4 4 1 4 4 c . . . 
                            c c c 1 4 4 4 4 1 4 4 4 4 c . . 
                            c 4 4 1 4 4 c c 1 4 4 4 4 4 c . 
                            f 4 f 1 4 f 4 4 1 4 4 4 4 4 c . 
                            f 4 f d 4 f 4 c 1 4 f 4 4 4 4 f 
                            f 4 f f 4 f f 4 1 4 4 4 4 4 4 f 
                            f f c b c 4 4 4 4 1 4 4 4 4 f . 
                            . . c d d c 4 4 4 4 d f f f . . 
                            . . . c c c f f f f f . . . . . 
                            . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . c c c c . . . . . . . . 
                            . . . c d d d d c c . . . . . . 
                            . . . c d c c c c c c . . . . . 
                            c c . c c d 4 4 4 4 c c . . . . 
                            c 4 c c 1 4 4 4 4 4 d 4 c . . . 
                            f 4 c 1 d 4 4 4 4 1 4 4 4 c . . 
                            f 4 4 1 4 4 4 4 4 1 4 4 4 4 c . 
                            f 4 f 1 4 4 f c 1 1 4 4 4 4 4 f 
                            f 4 f 1 4 4 f 4 c 1 4 f 4 4 4 f 
                            f f f d 4 4 f 4 4 1 4 4 4 4 4 f 
                            . . f f d 4 4 c c 1 4 4 4 4 f . 
                            . . . f c 4 4 4 4 4 d 4 f f . . 
                            . . c b d c 4 4 4 4 f f . . . . 
                            . . c d d d f f f f . . . . . . 
                            . . . c c c . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                            . . . c c c c . . . . . . . . . 
                            . . c d d d d c c . . . . . . . 
                            . . c d d c c c c c c . . . . . 
                            c c c c c d 4 4 4 4 c c c . . . 
                            f 4 c c 1 4 4 4 4 4 1 4 4 c . . 
                            f 4 f 1 d 4 4 4 4 1 4 4 4 4 c . 
                            f 4 f 1 4 4 4 4 4 1 4 4 4 4 4 f 
                            f 4 4 1 4 4 f c 4 1 4 4 f 4 4 f 
                            f f f 1 4 4 f 4 c 1 4 4 4 4 4 f 
                            . . f d 4 4 f 4 4 1 4 4 4 4 f . 
                            . . . f d 4 4 c c 4 1 4 4 f . . 
                            . . . f c 4 4 4 4 4 4 d f . . . 
                            . . c b d c 4 4 4 4 f f . . . . 
                            . . c d d d f f f f . . . . . . 
                            . . . c c c . . . . . . . . . .
                """)])]
    listImg = [img("""
            . . . . . . f f f f . . . . . . 
                    . . . . f f f 2 2 f f f . . . . 
                    . . . f f f 2 2 2 2 f f f . . . 
                    . . f f f e e e e e e f f f . . 
                    . . f f e 2 2 2 2 2 2 e e f . . 
                    . . f e 2 f f f f f f 2 e f . . 
                    . . f f f f e e e e f f f f . . 
                    . f f e f b f 4 4 f b f e f f . 
                    . f e e 4 1 f d d f 1 4 e e f . 
                    . . f e e d d d d d d e e f . . 
                    . . . f e e 4 4 4 4 e e f . . . 
                    . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                    . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                    . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                    . . . . . f f f f f f . . . . . 
                    . . . . . f f . . f f . . . . .
        """),
        img("""
            . . . . . f f 4 4 f f . . . . . 
                    . . . . f 5 4 5 5 4 5 f . . . . 
                    . . . f e 4 5 5 5 5 4 e f . . . 
                    . . f b 3 e 4 4 4 4 e 3 b f . . 
                    . . f 3 3 3 3 3 3 3 3 3 3 f . . 
                    . f 3 3 e b 3 e e 3 b e 3 3 f . 
                    . f 3 3 f f e e e e f f 3 3 f . 
                    . f b b f b f e e f b f b b f . 
                    . f b b e 1 f 4 4 f 1 e b b f . 
                    f f b b f 4 4 4 4 4 4 f b b f f 
                    f b b f f f e e e e f f f b b f 
                    . f e e f b d d d d b f e e f . 
                    . . e 4 c d d d d d d c 4 e . . 
                    . . e f b d b d b d b b f e . . 
                    . . . f f 1 d 1 d 1 d f f . . . 
                    . . . . . f f b b f f . . . . .
        """),
        img("""
            . . 4 4 4 . . . . 4 4 4 . . . . 
                    . 4 5 5 5 e . . e 5 5 5 4 . . . 
                    4 5 5 5 5 5 e e 5 5 5 5 5 4 . . 
                    4 5 5 4 4 5 5 5 5 4 4 5 5 4 . . 
                    e 5 4 4 5 5 5 5 5 5 4 4 5 e . . 
                    . e e 5 5 5 5 5 5 5 5 e e . . . 
                    . . e 5 f 5 5 5 5 f 5 e . . . . 
                    . . f 5 5 5 4 4 5 5 5 f . . f f 
                    . . f 4 5 5 f f 5 5 6 f . f 5 f 
                    . . . f 6 6 6 6 6 6 4 4 f 5 5 f 
                    . . . f 4 5 5 5 5 5 5 4 4 5 f . 
                    . . . f 5 5 5 5 5 4 5 5 f f . . 
                    . . . f 5 f f f 5 f f 5 f . . . 
                    . . . f f . . f f . . f f . . .
        """),
        img("""
            . . . . . . . . c c c c . . . . 
                    . . . . . . c c d d d d c . . . 
                    . . . . . c c c c c c d c . . . 
                    . . . . c c 4 4 4 4 d c c . c c 
                    . . . c 4 d 4 4 4 4 4 1 c c 4 c 
                    . . c 4 4 4 1 4 4 4 4 d 1 c 4 f 
                    . c 4 4 4 4 1 4 4 4 4 4 1 4 4 f 
                    f 4 4 4 4 4 1 1 c f 4 4 1 f 4 f 
                    f 4 4 4 f 4 1 c 4 f 4 4 1 f 4 f 
                    f 4 4 4 4 4 1 4 4 f 4 4 d f f f 
                    . f 4 4 4 4 1 c c 4 4 d f f . . 
                    . . f f 4 d 4 4 4 4 4 c f . . . 
                    . . . . f f 4 4 4 4 c d b c . . 
                    . . . . . . f f f f d d d c . . 
                    . . . . . . . . . . c c c . . . 
                    . . . . . . . . . . . . . . . .
        """)]
    index = randint(0, len(listImg) - 1)
    mySprite = sprites.create(listImg[index], SpriteKind.enemy)
    Render.takeover_scene_sprites()
    mySprite.scale = 0.5
    mySprite.set_bounce_on_wall(True)
    mySprite.set_velocity(18, 24)
    tiles.place_on_random_tile(mySprite, assets.tile("""
        transparency16
    """))
    Render.set_sprite_animations(mySprite, listAni[index])
index = 0
listImg: List[Image] = []
listAni: List[Render.Animations] = []
projectile: Sprite = None
mySprite: Sprite = None
game.stats = True
tiles.set_current_tilemap(tilemap("""
    level1
"""))
scene.set_background_image(img("""
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999bbbbbbbbb99999999
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
"""))
Render.get_render_sprite_instance().set_position(114, 115)
for index2 in range(8):
    spawnCoin()
for index22 in range(8):
    spawnEnemy()