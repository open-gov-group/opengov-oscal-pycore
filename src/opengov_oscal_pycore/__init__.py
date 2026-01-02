"""
opengov_oscal_core

Schlanker Kern für Arbeit mit NIST OSCAL in Python.
Baut auf oscal-pydantic auf und bietet:
- Modell-Reexports
- Repository-Funktionen (Datei-Handling)
- Utilities für Props/Parts
- Katalog-spezifische CRUD-Helfer
- einfache Versionierungs-Utilities
"""

from .models import (
    Catalog,
    Profile,
    ComponentDefinition,
    SystemSecurityPlan,
)

__all__ = [
    "Catalog",
    "Profile",
    "ComponentDefinition",
    "SystemSecurityPlan",
]
