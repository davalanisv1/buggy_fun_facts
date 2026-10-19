from pathlib import Path

from PyInstaller.utils.hooks import collect_all

root = Path(SPECPATH)
bs4_datas, bs4_binaries, bs4_hiddenimports = collect_all("bs4")


a = Analysis(
    [str(root / "run_app.py")],
    pathex=[str(root)],
    binaries=bs4_binaries,
    datas=[
        (str(root / "index.html"), "."),
        (str(root / "assets"), "assets"),
        *bs4_datas,
    ],
    hiddenimports=bs4_hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="BuggyFunFacts",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
)
