# -*- mode: python ; coding: utf-8 -*-


from pathlib import Path
from PyInstaller.utils.hooks import collect_submodules

project = Path(SPECPATH)
server_root = project.parent / 'server_USKO-Russia-Tab'
if not (server_root / 'server.py').is_file():
    raise FileNotFoundError('Для сборки нужен соседний проект server_USKO-Russia-Tab')

a = Analysis(
    ['USKO-Russia-Tab.py'],
    pathex=[],
    binaries=[],
    datas=[(str(server_root / 'server.py'), 'overlay_server'),
           (str(server_root / 'assets'), 'overlay_server/assets')],
    # server.py загружается как ресурс, поэтому его импорты указываем явно.
    hiddenimports=collect_submodules('uvicorn') + collect_submodules('websockets') +
                  ['fastapi', 'fastapi.staticfiles', 'fastapi.responses'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='USKO-Russia-Tab',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=[str(project / 'Images' / 'icon.ico')],
)
