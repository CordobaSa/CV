import reflex as rx

config = rx.Config(
    app_name="CV",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.RadixThemesPlugin(),
    ]
)