"""Basic tests for Lanhu MCP Server"""

import sys
import unittest
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


class TestBasic(unittest.TestCase):
    def test_python_version(self):
        """Test that Python version is 3.10 or higher"""
        self.assertGreaterEqual(sys.version_info, (3, 10), "Python 3.10+ is required")

    def test_imports(self):
        """Test that required packages can be imported"""
        try:
            import fastmcp  # noqa: F401
            import httpx  # noqa: F401
            import bs4  # noqa: F401
            import playwright  # noqa: F401
            import lxml  # noqa: F401
        except ImportError as e:
            self.fail(f"Import failed: {e}")

    def test_project_structure(self):
        """Test that key project files exist"""
        self.assertTrue((project_root / "lanhu_mcp_server.py").exists())
        self.assertTrue((project_root / "requirements.txt").exists())
        self.assertTrue((project_root / "README.md").exists())
        self.assertTrue((project_root / "pyproject.toml").exists())

    def test_data_directory_creation(self):
        """Test that data directories can be created"""
        data_dir = project_root / "data"
        data_dir.mkdir(exist_ok=True)
        self.assertTrue(data_dir.exists())

        logs_dir = project_root / "logs"
        logs_dir.mkdir(exist_ok=True)
        self.assertTrue(logs_dir.exists())

    def test_easy_install_avoids_inline_cookie_reparse(self):
        """Test that Windows install script does not reparse Cookie with CMD expansion."""
        script = (project_root / "easy-install.bat").read_text(encoding="utf-8")

        self.assertNotIn('set LANHU_COOKIE=%LANHU_COOKIE:"=%', script)
        self.assertNotIn('type .env ^| findstr /B "LANHU_COOKIE="', script)


if __name__ == "__main__":
    unittest.main()
