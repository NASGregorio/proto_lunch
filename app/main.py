from router import Router

from nicegui import ui, Client, Tailwind


@ui.page('/')  # normal index page (e.g. the entry point of the app)
@ui.page('/{_:path}')  # all other pages will be handled by the router but must be registered to also show the SPA index page
def main(client: Client):
    router = Router()

    @router.add('/')
    def show_one():
        ui.label('Content One').classes('text-2xl')

    @router.add('/two')
    def show_two():
        ui.label('Content Two').classes('text-2xl')

    @router.add('/three')
    def show_three():
        ui.label('Content Three').classes('text-2xl')

    def show(tab):
        if tab.value == "home":
            router.open(show_one)
        elif tab.value == "ranking":
            router.open(show_two)
        else:
            router.open(show_three)

    ui.query('.nicegui-content').classes('pt-[6rem] pb-[10rem] px-[1rem]')

    with ui.column().classes('w-full items-center'):

        ui.label("Lunch Assistant").classes("font-bold 'Source Sans Pro' font-sans text-[2.75rem] text-[#0F596E] mb-[3rem]")

        with ui.tabs().classes("w-full rounded-lg p-5 bg-gray-100") as tabs:
            ui.tab("home",    label='Home',    icon="house")               .classes("bg-[#eb651a] selection:bg-[#0F596E] hover:bg-[#0F596E] text-white rounded-lg mr-5")
            ui.tab("ranking", label='Ranking', icon="trending_up")         .classes("bg-[#eb651a] selection:bg-[#0F596E] hover:bg-[#0F596E] text-white rounded-lg mx-5")
            ui.tab("picker",  label='Picker',  icon="how_to_vote")         .classes("bg-[#eb651a] selection:bg-[#0F596E] hover:bg-[#0F596E] text-white rounded-lg mx-5")
            ui.tab("review",  label='Review',  icon="rate_review")         .classes("bg-[#eb651a] selection:bg-[#0F596E] hover:bg-[#0F596E] text-white rounded-lg mx-5")
            ui.tab("suggest", label='Suggest', icon="add_location_alt")    .classes("bg-[#eb651a] selection:bg-[#0F596E] hover:bg-[#0F596E] text-white rounded-lg mx-5")
            ui.tab("admin",   label='Admin',   icon="admin_panel_settings").classes("bg-[#eb651a] selection:bg-[#0F596E] hover:bg-[#0F596E] text-white rounded-lg ml-5")
        ui.tab_panels(tabs, value="home", on_change=lambda tab: show(tab))
        ui.query('#c8').style("color: white; border-radius: 0.5rem;")

    with ui.footer(value=False) as footer:
        ui.label('Admin page links')
        with ui.row():
            ui.button('One', on_click=lambda: router.open(show_one)).classes('w-32')
            ui.button('Two', on_click=lambda: router.open(show_two)).classes('w-32')
            ui.button('Three', on_click=lambda: router.open(show_three)).classes('w-32')

    with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20):
        ui.button(on_click=footer.toggle, icon='contact_support').props('fab')


    # this places the content which should be displayed
    router.frame().classes('w-full p-4 bg-gray-100')


# ui.add_body_html('<script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>')
# src = 'https://assets5.lottiefiles.com/packages/lf20_MKCnqtNQvg.json'
# ui.html(f'<lottie-player src="{src}" loop autoplay />').classes('w-24')

# @ui.page('/')
# def page(client: Client):
#     client.layout.classes('pt-[6rem] pb-[10rem] px-[1rem]')

#     with ui.column().classes('w-full'):
#         with ui.column().classes('w-full items-center'):
#             with ui.row():
#                 ui.label("Lunch Assistant").classes("font-bold 'Source Sans Pro' font-sans text-[2.75rem] text-[#0F596E] mb-[6rem]")
#             with ui.tabs().classes("rounded-lg p-5 bg-gradient-to-b from-gray-100 to-white") as tabs:
#                 ui.tab("home",    label='Home',    icon="house")                .classes("bg-[#eb651a] selection:bg-[#0F596E] hover:bg-[#0F596E] text-white rounded-t-lg mr-5")
#                 ui.tab("ranking", label='Ranking', icon="trending_up")          .classes("bg-[#eb651a] selection:bg-[#0F596E] hover:bg-[#0F596E] text-white rounded-t-lg mx-5")
#                 ui.tab("picker",  label='Picker',  icon="how_to_vote")          .classes("bg-[#eb651a] selection:bg-[#0F596E] hover:bg-[#0F596E] text-white rounded-t-lg mx-5")
#                 ui.tab("review",  label='Review',  icon="rate_review")          .classes("bg-[#eb651a] selection:bg-[#0F596E] hover:bg-[#0F596E] text-white rounded-t-lg mx-5")
#                 ui.tab("suggest", label='Suggest', icon="add_location_alt")     .classes("bg-[#eb651a] selection:bg-[#0F596E] hover:bg-[#0F596E] text-white rounded-t-lg mx-5")
#                 ui.tab("admin",   label='Admin',   icon="admin_panel_settings") .classes("bg-[#eb651a] selection:bg-[#0F596E] hover:bg-[#0F596E] text-white rounded-t-lg ml-5")

#             with ui.tab_panels(tabs, value="home").classes('w-full'):
#                 with ui.tab_panel("home"):
#                     ui.label('Content of Home')
#                 with ui.tab_panel("ranking"):
#                     ui.label('Content of Ranking')
#                 with ui.tab_panel("picker"):
#                     ui.label('Content of Picker')
#                 with ui.tab_panel("review"):
#                     ui.label('Content of Review')
#                 with ui.tab_panel("suggest"):
#                     ui.label('Content of Suggest')
#                 with ui.tab_panel("admin"):
#                     ui.label('Content of Admin')

ui.run(title="Lunch Assistant", favicon="🍴")