def on_button_pressed_a():
    music._play_default_background(music.built_in_playable_melody(Melodies.NYAN),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
    # sb
    basic.show_leds("""
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    # fuck microbit
    basic.show_leds("""
        # . . . .
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    # fuck ...
    basic.show_leds("""
        # . . . .
        # . . . .
        # . . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        # . . . .
        # . . . .
        # . . . .
        # . . . .
        . . . . .
        """)
    basic.show_leds("""
        # . . . .
        # . . . .
        # . . . .
        # . . . .
        # . . . .
        """)
    basic.show_leds("""
        # # . . .
        # . . . .
        # . . . .
        # . . . .
        # . . . .
        """)
    basic.show_leds("""
        # # . . .
        # # . . .
        # . . . .
        # . . . .
        # . . . .
        """)
    basic.show_leds("""
        # # . . .
        # # . . .
        # # . . .
        # . . . .
        # . . . .
        """)
    basic.show_leds("""
        # # . . .
        # # . . .
        # # . . .
        # # . . .
        # . . . .
        """)
    basic.show_leds("""
        # # . . .
        # # . . .
        # # . . .
        # # . . .
        # # . . .
        """)
    basic.show_leds("""
        # # # . .
        # # . . .
        # # . . .
        # # . . .
        # # . . .
        """)
    basic.show_leds("""
        # # # . .
        # # # . .
        # # . . .
        # # . . .
        # # . . .
        """)
    basic.show_leds("""
        # # # . .
        # # # . .
        # # . . .
        # # . . .
        # # . . .
        """)
    basic.show_leds("""
        # # # . .
        # # # . .
        # # # . .
        # # . . .
        # # . . .
        """)
    basic.show_leds("""
        # # # . .
        # # # . .
        # # # . .
        # # # . .
        # # . . .
        """)
    basic.show_leds("""
        # # # . .
        # # # . .
        # # # . .
        # # # . .
        # # # . .
        """)
    basic.show_leds("""
        # # # # .
        # # # . .
        # # # . .
        # # # . .
        # # # . .
        """)
    basic.show_leds("""
        # # # # .
        # # # # .
        # # # . .
        # # # . .
        # # # . .
        """)
    basic.show_leds("""
        # # # # .
        # # # # .
        # # # # .
        # # # . .
        # # # . .
        """)
    basic.show_leds("""
        # # # # .
        # # # # .
        # # # # .
        # # # # .
        # # # . .
        """)
    basic.show_leds("""
        # # # # .
        # # # # .
        # # # # .
        # # # # .
        # # # # .
        """)
    basic.show_leds("""
        # # # # #
        # # # # .
        # # # # .
        # # # # .
        # # # # .
        """)
    basic.show_leds("""
        # # # # #
        # # # # #
        # # # # .
        # # # # .
        # # # # .
        """)
    basic.show_leds("""
        # # # # #
        # # # # #
        # # # # #
        # # # # .
        # # # # .
        """)
    basic.show_leds("""
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # .
        """)
    basic.show_leds("""
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        """)
    basic.show_leds("""
        # # # # #
        # # # # #
        # # . # #
        # # # # #
        # # # # #
        """)
    basic.show_leds("""
        # # # # #
        # . . . #
        # . . . #
        # . . . #
        # # # # #
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    music.stop_all_sounds()
input.on_button_pressed(Button.A, on_button_pressed_a)
