import flet as ft
import json, random

class Myapp:
    def __init__(self):
        self.data = json.load(open('assets/questions.json', 'r'))
        self.question = random.choice(self.data)

    def get_random_data(self):
        self.question = random.choice(self.data)
        print(self.question['Answer'])
        

my_app = Myapp()

def main(page: ft.Page):
    page.title = 'MyQuizApp'
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    def check_answer1(e):
        if my_app.question['Answer']=='A':
            b1.style.bgcolor = ft.colors.GREEN_100
            t2.value = my_app.question['Explanation']
        else:
            b1.style.bgcolor = ft.colors.RED_ACCENT_100
        page.update()
    def check_answer2(e):
        if my_app.question['Answer']=='B':
            b2.style.bgcolor = ft.colors.GREEN_100
            t2.value = my_app.question['Explanation']
        else:
            b2.style.bgcolor = ft.colors.RED_ACCENT_100
        page.update()
    def check_answer3(e):
        if my_app.question['Answer']=='C':
            b3.style.bgcolor = ft.colors.GREEN_100
            t2.value = my_app.question['Explanation']
        else:
            b3.style.bgcolor = ft.colors.RED_ACCENT_100
        page.update()
    def check_answer4(e):
        if my_app.question['Answer']=='D':
            b4.style.bgcolor = ft.colors.GREEN_100
            t2.value = my_app.question['Explanation']
        else:
            b4.style.bgcolor = ft.colors.RED_ACCENT_100
        page.update()
    def get_next(e):
        my_app.get_random_data()
        t1.value = f"{my_app.question['QN']}: {my_app.question['Question']}"
        b1.text = f"A:  {my_app.question['A']}"
        b2.text = f"B:  {my_app.question['B']}"
        b3.text = f"C:  {my_app.question['C']}"
        b4.text = f"D:  {my_app.question['D']}"
        t2.value = ''
        b1.style.bgcolor = ft.colors.WHITE
        b2.style.bgcolor = ft.colors.WHITE
        b3.style.bgcolor = ft.colors.WHITE
        b4.style.bgcolor = ft.colors.WHITE
        page.update()

    
    t1 = ft.Text(value=my_app.question['Question'])
    b1 = ft.OutlinedButton(
        text = f"A:  {my_app.question['A']}",
        on_click = check_answer1,
        width = 400,
        style = ft.ButtonStyle(
            shape = ft.RoundedRectangleBorder(radius=10),
            # bgcolor = ft.colors.RED_100
        )
    )
    b2 = ft.OutlinedButton(
        text = f"B:  {my_app.question['B']}",
        on_click = check_answer2,
        width = 400,
        style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
        )
    )
    b3 = ft.OutlinedButton(
        text=f"C:  {my_app.question['C']}",
        on_click=check_answer3,
        width = 400,
        style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
        )
    )
    b4 = ft.OutlinedButton(
        text=f"D:  {my_app.question['D']}",
        on_click=check_answer4,
        width = 400,
        style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
        )
    )
    t2 = ft.Text(value='')

    
    page.add(
        ft.Column(
            controls = [
                t1,
                b1,
                b2,
                b3,
                b4,
                ft.ElevatedButton(text="Next", on_click=get_next),
                t2
            ],
            # alignment = ft.MainAxisAlignment.CENTER,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            
        )
    )
    page.update()

# ft.app(target=main, view=ft.AppView.WEB_BROWSER)
ft.app(target=main)