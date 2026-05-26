import flet as ft
from models import load_contacts
from views import contacts_view, add_contact_view, search_view

def main(page: ft.Page):
    page.title = "Телефона Книга"
    user_state = load_contacts()
    page.theme_mode = ft.ThemeMode.LIGHT

    def route_change():
        page.views.clear()
        page.views.append(contacts_view(page, user_state))
        if page.route == "/add_contact":
            page.views.append(add_contact_view(page, user_state))
        elif page.route == "/search":
            page.views.append(search_view(page, user_state))

        page.update()

    async def view_pop(e):
        if len(page.views) > 1:
            page.views.pop()
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    route_change()

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)