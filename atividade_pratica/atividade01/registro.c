#include <stdio.h>
#include <stdlib.h>
#include <iostream>

using namespace std;

// Function to reverse a string
void reverse(string str)
{
    for (int i = str.length() - 1; i >= 0; i--)
        cout << str[i];
	cout<<"\n";
}

int main()
{
	// variaveis RU e nome.
	long ru;
  	char name[1000];
  	printf("Digite o RU: ");
  	scanf("%ld", &ru);

    printf("Digite o seu nome: ");
    scanf(" %[^\t\n]s", name);

	// true if num is perfectly divisible by 2
    if(ru % 2 == 0)
        printf("numero do RU %ld --> par.\n", ru);
    else
        printf("numero do RU %ld --> impar.\n", ru);

	// reverter o nome -> RU
	reverse(name);
    return 0;
}