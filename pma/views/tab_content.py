from kivy.uix.boxlayout import BoxLayout


class TabContent(BoxLayout):
    def __init__(self, **kwargs):
        super(TabContent, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 25
        self.spacing = 25
