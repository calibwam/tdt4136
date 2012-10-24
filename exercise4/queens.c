#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <limits.h>
#include "binomial.h"

void generate_start_state(int * state, int k)
{
    for(int i = 0; i<k; i++){
        state[i] = rand()%k;
    }
}

void print_state(int * state, int k)
{
    int print_array[k][k];
    for(int i = 0; i<k; i++){
        for(int j = 0; j<k; j++){
            if(j == state[i]){
                print_array[i][j] = 1;
            } else {
                print_array[i][j] = 0;
            }
        }
    }
    for(int i = 0; i<k; i++){
        for(int j = 0; j<k; j++){
            printf("%i ", print_array[i][j]);
        }
        printf("\n");
    }
}

int is_solution(int * state, int k, int * collision)
{
    struct attacks {
        int party1;
        int party2;

    };
    struct attacks found_collisions[(int) binomial((ULONG)k,(ULONG)2)];
    struct attacks *next_spot = &found_collisions[0];

    int collisions = 0;
    for(int i = 0; i<k; i++){
        for(int j = i+1; j<k; j++){
            if ((state[j] == state[i]) || (state[j] == state[i]+abs(i-j))
                                       || (state[j] == state[i]-abs(i-j)))
                collisions++;
                struct attacks new_attack;
                new_attack.party1 = state[i];
                new_attack.party2 = state[j];
                *next_spot++ = new_attack;
        }
    }

    // TODO fix random collision
    *collision = found_collisions[0].party2;
    printf("%d\n", found_collisions[0].party2);

    if(!collisions)
        return 1;
    return 0;
}

int num_of_conflicts(int state[], int k, int column, int conflicts[])
{
    for(int i = 0; i<k; i++){
        for(int j = i+1; j<k; j++){
            if ((state[j] == state[i]) || (state[j] == state[i]+abs(i-j))
                                       || (state[j] == state[i]-abs(i-j))){
                conflicts[i]++; 
            }
                
        }
    }
    int lowest = INT_MAX;
    for(int i = 0; i <k; i++){
        if(conflicts[i] < lowest)
            lowest = conflicts[i];
    }
    return lowest;

}

int main(int argc, char** argv)
{
    srand( time(NULL) );
    int k = atoi(argv[1]);
    int state[k];
    generate_start_state(state, k);
    int collision = 0;
    do{
        int min_conflicts[k];
        for(int i = 0; i<k; i++)
            min_conflicts[i] = 0;
        int current_lowest = num_of_conflicts(state, k, collision, min_conflicts);
        int index;
        for(int i = 0; i<k; i++){
            if(min_conflicts[i] == current_lowest && i != state[collision])
                index = i;
        }
        state[collision] = index;
        print_state(state, k);
        printf("\n");

    }while(!is_solution(state, k, &collision));
    print_state(state, k);
}
