void scram(char *arg1)
{
    char *pcVar1;
    char *s;
    char *var_10h;
    undefined8 var_8h;
    
    pcVar1 = (char *)strlen(arg1);
    var_10h = (char *)0x0;
    while (var_10h < pcVar1) {
        var_10h[(int64_t)arg1] = var_10h[(int64_t)arg1] ^ 0x77;
        var_10h = var_10h + 1;
    }
    return;
}

bool asdfghjkl(void)
{
    int32_t iVar1;
    char *arg1;
    char *s1;
    
    printf("ENTER THE CHECKERED FLAG: ");
    arg1 = (char *)getpasswd(0x26);
    scram(arg1);
    iVar1 = strcmp(arg1, pass);
    return iVar1 == 0;
}
