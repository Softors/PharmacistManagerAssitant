from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.tabbedpanel import TabbedPanelItem

from pma.views.tab_content import TabContent


class UsagesTabContent(TabContent):
    def __init__(self, **kwargs):
        super(UsagesTabContent, self).__init__(**kwargs)
        self.add_widget(Button(text='Usages Header', size_hint=(0.2, 0.1)))  # placeholder
        self.add_widget(Button(text='Usages Content', size_hint=(0.2, 0.1)))  # placeholder
        self.add_widget(FloatLayout())  # placeholder


class UsagesTabItem(TabbedPanelItem):
    def __init__(self, **kwargs):
        super(UsagesTabItem, self).__init__(**kwargs)
        self.text = 'Usages'
        self.add_widget(UsagesTabContent())
