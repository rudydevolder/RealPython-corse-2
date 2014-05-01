import xlrd
wb = xlrd.open(datanitro.xlsm)
sh = wb.sheet_by_name(u'Assumptions-Test')
for rownum in range(sh.nrows):
    print sh.row_values(rownum)