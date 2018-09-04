#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>

int main(int argc, char *argv[]){
	int file=open(argv[1], O_WRONLY | O_APPEND | O_CREAT, 0777);
	if(file<0){
		printf("Error al abrir el archivo\n");
		return 1;
	}
	if(write(file,argv[2],strlen(argv[2]))!= strlen(argv[2])){
		printf("Error al escribir el archivo\n");
		return 1;
	}
	if(close(file)<0){
		printf("Error\n");
		return 1;
	}
	return 0;
}
