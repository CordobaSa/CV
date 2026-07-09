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
                
                # Pre-procesamos los datos para que metrics sea una lista de pares [key, value]
                # en lugar de un dict, lo cual es más fácil de iterar con rx.foreach
                processed = []
                for p in response.data:
                    project = dict(p)
                    # Convertir metrics dict a lista de pares para rx.foreach
                    raw_metrics = project.get("metrics", {})
                    if isinstance(raw_metrics, dict):
                        project["metrics_list"] = [[k, v] for k, v in raw_metrics.items()]
                    else:
                        project["metrics_list"] = []
                    
                    # Asegurar que tech_stack siempre sea una lista
                    if not isinstance(project.get("tech_stack"), list):
                        project["tech_stack"] = []
                    
                    # Asegurar valores por defecto para campos opcionales
                    project.setdefault("demo_url", "")
                    project.setdefault("mermaid_diagram", "")
                    project.setdefault("github_url", "#")
                    
                    processed.append(project)
                
                self.projects = processed
                
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
