import arcade

class imp(arcade.Window):
    def __init__(self):
        super().__init__(1024, 512, "acc")
    def on_draw(self):
        a=arcade.load_texture("groupGray.jpg")
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,1024,512,a)
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        print(x, y)


i = imp()
arcade.run()