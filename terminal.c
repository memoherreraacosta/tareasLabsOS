#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>

int main(void){
	char* args= (char *)malloc(30);
	pid_t pid;
	printf("To exit, write down Exit \n");	

	while(1){
		printf("$");
		fgets(args,30,stdin);
		char* command = strtok(args," ");
		char* param = strtok(NULL," ");
		
		if(strcmp(command,"Exit")==0){
			printf("\nHa salido correctamente del programa");
			break;
		}else{
			pid=fork();
			if(pid<0){
				printf("Error al crear el PID");
				return 1;
			}else if(pid==0){
				char path[10];
				strcpy(path,"/bin/");
				strcat(path,command);
				execlp(path,command,param,NULL);
			}else{
				wait(NULL);
			}
		}
	}
	return 0;
}
