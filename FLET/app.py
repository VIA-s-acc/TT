import flet as ft
from pages.main import main_page

def main(page: ft.Page):
    """
    This function is the main entry point of the application. It initializes the page and sets up the navigation bar.
    It also defines the behavior of the navigation bar when the user changes the selected index.
    """

    # Set the page to adaptive mode
    page.adaptive = True

    # Define the behavior of the navigation bar when the user changes the selected index
    def on_navbar_change(e):
        # Clear the controls of the page
        page.controls.clear()

        # Check if the selected index is 0 (Home)
        if e.control.selected_index == 0:
            # Call the main_page function with the page object as an argument
            main_page(page)
        # Check if the selected index is 1 (Settings)
        elif e.control.selected_index == 1:
            # Do nothing (placeholder for future implementation)
            pass

        # Update the page
        page.update()

    # Set up the navigation bar
    page.navigation_bar = ft.NavigationBar(
        # Define the destinations (icons and labels) of the navigation bar
        destinations=[
            ft.NavigationBarDestination(icon=ft.HOME, label='Home'),
            ft.NavigationBarDestination(icon=ft.SETTINGS, label='Settings'),
        ],
        # Set the border of the navigation bar
        border=ft.Border(
            top=ft.BorderSide(color=ft.cupertino_colors.SYSTEM_GREY2, width=2)
        ),
        # Set the background color of the navigation bar
        bgcolor=ft.colors.with_opacity(0.04, ft.cupertino_colors.SYSTEM_BACKGROUND),
        # Set the animation duration of the navigation bar
        animation_duration=1000,
        # Set the initial selected index of the navigation bar
        selected_index=0,
        # Set the behavior of the navigation bar when the user changes the selected index
        on_change=on_navbar_change
    )

    # Call the main_page function with the page object as an argument
    main_page(page)

ft.app(target=main)
    