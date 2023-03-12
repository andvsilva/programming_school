#include <stdio.h>
#include <stdlib.h>
#include <iostream>

using namespace std;

int main(){
	while (true){
		int x, y, z; //VARIÁVEIS DE ENTRADA
		float media; //VARIAVEL PARA A MÉDIA DEVE SER FLOAT, POIS A RESPOSTA PODE SER COM VIRGULA
		printf("RU do aluno: 1234567\n");
		printf("Digite um valor - Antepenultimo valor do RU: "); //Antepenultimo valor do RU
		scanf("%d", &x);
		printf("Digite um valor - Penultimo valor do RU: "); //Penultimo valor do RU
		scanf("%d", &y);
		printf("Digite um valor - Ultimo valor do RU: "); //Ultimo valor do RU
		scanf("%d", &z);
		media = (x + y + z) / 3; //FAZ A MEDIA
		printf("Resposta: %.2f\n", media);
		cout<<"Feito. :)"<<endl;
	}
	return 0;
}