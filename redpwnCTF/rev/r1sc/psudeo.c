#include <stdio.h>
#include <string.h>

int sub_107E(int *a1, int a2)
{
  unsigned int result; // rax
  int v3; // rbx
  int v4; // cc

  while ( a2 != 1 )
  {
    result = *(a1 + 8 * *(a1 + 8 * a2));
    v3 = (a1 + 8 * a2 + 8);
    v4 = *(a1 + 8 * v3) <= result;
    *(a1 + 8 * v3) -= result;
    
    if ( !v4 )
    	a2 += 3;

    if ( *(a1 + 8 * a2 + 16) == 2 ) {
        puts("DEBUGBREAK"); //   __debugbreak();

    } else {
      if ( *(a1 + 8 * a2 + 16) == 0 )
        a2 += 3;
      a2 = *(a1 + 8 * a2 + 16);
    }
  }
  return result;
}


int main() {
	char *s;
	char sucess[] = "Sucessfuy";
	char filed[] = "Filed";

	printf("Enter access code: ");
	fgets(s, 48, stdin);
	sub_1073(0, 0);
	if () {
		printf("%s\n",filed);
	} else {
		printf("%s\n",sucess);
	}
	return 0;
}

