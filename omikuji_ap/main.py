import flet as ft
import random

# メニュー設定
MENU_OPTIONS = {
    "morning_yes": ["マックグリドル", "パンケーキ"],
    "morning_no": ["ソーセージエッグマフィン", "チキンマックナゲット"],
    "day_night_yes": ["マックシェイクL", "ホットアップルパイ", "プチパンケーキハッピーセット"],
    "day_night_no": ["サムライマック", "チキンマックナゲット", "ダブルチーズバーガー"],
}

def main(page: ft.Page):
    page.title = "マクドナルドおみくじ"
    page.bgcolor = "#F5F5F5"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ADAPTIVE

    # --- 音声機能（Audio）を一旦削除しました ---

    # 共通ボックスデザイン
    def create_box(title, control):
        return ft.Container(
            content=ft.Column([
                ft.Text(title, size=18, weight="bold", color="#DB0007"),
                control,
            ], horizontal_alignment="center"),
            bgcolor="white", padding=20, border_radius=20,
            border=ft.border.all(2, "#FFBC0D"), width=350,
            shadow=ft.BoxShadow(blur_radius=15, color="#00000011")
        )

    mac_image = ft.Image(src="mc_top.png", width=180, height=180, fit="contain")

    time_group = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="morning", label="朝ごはん", 
    label_style=ft.TextStyle(      # (2) TextStyle開始
        color=ft.Colors.BLACK
    )),
            ft.Radio(value="day_night", label="昼・夜ごはん", 
    label_style=ft.TextStyle(      # (2) TextStyle開始
        color=ft.Colors.BLACK
    )),
        ], alignment="center"),
        value="morning"
    )

    sweet_group = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="yes", label="Yes", 
    label_style=ft.TextStyle(      # (2) TextStyle開始
        color=ft.Colors.BLACK
    )),
            ft.Radio(value="no", label="No", 
    label_style=ft.TextStyle(      # (2) TextStyle開始
        color=ft.Colors.BLACK
    )),
        ], alignment="center"),
        value="yes"
    )

    def run_diagnosis(e):
        # 診断ロジック
        cat = (time_group.value) + ("_yes" if sweet_group.value == "yes" else "_no")
        menu = random.choice(MENU_OPTIONS.get(cat, MENU_OPTIONS["day_night_no"]))

        page.clean()
        page.add(
            mac_image,
            ft.Text("あなたへのおすすめは...", size=18, color="#555555"),
            ft.Container(
                content=ft.Text(menu, size=26, weight="bold", color="white", no_wrap=True),
                bgcolor="#DB0007", padding=ft.padding.symmetric(vertical=25, horizontal=40),
                border_radius=20,
            ),
            ft.Divider(height=40, color="transparent"),
            ft.ElevatedButton("もう一度診断", on_click=lambda _: reset(), style=ft.ButtonStyle(bgcolor="#FFBC0D", color="black")),
            ft.TextButton("トップへ戻る", on_click=lambda _: reset(), style=ft.ButtonStyle(color="#DB0007"))
        )
        page.update()

    def reset():
        page.clean()
        initial_view()
        page.update()

    def initial_view():
        page.add(
            mac_image,
            ft.Text("マクドナルドおみくじ", size=26, weight="bold", color="#DB0007"),
            ft.Divider(height=20, color="transparent"),
            create_box("今の時間は？", time_group),
            ft.Divider(height=10, color="transparent"),
            create_box("三度の飯より甘味が好き？", sweet_group),
            ft.Divider(height=30, color="transparent"),
            ft.ElevatedButton("診断する", on_click=run_diagnosis, bgcolor="#FFBC0D", color="black", width=250, height=60)
        )

    initial_view()
    page.update()

ft.app(target=main, view=ft.AppView.WEB_BROWSER, assets_dir="assets")