from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition, SlideTransition
from kivy.uix.widget import Widget
from kivy.core.window import Window


class GraphicsView(ScreenManager):
    def __init__(self, scene: any = ...):
        super(GraphicsView, self).__init__(transition=FadeTransition())
        # if scene:
        #     self.add_widget(scene)
    def setScene(self, scene):
        self.setCurrentScene(scene)
    def setCurrentScene(self, scene):
        self.current = scene.name
    def add_scene(self, scene):
        self.add_widget(scene)

class GraphicsScene(Screen):
    def __init__(self, name, background_color):
        super(GraphicsScene, self).__init__(name=name)
        if background_color == 'white':
            Window.clearcolor = (1, 1, 1, 1)
        elif background_color == 'red':
            Window.clearcolor = (1, 0, 0, 1)
        elif background_color == 'blue':
            Window.clearcolor = (0, 0, 1, 1)
        elif background_color == 'green':
            Window.clearcolor = (0, 1, 0, 1)
        elif background_color == 'black':
            Window.clearcolor = (0, 0, 0, 1)
        else:
            Window.clearcolor = background_color
#
# class AppBox(BoxLayout):
#     def __init__(self):
#         super(AppBox, self).__init__()
#         scene = GraphicsScene('GameOverScreen')
#         view = GraphicsView(scene)
#         self.add_widget(view)


class MainApp(App):
    def build(self):
        super(MainApp, self).__init__()
        self.view = GraphicsView()
        self.layout = BoxLayout()
        self.layout.add_widget(self.view)

        for i in range(20):
            scene = GraphicsScene('Title %d' % i, 'black')
            scene.size = self.view.size

            # self.button = Button(text='Change Screen', on_press=self.change_screen)
            # scene.add_widget(self.button)
            self.label = Label(text=scene.name, color=(1, 0, 0, 1))
            scene.add_widget(self.label)


            self.view.add_scene(scene)


        self.view.current = 'Title 2'
        return self.layout
    def change_screen(self, button):
        self.view.current = 'Title 6'



MainApp().run()