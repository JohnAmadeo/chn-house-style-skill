#!/usr/bin/python3
import os,sys
from decimal import Decimal,InvalidOperation
args=sys.argv[1:]
for i,x in enumerate(args):
 if i and args[i-1]=='-read_intervals':
  parts=x.split('%',1)
  try:
   n=Decimal(parts[0])
   if abs(n)<Decimal('0.000001'):n=Decimal(0)
   args[i]=format(n,'f')+('%'+parts[1] if len(parts)>1 else '')
  except InvalidOperation:pass
os.execv('/opt/homebrew/opt/ffmpeg-full/bin/ffprobe',['ffprobe']+args)
