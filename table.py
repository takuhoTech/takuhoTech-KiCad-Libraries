import glob

table_fp  = 'fp-lib-table'
table_sym = 'sym-lib-table'

path_lib = 'KICAD_USER_LIB_DIR'
# D:\GitHub\takuhoTech-KiCad-Libraries

list_path_fp = []
list_name_fp = []
for tmp in glob.glob('./*/*/*.pretty'):
  list_path_fp.append(tmp)
  list_name_fp.append(tmp.split('\\')[-1][:-7])#パスを\で分割し、分割した最後の部分(prettyフォルダ)を取り出し、.prettyをトリミングしてパーツ名とする。

list_path_sym = []
list_name_sym = []
for tmp in glob.glob('./*/*/*.kicad_sym'):
  list_path_sym.append(tmp)
  list_name_sym.append(tmp.split('\\')[-1][:-10])

#print(list_path_fp[0]) #１つの要素の場合は\区切りで表示
print(list_path_fp)     #配列の場合は\\区切りで表示
print(list_name_fp)
print(list_path_sym)
print(list_name_sym)

table_text_fp  = '(fp_lib_table\n'
for (path,name) in zip(list_path_fp,list_name_fp):
  table_text_fp +=  f'  (lib (name "{name}")(type "KiCad")(uri "${{{path_lib}}}{path[1:]}")(options "")(descr ""))\n'
table_text_fp += ')\n'

table_text_sym = '(sym_lib_table\n'
for (path,name) in zip(list_path_sym,list_name_sym):
  table_text_sym += f'  (lib (name "{name}")(type "KiCad")(uri "${{{path_lib}}}{path[1:]}")(options "")(descr ""))\n'
table_text_sym += ')\n'

with open(table_fp, mode='w') as fp:
  fp.write(table_text_fp)

with open(table_sym, mode='w') as sym:
  sym.write(table_text_sym)
