import flet as ft
from src.models import load_contacts, delete_contact, edit_contact

def contacts_view(page, user_state):

    async def new_contact(e):
        await page.push_route("/add_contact")

    async def go_to_search(e):
        await page.push_route("/search")

    sorting = {"mode": "time_add"}


    def list_contact():
        contacts = sorted_contacts(load_contacts())
        tiles = []

        for i, c in enumerate(contacts):



            def on_redact(e, contact=c):
                edit_name = ft.TextField(label="Ім'я", value=contact["name"])
                edit_phone = ft.TextField(label="Номер", value=contact["phone"])

                def save_edit(e):
                    all_contacts = load_contacts()
                    real_index = next(
                        j for j, x in enumerate(all_contacts)
                        if x["name"] == contact["name"] and x["phone"] == contact["phone"]
                    )
                    edit_contact(real_index, edit_name.value.strip(), edit_phone.value.strip())
                    vicno_redact.open = False
                    contact_list.controls = list_contact()
                    page.update()

                def skasuvaty_edit(e):
                    vicno_redact.open = False
                    page.update()

                vicno_redact = ft.AlertDialog(
                    modal=True,
                    title=ft.Text("Редагувати контакт"),
                    content=ft.Column([edit_name, edit_phone], tight=True),
                    actions=[
                        ft.TextButton("Скасувати", on_click=skasuvaty_edit),
                        ft.TextButton("Зберегти", on_click=save_edit),
                    ],
                )
                page.overlay.append(vicno_redact)
                vicno_redact.open = True
                page.update()


            tiles.append(
                ft.ListTile(
                    leading=ft.CircleAvatar(
                        content=ft.Text(c["name"][0].upper()),
                    ),
                    title=ft.Text(c["name"]),
                    subtitle=ft.Text(c["phone"]),
                    trailing=ft.Row(
                        tight=True,
                        controls=[
                            ft.IconButton(ft.Icons.EDIT, on_click=on_redact),
                            ft.IconButton(ft.Icons.DELETE, on_click=on_delete,
                                          icon_color=ft.Colors.RED),
                        ],
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