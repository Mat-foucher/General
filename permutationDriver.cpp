#include <iostream>
#include "Permutation.h"

using namespace std;

int main()
{
    int arrSize = 4;
    
    int p[4] = {2,1,3,4};

    Permutation sig; 
    
    sig.setSize(arrSize);
    sig.setP(p);

    sig.showPermutation();

    cout << endl;

    sig.cycleType();

    


    

}