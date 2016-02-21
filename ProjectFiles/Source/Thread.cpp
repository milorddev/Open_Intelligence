#include<iostream>
#include<stdio.h>
#include<pthread.h>

void *inc_x(void *x_void_ptr){

  int *x_ptr = (int*) x_void_ptr;
  while(++(*x_ptr) < 100);

  printf("x increment finished\n");

  return NULL;
}

int main(void){

  int x = 0, y = 0;

  pthread_t inc_x_thread;

  printf("x: %d, y: %d\n", x, y);

  if(pthread_create(&inc_x_thread, NULL, inc_x, &x)){
    fprintf(stderr, "Error creating thread\n");
    return 1;
  }

  while(++y < 100);

  printf("y increment finished\n");

  if(pthread_join(inc_x_thread, NULL)){
    fprintf(stderr, "Error joining thread\n");
    return 2;
  }
  printf("x: %d, y: %d\n", x, y);

  return 0;
}

