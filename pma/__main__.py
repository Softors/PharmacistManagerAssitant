from kivy.app import App

from pma.views.main_container import MainContainer


class PharmacistManagerAssistantApp(App):
    def build(self):
        return MainContainer()


if __name__ == '__main__':
    PharmacistManagerAssistantApp().run()
