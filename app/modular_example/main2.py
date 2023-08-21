import os

import example_c
import example_pages
import home_page
import theme

from nicegui import app, ui


# @ui.page('/')
# def index():
#     ui.textarea('This note is kept between visits') \
#         .classes('w-96').bind_value(app.storage.user, 'note')

@ui.page('/')
def index_page() -> None:
    with theme.frame('Homepage'):
        home_page.content()


def on_shutdown():
    print('Shutdown has been initiated!')

example_pages.create()

app.include_router(example_c.router)

app.on_shutdown(on_shutdown)
ui.run(
    title="Lunch Assistant",
    storage_secret=os.environ['STORAGE_ENV']
)