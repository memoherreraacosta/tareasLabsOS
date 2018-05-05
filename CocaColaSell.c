#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>

sem_t semaphore;
int cokeAvailable=20;

void *sellCoke(){

	int sold;
	while(cokeAvailable>0){
		sold=1+rand()%4;
		sem_wait(&semaphore);
		if(sold>cokeAvailable){
			printf("Perdon, no puedo vender %d cocas, solo tengo %d\n",sold,cokeAvailable);
			sem_post(&semaphore);
		}else{
			cokeAvailable-=sold;
			printf("Se vendieron %d cocas",sold);
			sem_post(&semaphore);
		}
	}
	pthread_exit(NULL);
}
int main(){
	int compradores=4;
	sem_init(&semaphore,0,1);
	pthread_t threads[compradores];
	int rc;

	for(int i=0;i<compradores;i++){
		rc=pthread_create(&threads[i],NULL,sellCoke,NULL);
	}
	for(int j=0;j<compradores;j++){
		pthread_join(threads[j],NULL);
	}
	printf("Todas las cocas se vendieron");
	return 0;
}
