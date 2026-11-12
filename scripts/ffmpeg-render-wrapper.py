#!/usr/bin/python3
import os,sys
from decimal import Decimal,InvalidOperation
args=sys.argv[1:]
for i,x in enumerate(args):
 if i and args[i-1] in ['-ss','-sseof','-t','-to']:
  try:
   n=Decimal(x)
   if abs(n)<Decimal('0.000001'):n=Decimal(0)
   args[i]=format(n,'f')
  except InvalidOperation:pass
os.execv('/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg',['ffmpeg']+args)
