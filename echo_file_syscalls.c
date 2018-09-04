#include <stdio.h>
#include <sys/syscall.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>

int main(int argc, char *argv[]){
	int file= syscall(SYS_open,argv[1],O_WRONLY | O_APPEND | O_CREAT, 077);
	if(file<0){
		printf("Error\n");
		return 1;
	}
	if(syscall(SYS_write,file,argv[2],strlen(argv[2])) != strlen(argv[2])){
		printf("Error\n");
	}
	if(close(file)<0){
		printf("Error\n");
		return 1;
	}
	return 0;
}
