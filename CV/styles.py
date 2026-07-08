import reflex as rx

# Color Palette (Financial Noir - Muted Blue Edition)
colors = {
    "bg_app": "#0A0A0B",
    "bg_surface": "#121214",
    "text_primary": "#EAEAEA",
    "text_muted": "#8F8F91",
    "accent_neon": "#2563EB",  # Muted Neon Blue (Elegante, no enceguece)
    "accent_silver": "#C0C0C0",
}

# Global App Styles
base_style = {
    "background_color": colors["bg_app"],
    "color": colors["text_primary"],
    "font_family": "Inter, sans-serif",
    "min_height": "100vh",
    
    # Estilo de selección de texto
    "::selection": {
        "background_color": colors["accent_neon"],
        "color": "#FFFFFF",
    },
    
    # Para los scrollbars que no rompan la estética oscura
    "::-webkit-scrollbar": {
        "width": "8px",
    },
    "::-webkit-scrollbar-track": {
        "background": colors["bg_app"],
    },
    "::-webkit-scrollbar-thumb": {
        "background": colors["bg_surface"],
        "border_radius": "4px",
    },
    "::-webkit-scrollbar-thumb:hover": {
        "background": colors["text_muted"],
    },
    
    # CSS Avanzado para el efecto de Cascada Alterna (Alternating Timeline)
    ".timeline-row:nth-child(even)": {
        "flexDirection": "row-reverse",
    },
    ".timeline-row:nth-child(even) .text-align-dynamic": {
        "textAlign": "right",
    }
}
