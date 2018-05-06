#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <math.h>

int numThreads=12;
int numpoints=1000000;
int contador=0;

void *quarterCircle(){
	float xco, yco, xsq, ysq, hip;	

	for(int j=0;j<numpoints/numThreads ;j++){
		xco=(float)rand()/(float)RAND_MAX;
		yco=(float)rand()/(float)RAND_MAX;		
		xsq= pow(xco,2);
		ysq= pow(yco,2);
		hip= sqrt(xsq+ysq);
	
		if(hip<1){
			contador=contador+1;
		}
	}
	pthread_exit(NULL);
}

int main(){
	pthread_t threads[numThreads];
	int rr;

	for(int t=0; t<numThreads;t++){
		rr=pthread_create(&threads[t],NULL,quarterCircle,NULL);
	}
	for(int i=0; i<numThreads;i++){
		pthread_join(threads[i],NULL);
	}	
	float pi=(4.0* contador)/numpoints*1.0;
	printf("Valor de Pi: %f calculado con %d numero de threads con %d puntos \n",pi, numThreads,numpoints);
	return 0;
}

//Grafica: https://drive.google.com/file/d/1rk4al4QuN-l5_Hclc6Q33F7uRt7jGP4P/view?usp=sharing
