import yaml
from pathlib import Path
from typing import Dict, Any

PROMPTS_DIR = Path('prompts')
PROMPTS_FILE = 'prompts.yaml'

def load_yaml_file(file_path: str, encoding: str = 'utf-8') -> Dict[str, Any]:
    """
    Load a YAML file and return its content.
    
    Args:
        file_path: Path to the YAML file
        encoding: File encoding (default: utf-8)
        
    Returns:
        Dictionary with YAML content
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        yaml.YAMLError: If YAML parsing fails
        ValueError: If file is empty or invalid
    """
    file_path = Path(file_path)
    
    # Verificar que el archivo existe
    if not file_path.exists():
        raise FileNotFoundError(f"YAML file not found: {file_path}")
    
    # Verificar que no está vacío
    if file_path.stat().st_size == 0:
        raise ValueError(f"YAML file is empty: {file_path}")
    
    try:
        with file_path.open('r', encoding=encoding) as f:
            data = yaml.safe_load(f)
            
        # Verificar que el contenido no es None
        if data is None:
            raise ValueError(f"YAML file contains no valid data: {file_path}")
            
        return data
        
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Error parsing YAML file '{file_path}': {e}") from e
    except UnicodeDecodeError as e:
        raise ValueError(f"Encoding error in file '{file_path}': {e}") from e

def load_prompts_config(file_path: str = None) -> Dict[str, Any]:
    """
    Load prompts configuration from YAML file.
    
    Args:
        file_path: Path to the prompts YAML file
        
    Returns:
        Dictionary with prompts configuration
        
    Raises:
        FileNotFoundError: If prompts file doesn't exist
        ValueError: If prompts structure is invalid
    """
    if file_path is None:
        file_path = PROMPTS_DIR / PROMPTS_FILE

    data = load_yaml_file(file_path)
    
    # Validar estructura esperada
    if 'prompts' not in data:
        raise ValueError(f"Invalid prompts file structure: missing 'prompts' key in {file_path}")
    
    if not isinstance(data['prompts'], dict):
        raise ValueError(f"Invalid prompts file structure: 'prompts' must be a dictionary in {file_path}")
    
    return data

def get_system_prompt(context: str = 'default', file_path: str = None) -> str:
    """
    Get system prompt for specific context.
    
    Args:
        context: Prompt context (default, technical, support, etc.)
        file_path: Path to the prompts YAML file
        
    Returns:
        System prompt string
        
    Raises:
        KeyError: If the specified context doesn't exist
        FileNotFoundError: If prompts file doesn't exist
        ValueError: If prompts structure is invalid
    """
    if file_path is None:
        file_path = PROMPTS_DIR / PROMPTS_FILE

    config = load_prompts_config(file_path)
    prompt_key = f'system_{context}'
    
    if prompt_key not in config['prompts']:
        available = [k.replace('system_', '') for k in config['prompts'].keys() 
                    if k.startswith('system_')]
        raise KeyError(f"Prompt context '{context}' not found. Available: {available}")
    
    prompt = config['prompts'][prompt_key]
    
    # Asegurar que el prompt no esté vacío
    if not prompt or not prompt.strip():
        raise ValueError(f"Empty prompt for context '{context}'")
    
    return prompt.strip()

# Función de conveniencia para caso más común
def load_system_prompt(file_path: str = None) -> str:
    """
    Load default system prompt.
    
    Args:
        file_path: Path to the prompts YAML file
        
    Returns:
        Default system prompt string
    """
    if file_path is None:
        file_path = PROMPTS_DIR / PROMPTS_FILE
        
    return get_system_prompt('default', file_path)

if __name__ == '__main__':
    # Ejemplo de uso robusto
    try:
        # Load prompt by default
        system_prompt = load_system_prompt()
        print("✓ System prompt loaded successfully")
        print(f"Length: {len(system_prompt)} characters")
        
        # Load system_prompt
        tech_prompt = get_system_prompt('alternative')
        print("✓ Alternative prompt loaded successfully")
        
        # Mostrar configuración completa
        config = load_prompts_config()
        print(f"✓ Configuration loaded - Version: {config.get('version', 'Unknown')}")
        
    except FileNotFoundError as e:
        print(f"✗ File not found: {e}")
    except KeyError as e:
        print(f"✗ Missing prompt: {e}")
    except ValueError as e:
        print(f"✗ Invalid file: {e}")
    except yaml.YAMLError as e:
        print(f"✗ YAML error: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")