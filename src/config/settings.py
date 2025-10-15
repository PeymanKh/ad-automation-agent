"""
Configuration Management Module

Handles secure loading and validation of environment variables with support
for local .env files and cloud deployment with GCP Secret Manager integration.

Author: Peyman Kh
Last Updated: 2025-10-12
"""
# Import libraries
import os
import sys
import logging
from enum import Enum
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, SecretStr, BaseModel, ValidationError


class LogLevel(str, Enum):
    """Standard logging levels for application logging configuration."""
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class SystemSettings(BaseSettings):
    """
    Main application configuration with environment-based loading.

    Supports local development with .env files and cloud deployment
    with environment variables from GCP Secret Manager.

    Read .env.example for more information about Environment Variables
    """
    # Application Settings with defaults
    app_name: str = Field(
        default="ad-automation-agent",
        description="Application identifier"
    )
    app_description: str = Field(
        default="The app automates the creation of high-quality and effective social media ads content.",
        description="Application description"
    )
    app_version: str = Field(
        default="1.0.0",
        description="Application version"
    )
    environment: str = Field(
        default="development",
        description="Deployment environment"
    )
    debug: bool = Field(
        default=False,
        description="Enable debug mode"
    )

    # Logging Configuration with defaults
    log_level: LogLevel = Field(
        default=LogLevel.INFO,
        description="Logging level"
    )
    log_format: str = Field(
        default="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        description="Log message format string"
    )

    # Database Configurations
    database_url: SecretStr = Field(
        ...,
        description="Database connection URL"
    )

    # LLM Configurations
    open_ai_api_key: SecretStr = Field(
        ...,
        description="OpenAI API key"
    )
    langsmith_api_key: SecretStr = Field(
        ...,
        description="Langsmith API key"
    )
    tavily_api_key: SecretStr = Field(
        ...,
        description="Tavily API key"
    )

    def is_production(self) -> bool:
        """Check if running in a production environment."""
        return self.environment.lower() == "production"

    def is_development(self) -> bool:
        """Check if running in a development environment."""
        return self.environment.lower() == "development"

    model_config = SettingsConfigDict(
        env_file = Path(__file__).parent.parent.parent / '.env',
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


# Initialize logging with basic configuration
DEFAULT_LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=DEFAULT_LOG_FORMAT)

# Load and validate configuration on module import
try:
    settings = SystemSettings()
    logging.info(f"{settings.app_name} settings loaded successfully for {settings.environment} environment.")
except ValidationError as e:
    logging.error(f"Configuration validation failed: {e}")
    sys.exit(1)
except Exception as e:
    logging.error(f"Failed to load configuration: {e}")
    sys.exit(1)


# Public API
__all__ = ['settings', 'SystemSettings']