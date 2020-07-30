import os
import xlrd
import numpy as py

'''
  This is the script for extracting human corrected translation for ifly product with a * in the input file.
    @Author:  Yuxin Miao
    @Date:  2020-07-24 17:50:51
    @Last Modified by:  Yuxin Miao
    @Last Modified time:  2020-07-24 17:50:51
'''

INPUT = 'source_file_1.xlsx'
OUTPUT = 'output.txt'

# Each time read three lines from the file, if a * is met, go back twice to extract, otherwise revert one line and continue.

def get_first_col(handle):
  sheet = handle.sheet_by_index(0)
  return sheet.col_values(0)


if __name__ == '__main__':
  data = get_first_col(xlrd.open_workbook(INPUT))
  output = open(OUTPUT,'w')
  cnt = 0
  for i in range(len(data)):
    if '*' in data[i]:
      cnt += 1
      trans = data[i][1::]
      raw = data[i-2][0:-1].replace('[原文本] ','')
      res = raw + '|' + trans + '\n'
      output.write(res)
      # print(res)
