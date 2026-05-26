import flet as ft
from src.models import load_contacts, delete_contact, edit_contact

def contacts_view(page, user_state):

    async def new_contact(e):
        await page.push_route("/add_contact")

    async def go_to_search(e):
        await page.push_route("/search")

    sorting = {"mode": "time_add"}


    def list_contact():
        contacts =(load_contacts())
        tiles = []

        for i, c in enumerate(contacts):






            tiles.append(
                ft.ListTile(
                    leading=ft.CircleAvatar(
                        content=ft.Text(c["name"][0].upper()),
                    ),
                    title=ft.Text(c["name"]),
                    subtitle=ft.Text(c["phone"]),
                    trailing=ft.Row(

                    ),
                )
            )
        return tiles

    contact_list = ft.Column(
        controls=list_contact(),
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )

    return ft.View(
        route="/contacts",
        controls=[
            ft.AppBar(title=ft.Text("Контакти"),
                      actions=[ft.IconButton(ft.Icons.SEARCH,
                                             on_click = go_to_search)]),

            contact_list,


        ],
        bottom_appbar=ft.BottomAppBar(
            bgcolor=ft.Colors.SURFACE_CONTAINER_LOW,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                controls=[
                    ft.IconButton(ft.Icons.PERSON),
                ],
            ),
        ),
        floating_action_button=ft.FloatingActionButton(
            icon=ft.Icons.PERSON_ADD, on_click=new_contact),

    )