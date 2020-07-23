undefined8 main(undefined8 argc, char **argv)
{
    char *tmp;
    char cVar2;
    int32_t iVar3;
    char **var_20h;
    int64_t var_14h;
    uint32_t v8;
    char *input;
    
    input = (char *)sym.imp.malloc(0x400);
    sym.imp.fgets(input, 0x400, _reloc.stdin);
    sym.imp.setbuf(_reloc.stdout, 0);
    while (tmp = sa, *input != '\0') {
    // switch table (61 cases) at 0x402020
        switch(*input) {
            case '!':
                tmp = sa;
                sa = sb;
                sb = sc;
                sc = tmp;
                break;

            case '$':
                sa = sa + 1;
                *sa = '\x01';
                break;
            
            case '+':
                sa[-1] = *sa + sa[-1];
                sa = sa + -1;
                break;
            
            case ',':
                cVar2 = sym.imp.getchar();
                *sa = cVar2;
                break;
            
            case '-':
                sa[-1] = sa[-1] - *sa;
                sa = sa + -1;
                break;
            
            case '.':
                tmp = (char *)str + 1;
                *str = (code)*sa;
                str = (code *)tmp;
                break;
            
            case '[':
                if (*sa == '\0') {
                    v8 = 1;
                    while (v8 != 0) {
                        input = input + 1;
                        if (*input == '[') {
                            v8 = v8 + 1;
                        } else {
                            if (*input == ']') {
                                v8 = v8 - 1;
                            }
                        }
                    }
                }
                break;
            
            case ']':
                if (*sa != '\0') {
                    v7 = 1;
                    while (v7 != 0) {
                        input = input + -1;
                        if (*input == '[') {
                            v7 = v7 + -1;
                        } else {
                            if (*input == ']') {
                                v7 = v7 + 1;
                            }
                        }
                    }
                }
        }
        input = input + 1;
    }
    str = obj.STR;
    iVar3 = sym.imp.strcmp(obj.STR, "HELLO\n");
    if (iVar3 == 0) {
        sym.imp.puts(str);
        sym.imp.system("cat flag.txt");
    } else {
        sym.imp.puts("Failed.");
    }
    return 0;
}
