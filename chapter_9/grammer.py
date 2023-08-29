import flet as ft
#importing the user defined class
from standardEnglish import StandardEnglish

def main(page:ft.Page):
    page.title = "Correct My Grammer"
    page.theme_mode = "light"
    page.horizontal_alignment = "center"
    page.window_max_height = 600
    page.window_max_width = 700
    page.window_width = 700
    page.window_height = 600

    # Image in flet 
    logo = ft.Image(src=f"logo.jpg",width=300)

    # Input
    user_input = ft.TextField(hint_text="Enter any sentence...",color="#000000",border_radius=25,autofocus=True)

    # output
    outputText = ft.Text("Your response will be generated here...")

    #defining the function
    def print_result(e):
        #using class functions
        answer = StandardEnglish(str(user_input.value)).convertStandardEnglish() 
        outputText.value = answer

    # Generating a Beautiful container to display output
    outcontainer = ft.Container(
        content = outputText,
        margin = 20,
        padding=20,
        bgcolor="#f2f2f2",
        border_radius=30
    ) 

    # adding the elements 
    page.add(
        logo,
        user_input,
        ft.ElevatedButton("Submit",on_click=print_result),
        outcontainer,
        ft.Image(src=f"children_happy.jpg",width=500)
    )

ft.app(target=main,assets_dir="assets")