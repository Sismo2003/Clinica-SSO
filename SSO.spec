# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['menu.py'],
    pathex=[],
    binaries=[],
    datas=[   
    ('documents/forest-light/*','documents/forest-light/'),
    ('documents/forest-dark/*','documents/forest-dark/'),
    ('documents/*','documents/'),
    ('documents/images/*','documents/images'),
    ('documents/templateColoscopia.docx','documents')
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
    onefile = False,
    name='SSO',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['documents/images/LogoAppMac.icns'],
)
app = BUNDLE(
    exe,
    name='SSO.app',
    icon='documents/images/LogoAppMac.icns',
    bundle_identifier=None,
)
