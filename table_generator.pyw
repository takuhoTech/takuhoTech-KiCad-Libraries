"""
KiCad library table generator.

Copyright (c) 2025 takuhoTech
Licensed under the MIT License
"""
import glob, os
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox

# Environment variable (set in KiCad) that points to the local repository directory containing this script
LIB_ENV_VAR      = 'KICAD_USER_LIB_DIR'
# Output file names
OUTPUT_FP_TABLE  = 'fp-lib-table'
OUTPUT_SYM_TABLE = 'sym-lib-table'
OUTPUT_BLK_TABLE = 'design-block-lib-table'

def find_libs(pattern: str):
    """Search libraries by pattern and return a list of (Path, name) tuples."""
    return [(Path(p), Path(p).stem) for p in glob.glob(pattern, recursive=True)]

def make_table(kind: str, libs: list[tuple[Path, str]]) -> str:
    """Generate lib_table text for KiCad."""
    version = '  (version 7)\n' if kind in ('sym', 'design_block') else ''
    entries = ''.join(
        f'  (lib (name "{n}")(type "KiCad")(uri "${{{LIB_ENV_VAR}}}/{str(p).replace(os.sep, '/')}")(options "")(descr ""))\n'
        for p, n in libs
    )
    return f'({kind}_lib_table\n{version}{entries})\n'

def main():
    root = tk.Tk()
    root.withdraw()

    project_file = filedialog.askopenfilename(
        title='Select KiCad Project',
        defaultextension='.kicad_pro',
        filetypes=[('KiCad Project', '*.kicad_pro'), ('All files', '*.*')]
    )
    if not project_file:
        messagebox.showinfo('Canceled', 'No project file selected.')
        return
    project_dir = Path(project_file).parent

    fp_libs  = find_libs('./**/*.pretty')
    sym_libs = find_libs('./**/*.kicad_sym')
    blk_libs = find_libs('./**/*.kicad_blocks')
    (project_dir / OUTPUT_FP_TABLE).write_text(make_table('fp', fp_libs), encoding='utf-8')
    (project_dir / OUTPUT_SYM_TABLE).write_text(make_table('sym', sym_libs), encoding='utf-8')
    (project_dir / OUTPUT_BLK_TABLE).write_text(make_table('design_block', blk_libs), encoding='utf-8')

    messagebox.showinfo(
        'Done',
        f'Footprint libraries:\t{len(fp_libs)}\n'
        f'Symbol libraries:\t{len(sym_libs)}\n'
        f'Block libraries:\t{len(blk_libs)}\n\n'
        f'Files generated:\n'
        f'- {OUTPUT_FP_TABLE}\n'
        f'- {OUTPUT_SYM_TABLE}\n'
        f'- {OUTPUT_BLK_TABLE}\n\n'
        f'Location:\n{project_dir}'
    )

if __name__ == '__main__':
    main()
