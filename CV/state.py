import reflex as rx
import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Cargamos las variables de entorno desde el archivo .env
load_dotenv()

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

# Inicializamos el cliente. Si falta alguna credencial, no fallará silenciosamente, 
# pero es importante controlarlo.
if SUPABASE_URL and SUPABASE_KEY:
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
else:
    supabase = None
    print("WARNING: Credenciales de Supabase no encontradas.")

class AppState(rx.State):
    """Estado global de la aplicación (The Single Source of Truth)."""
    
    projects: list[dict] = []
    is_loading: bool = False

    def load_projects(self):
        """Función asíncrona (operacionalmente) para hidratar el estado."""
        if supabase:
            self.is_loading = True
            try:
                # Realizamos el fetch de la tabla 'projects'
                response = supabase.table("projects").select("*").order("id", desc=True).execute()
                print(f"[DEBUG] Proyectos cargados desde Supabase: {response.data}")
                self.projects = response.data
                
                # Desencadenamos los efectos JS después de cargar los datos
                return rx.call_script('''
                    if (window.particlesJS) {
                        particlesJS.load("particles-js", "/particles.json", function() {});
                    }
                    if (typeof mermaid !== "undefined") {
                        setTimeout(() => mermaid.run(), 500);
                    }
                ''')
            except Exception as e:
                print(f"Error fetching from Supabase: {e}")
            finally:
                self.is_loading = False
