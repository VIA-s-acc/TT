import flet as ft
import configparser

def settings_page(page: ft.Page):
    with open('config.ini', 'r') as config_file:
        config = configparser.ConfigParser()
        config.read_file(config_file)
    theme = config.get('settings', 'theme', fallback='light')

    def on_change(e):
        theme = e.control.value
        with open('config.ini', 'r+') as config_file:
            config = configparser.ConfigParser()
            config.read_file(config_file)
            config.set('settings', 'theme', theme)
            config.write(config_file)
            
    stack = ft.Stack(
            padding=ft.SpacingSize.LARGE,
            horizontal_align="center",
            vertical_content_alignment="center",
            children=[
                ft.Text(
                    text="Settings",
                    font="bold 32px sans-serif",
                    color=ft.ForeColors.ATTENTION,
                    opacity=1,
                ),
                ft.Stack(
                    padding=ft.SpacingSize.LARGE,
                    horizontal_align="center",
                    vertical_content_alignment="center",
                    children=[
                        ft.Text(
                            text="Theme:",
                            font="bold 16px sans-serif",
                            color=ft.ForeColors.ATTENTION,
                            opacity=1,
                        ),
                        ft.Checkbox(
                            value=theme == 'dark',
                            on_change=on_change,
                        ),
                    ],
                ),
            ],
        ),
    
    page.add(
        stack
    )
    