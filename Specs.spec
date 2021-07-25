# -*- mode: python -*-

block_cipher = None


a = Analysis(['FFXIV - Craft Manager.pyw'],
             pathex=['E:\GitHub\FFXIV-Craft'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)


a.datas += [('FFXIV.jpeg','E:\GitHub\FFXIV-Craft\Content\Back_End\Visual_Ressources\FFXIV.jpeg', 'Data')]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='FFXIV - Craft Manager',
          debug=False,
          strip=False,
          upx=True,
          console=False,icon='E:\GitHub\FFXIV-Craft\FFXIVCraft.ico')