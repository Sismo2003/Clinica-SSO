# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['menu.py'],
    pathex=[],
    binaries=[],

   datas=[
    ('config.json', '.'),
    ('forest-dark.tcl', '.'),
    ('forest-light.tcl', '.'),
    ('DB.json', '.'),
    ('images/imagen1.png', 'images')
],


    hiddenimports=['babel.numbers'],
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
    name='SSO',
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
    icon=['images/LogoAppMac.icns'],
)
app = BUNDLE(
    exe,
    name='SSO.app',
    icon='images/LogoAppMac.icns',
    bundle_identifier=None,
)
