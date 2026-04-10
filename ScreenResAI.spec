# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all

block_cipher = None
ctk_datas, ctk_binaries, ctk_hiddenimports = collect_all('customtkinter')
anth_datas, anth_binaries, anth_hiddenimports = collect_all('anthropic')

a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=ctk_binaries + anth_binaries,
    datas=ctk_datas + anth_datas,
    hiddenimports=ctk_hiddenimports + anth_hiddenimports + [
        'tkinter', 'tkinter.messagebox', 'tkinter.filedialog',
        'ctypes', 'ctypes.wintypes', 'winreg', 'anthropic', 'httpx',
        'certifi', 'charset_normalizer', 'sniffio', 'anyio', 'packaging',
    ],
    hookspath=[], excludes=['matplotlib', 'numpy', 'pandas'],
    cipher=block_cipher, noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz, a.scripts, a.binaries, a.zipfiles, a.datas, [],
    name='ScreenResAI', debug=False, bootloader_ignore_signals=False,
    strip=False, upx=True, upx_exclude=[], runtime_tmpdir=None,
    console=False, disable_windowed_traceback=False, argv_emulation=False,
    target_arch=None, codesign_identity=None, entitlements_file=None,
    uac_admin=True,
)
