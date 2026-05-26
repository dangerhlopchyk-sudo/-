import flet as ft
from src.models import save_contact

def add_contact_view(page, user_state):
    codes = {
        "Україна +380": "+380",
        "США +1": "+1",
        "Велика Британія +44": "+44",
        "Німеччина +49": "+49",
        "Франція +33": "+33",
        "Польща +48": "+48",
        "Італія +39": "+39",
        "Іспанія +34": "+34",
        "Нідерланди +31": "+31",
        "Швейцарія +41": "+41",
        "Австрія +43": "+43",
        "Бельгія +32": "+32",
        "Чехія +420": "+420",
        "Угорщина +36": "+36",
        "Румунія +40": "+40",
        "Казахстан +7": "+7",
        "Туреччина +90": "+90",
        "ОАЕ +971": "+971",
        "Китай +86": "+86",
        "Японія +81": "+81",
        "Індія +91": "+91",
        "Корея +82": "+82",
        "Бразилія +55": "+55",
        "Мексика +52": "+52",
        "Австралія +61": "+61",
    }

    async def go_to_contacts(e):
        await page.push_route("/contacts")

    async def done(e):
        name = pole_name.value.strip()
        code = codes[phone_code.value]
        phone = code + pole_phone.value.strip()
        save_contact(name, phone)
        await page.push_route("/contacts")

    def check_fields(e):
        name = pole_name.value.strip()
        phone = pole_phone.value.strip()

        if len(name.strip()) < 2:
            message.value = "Ім'я занадто коротке мінімум 2 символи"
            btn_ok.disabled = True
        elif len(name.strip()) > 50:
            message.value = "Ім'я занадто довге максимум 50 символів"
            btn_ok.disabled = True
        elif len(phone.strip()) <= 7:
            message.value = "Мінімальна довжина номеру 7 символів"
            btn_ok.disabled = True
        else:
            message.value = ""
            btn_ok.disabled = False
        page.update()
    pole_name = ft.TextField(label="І'мя", expand=True, on_change=check_fields)
    phone_code = ft.Dropdown(
        value="Україна +380",
        options=[ft.dropdown.Option(k) for k in codes.keys()]
    )
    pole_phone = ft.TextField(label="Номер", expand=True, on_change=check_fields)

    message = ft.Text(color=ft.Colors.RED,size = 15)

    btn_ok = ft.Button(
        "Готово",
        disabled=True,
        on_click=done,
        style=ft.ButtonStyle(color=ft.Colors.WHITE)
    )

    return ft.View(
        route="/add_contact",
        controls=[
            ft.AppBar(
                title=ft.Text("Новий Контакт"),
                leading_width=100,
                leading=ft.TextButton('Скасувати', on_click=go_to_contacts),
                actions=[ft.Row(controls=[btn_ok])]
            ),
            ft.Column([
                pole_name,
                ft.Row([phone_code, pole_phone]),
                message
            ])
        ]
    )