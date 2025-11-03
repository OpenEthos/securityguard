"""Configuration module for SecurityGuard."""

from pathlib import Path
from typing import List, Optional

from yaml import safe_load, dump
from pydantic import BaseModel

class Config(BaseModel):
    """
    Represents the structure of the securityguard.yaml configuration file.
    """
    scan_paths: List[Path] = [Path("./")]
    exclude_paths: Optional[List[Path]] = None
    output_format: str = "console"  # e.g., "console", "json", "sarif"
    api_key: Optional[str] = None
    # Add other configuration parameters as needed

    class Config: # pylint: disable=too-few-public-methods
        """Pydantic configuration for Config model."""
        arbitrary_types_allowed = True

    @classmethod
    def from_file(
        cls,
        config_dirs: Optional[List[Path]] = None,
        config_file: Path = Path("securityguard.yaml")
    ) -> 'Config':
        """
        Loads the configuration from the specified YAML file.

        Args:
            config_dirs: List of directories to search for config file.
            config_file: Name of the configuration file.

        Returns:
            A Config object populated with the settings from the file.
        """
        if config_dirs is None:
            config_dirs = [
                Path("/etc/securityguard"),
                Path("~/.config/securityguard"),
                Path(".")
            ]

        for config_dir in config_dirs:
            config_path = config_dir / config_file
            if config_path.exists():
                break
        else:
            raise FileNotFoundError(
                f"Configuration file '{str(config_file)}' not found in any "
                "of the specified directories."
            )

        with open(str(config_path), 'r', encoding='utf-8') as f:
            config_data = safe_load(f)

        return cls.model_validate(config_data)

    def __str__(self) -> str:
        """Returns a string representation of the configuration."""
        return self.model_dump_json(indent=2)

    def __repr__(self) -> str:
        """Returns a detailed string representation of the configuration."""
        return f"Config({self.model_dump()})"

    def to_dict(self) -> dict:
        """Converts the configuration to a dictionary."""
        return self.model_dump()

    @classmethod
    def from_dict(cls, data: dict) -> 'Config':
        """
        Creates a Config object from a dictionary.

        Args:
            data: Dictionary containing configuration parameters.

        Returns:
            A Config object populated with the data.
        """
        return cls.model_validate(data)

    def write_to_file(self, file_path: Path) -> None:
        """
        Writes the current configuration to a YAML file.

        Args:
            file_path: Path to the file where the configuration should be written.
        """

        with open(str(file_path), 'w', encoding='utf-8') as f:
            dump(self.to_dict(), f)
