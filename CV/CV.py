import reflex as rx
from CV import styles
from CV import components
from CV.state import AppState

def index() -> rx.Component:
    return rx.box(
        # Contenedor de fondo para la red de partículas
        rx.box(id="particles-js", position="fixed", width="100vw", height="100vh", z_index="0", top="0", left="0"),
        
        rx.vstack(
            # Top Navigation
            components.top_nav(),
            
            # Perfil principal
            rx.box(
                components.sovereign_card(),
                padding_top="4em",
                width="100%",
                display="flex",
                justify_content="center"
            ),
            
            # Línea de flujo hacia el feed
            components.animated_flow_line(),
            
            # Central Feed Recursivo
            rx.box(
                # Línea central de fondo para unir los nodos (estética)
                rx.box(
                    width="2px",
                    height="100%",
                    background=f"linear-gradient(to bottom, {styles.colors['accent_neon']}, {styles.colors['bg_app']})",
                    position="absolute",
                    left="50%",
                    transform="translateX(-50%)",
                    z_index="0",
                    opacity="0.3"
                ),
                rx.vstack(
                    rx.foreach(
                        AppState.projects,
                        components.project_feed_item
                    ),
                    width="100%",
                ),
                position="relative",
                width="100%",
                max_width="1000px",
                margin="0 auto",
                padding_top="2em"
            ),
            
            width="100%",
            max_width="1200px",
            margin="0 auto",
        ),
        background_color=styles.colors["bg_app"],
        min_height="100vh",
        width="100%"
    )

app = rx.App(
    style=styles.base_style,
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&family=Space+Mono:ital,wght@0,400;0,700;1,400;1,700&display=swap",
    ],
    head_components=[
        rx.script(src="https://cdn.jsdelivr.net/npm/mermaid@10.6.1/dist/mermaid.min.js"),
        rx.script("mermaid.initialize({ startOnLoad: false, theme: 'dark' });"),
        rx.script(src="https://cdn.jsdelivr.net/npm/particles.js@2.0.0/particles.min.js"),
    ]
)
# El evento on_load garantiza que hydrate el estado desde Supabase apenas cargue la página
app.add_page(
    index, 
    title="Sovereign | AI-Finance Architect",
    description="Portafolio Técnico y Arquitectura de Sistemas - Personal Sovereign Platform",
    on_load=AppState.load_projects
)
