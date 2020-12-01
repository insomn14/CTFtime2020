wierd_str = [0x09, 0x07, 0x11, 0x48, 0x20, 0x73, 0x02, 0x68, 0x2C, 0x67, 0x62, 0x02, 0x3E, 0x36, 0x7D, 0x1A, 0x1E, 0x35, 0x1F, 0x07, 0x2A, 0x1D, 0x3C, 0x0B, 0x71, 0x25, 0x62, 0x57, 0x7E, 0x30, 0x13, 0x3B, 0x71, 0x07, 0x2E]



'''
while ( 1 )
    {
      byte_shit = *after_XOR_maybe;
      *str_from_stack_0 = *after_XOR_maybe;
      if ( !byte_shit || byte_shit == '\n' || byte_shit == '\r' )
        break;
      if ( i_1 > val_8 )                    // 8
        goto EXIT_REJECT;
      if ( byte_shit >= 'A' && byte_shit <= 'Z' )
      {
        byte_shit += 17;
        if ( byte_shit > 'Z' )
          byte_shit = byte_shit - 'Z' + '@';
      }
      if ( *str_from_stack_CMPR != byte_shit )
        goto EXIT_REJECT;
      ++i_1;
      ++str_from_stack_0;
      ++after_XOR_maybe;
      ++str_from_stack_CMPR;
    }
'''


'''
>>> from string import ascii_uppercase as upper
>>> from string import digits
>>>
>>> cmp ='RJJ3DSCP'
>>> get = ''
>>>
>>> while(get != cmp):
...     for c in upper+digits:
...             tmp = chr(check_shit(ord(c)))
...             if tmp == cmp[len(get)]:
...                     get += c
>>> get
'ASS3MBLY'
'''


xoring = lambda x,y : ''.join(chr(j^ x[i%len(x)]) for i,j in enumerate(y))


res = xoring(b'ASS3MBLY', wierd_str)
print(res)

