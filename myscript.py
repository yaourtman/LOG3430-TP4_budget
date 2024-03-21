"""
Automatisation de git bisect pour trouver le premier
commit pour lequel les tests échouent.
"""

import subprocess

subprocess.call("git bisect start c1a4be04b972b6c17db242fc37752ad517c29402 e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c")
subprocess.call("git bisect run python manage.py test")