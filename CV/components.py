import reflex as rx
from CV import styles

def sovereign_card() -> rx.Component:
    """La tarjeta principal de perfil."""
    return rx.box(
        rx.vstack(
            rx.heading("EL SOVEREIGN", size="7", color=styles.colors["text_primary"], font_family="Space Mono, monospace"),
            rx.text("AI-Finance Architect & Systems Engineer", color=styles.colors["accent_neon"], font_weight="bold", font_family="Inter"),
            rx.text("Status: Deploying Capital & Code...", color=styles.colors["text_muted"], font_size="0.9em"),
            
            rx.hstack(
                rx.link(
                    rx.button(
                        "GitHub", 
                        variant="outline", 
                        color_scheme="blue",
                        border_color=styles.colors["accent_silver"],
                        color=styles.colors["text_primary"],
                    ), 
                    href="#"
                ),
                rx.link(
                    rx.button(
                        "LinkedIn", 
                        variant="outline",
                        color_scheme="blue",
                        border_color=styles.colors["accent_silver"],
                        color=styles.colors["text_primary"],
                    ), 
                    href="#"
                ),
                spacing="4",
                margin_top="1em"
            ),
            align="start",
            spacing="2",
        ),
        padding="2em",
        border_radius="8px",
        background_color=styles.colors["bg_surface"],
        border=f"1px solid {styles.colors['accent_silver']}33",
        box_shadow=f"0 4px 20px {styles.colors['accent_neon']}11",
        width="100%",
        max_width="600px",
        margin="0 auto"
    )

def animated_flow_line() -> rx.Component:
    """La línea central que conecta la Sovereign Card con el Feed."""
    return rx.box(
        width="2px",
        height="150px",
        background=f"linear-gradient(to bottom, {styles.colors['bg_app']}, {styles.colors['accent_neon']})",
        margin="0 auto",
        box_shadow=f"0 0 10px {styles.colors['accent_neon']}"
    )

def top_nav() -> rx.Component:
    """Header estilo terminal."""
    return rx.hstack(
        rx.text("[ SOVEREIGN.SYS ]", font_family="Space Mono", font_weight="bold", color=styles.colors["accent_silver"]),
        rx.spacer(),
        rx.text("[ STATUS: ONLINE ]", font_family="Space Mono", color=styles.colors["accent_neon"]),
        width="100%",
        padding="1em 2em",
        border_bottom=f"1px solid {styles.colors['accent_silver']}33"
    )


def _tech_badge(tech: rx.Var[str]) -> rx.Component:
    """Badge individual para una tecnología del tech_stack."""
    return rx.badge(
        tech,
        variant="outline",
        color_scheme="blue",
        font_family="Space Mono, monospace",
        font_size="0.7em",
    )


def _metric_item(key: rx.Var[str], value: rx.Var[str]) -> rx.Component:
    """Un par clave-valor para una métrica."""
    return rx.hstack(
        rx.text(key, color=styles.colors["accent_silver"], font_family="Space Mono, monospace", font_size="0.75em", font_weight="bold"),
        rx.text(value, color=styles.colors["text_primary"], font_family="Inter", font_size="0.85em"),
        spacing="2",
    )


def project_feed_item(project: dict) -> rx.Component:
    """Una fila del timeline para un proyecto (Alternating Timeline Cascade)."""
    return rx.box(
        rx.hstack(
            # Lado A: Tarjeta del Proyecto
            rx.box(
                rx.text(project["title"], font_family="Space Mono, monospace", font_weight="bold", font_size="1.2em", color=styles.colors["text_primary"]),
                
                # Tech Stack Badges
                rx.cond(
                    project["tech_stack"].length() > 0,
                    rx.hstack(
                        rx.foreach(
                            project["tech_stack"],
                            _tech_badge,
                        ),
                        flex_wrap="wrap",
                        gap="0.4em",
                        margin_top="0.8em",
                    ),
                    rx.fragment(),
                ),

                # Contenedor para inyectar el código de Mermaid
                rx.box(
                    rx.html("<div class='mermaid'>\n" + project["mermaid_diagram"] + "\n</div>"),
                    margin_top="1.5em",
                    margin_bottom="1em",
                    padding="1em",
                    background_color=styles.colors["bg_app"],
                    border_radius="4px",
                    overflow_x="auto"
                ),
                
                # Links: Código Fuente y Demo
                rx.hstack(
                    rx.link("Código Fuente", href=project["github_url"], color=styles.colors["text_muted"], text_decoration="underline", font_size="0.9em"),
                    rx.cond(
                        project["demo_url"],
                        rx.link("Live Demo", href=project["demo_url"], color=styles.colors["accent_neon"], text_decoration="underline", font_size="0.9em", font_weight="bold"),
                        rx.fragment(),
                    ),
                    spacing="4",
                    margin_top="0.5em",
                ),
                
                width="45%",
                padding="1.5em",
                background_color=styles.colors["bg_surface"],
                border=f"1px solid {styles.colors['accent_silver']}33",
                border_radius="8px",
                class_name="text-align-dynamic",
                z_index="1",
                transition="box-shadow 0.3s ease, border-color 0.3s ease",
                _hover={
                    "box_shadow": f"0 0 20px {styles.colors['accent_neon']}33",
                    "border_color": f"{styles.colors['accent_neon']}66",
                },
            ),
            
            # Nodo Central (El conector brillante)
            rx.box(
                width="16px",
                height="16px",
                border_radius="50%",
                background_color=styles.colors["bg_app"],
                border=f"3px solid {styles.colors['accent_neon']}",
                box_shadow=f"0 0 12px {styles.colors['accent_neon']}",
                z_index="2"
            ),
            
            # Lado B: Executive Summary + Metrics
            rx.box(
                rx.text("EXECUTIVE SUMMARY", font_family="Space Mono, monospace", font_size="0.8em", color=styles.colors["accent_silver"]),
                rx.text(project["executive_summary"], color=styles.colors["text_muted"], margin_top="0.5em", font_size="0.95em", line_height="1.5"),
                
                # Metrics Section
                rx.cond(
                    project["metrics_list"].length() > 0,
                    rx.box(
                        rx.text("KEY METRICS", font_family="Space Mono, monospace", font_size="0.75em", color=styles.colors["accent_silver"], margin_bottom="0.5em"),
                        rx.foreach(
                            project["metrics_list"],
                            lambda item: _metric_item(item[0], item[1]),
                        ),
                        margin_top="1.2em",
                        padding="1em",
                        background_color=styles.colors["bg_surface"],
                        border_radius="6px",
                        border=f"1px solid {styles.colors['accent_silver']}22",
                    ),
                    rx.fragment(),
                ),

                width="45%",
                padding="1.5em",
                class_name="text-align-dynamic",
                z_index="1"
            ),
            
            width="100%",
            display="flex",
            align_items="center",
            justify_content="space-between",
            class_name="timeline-row",
        ),
        width="100%",
        padding_y="2em",
        position="relative"
    )
