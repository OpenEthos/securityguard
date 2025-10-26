from pathlib import Path
from yaml import safe_load
from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class Config(BaseModel):
    """
    Represents the structure of the securityguard.yaml configuration file.
    """
    scan_paths: List[Path] = [Path("./")]
    exclude_paths: Optional[List[Path]] = None
    output_format: str = "console"  # e.g., "console", "json", "sarif"
    api_key: Optional[str] = None
    # Add other configuration parameters as needed

    class Config:
        arbitrary_types_allowed = True

    @classmethod
    def from_file(cls, config_dirs: List[Path] = [Path("/etc/securityguard"), Path("~/.config/securityguard"), Path(".")], config_file: Path = Path("securityguard.yaml")) -> 'Config':
        """
        Loads the configuration from the specified YAML file.

        Args:
            config_path: The path to the configuration file.

        Returns:
            A Config object populated with the settings from the file.
        """
        for config_dir in config_dirs:
            config_path = config_dir / config_file
            if config_path.exists():
                break
            else:
                continue
        else:
            raise FileNotFoundError(f"Configuration file '{str(config_file)}' not found in any of the specified directories.")

        with open(str(config_path), 'r') as f:
            config_data = safe_load(f)
        
        return cls.model_validate(config_data)
    






