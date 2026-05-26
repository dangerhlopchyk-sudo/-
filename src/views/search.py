import flet as ft
from src.models import load_contacts, delete_contact, edit_contact

def search_view(page, user_state):

    async def go_to_contacts(e):
        await page.push_route("/contacts")

    def on_search(e):
        poshuk = search_field.value.strip().lower()
        contacts = load_contacts()

        if poshuk == "":
            results = contacts
        else:
            results = [
                i for i in contacts
                if poshuk in i["name"].lower()
                or poshuk in i["phone"]
            ]

        result_list.controls = build_results(results)
        page.update()

    def build_results(contacts):
        tiles = []

        for i, c in enumerate(contacts):

            def on_delete(e, index=i, contact=c):
                def pidtverdshena_delete(e):
                    delete_contact(index)
                    vikno_delete.open = False
                    on_search(None)

                def cancel_delete(e):
                    vikno_delete.open = False
                    page.update()

                vikno_delete = ft.AlertDialog(
                    modal=True,
                    title=ft.Text("Видалити контакт?"),
                    content=ft.Text(f"Ви впевнені що хочете видалити {contact['name']}?"),
                    actions=[
                        ft.TextButton("Скасувати", on_click=cancel_delete),
                        ft.TextButton("Видалити",
                                      on_click=pidtverdshena_delete,
                                      style=ft.ButtonStyle(color=ft.Colors.RED)),
                    ],
                )
                page.overlay.append(vikno_delete)
                vikno_delete.open = True
                page.update()

            def on_redact(e, index=i, contact=c):
                edit_name = ft.TextField(label="Ім'я", value=contact["name"])
                edit_phone = ft.TextField(label="Номер", value=contact["phone"])

                def save_edit(e):
                    edit_contact(index, edit_name.value.strip(), edit_phone.value.strip())
                    vicno_redact.open = False
                    on_search(None)

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

    search_field = ft.TextField(
        label="Пошук",
        expand=True,
        on_change=on_search,
        prefix_icon=ft.Icons.SEARCH,
    )

    result_list = ft.Column(
        controls=[],
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )

    return ft.View(
        route="/search",
        controls=[
            ft.AppBar(
                title=search_field,
                actions=[
                    ft.TextButton("Скасувати", on_click=go_to_contacts)
                ]
            ),
            result_list,
        ],
    )