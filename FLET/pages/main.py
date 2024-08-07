import flet as ft
import time
def main_page(page: ft.Page):
    # Установить заголовок страницы
    page.title = "Sliding Text Animation Example"
    
    sliding_text = ft.Text("Hello, World!", size=40, color=ft.colors.BLUE, weight=ft.FontWeight.BOLD)
    text_width = len("Hello, World!") * (40 * 0.6)
    page.add(sliding_text)
    
    position = -1
    step = 0.01
    
    def animate_text():
        nonlocal position
        nonlocal step
        while True:
            window_width = page.width
            max_offset_x = (window_width//text_width) + 2
            
            while position < max_offset_x:
                position += step
                sliding_text.offset = ft.Offset(position, 0)
                page.update()
                time.sleep(0.01)
            
            position = -1
            sliding_text.offset = ft.Offset(position, 0)
            page.update()
            

    # Запускаем анимацию
    animate_text()

# Создаем приложение Flet и запускаем его
