# agent/self_modify.py
import os
from pathlib import Path

def propose_and_apply_change(user_response, proposed_code):
    """
    Si el usuario dice "sí", guarda el código en un archivo y lo agrega al sistema.
    """
    if user_response.lower() == "sí":
        # Crear directorio si no existe
        code_dir = Path("services") / "proposed_actions"
        code_dir.mkdir(exist_ok=True)

        # Guardar el código
        file_path = code_dir / f"new_action_{hash(proposed_code)}.py"
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(proposed_code)
        
        print(f"✅ Código guardado en: {file_path}")
        return True
    
    else:
        print("❌ No se ha aplicado el cambio.")
        return False
