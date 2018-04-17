/*
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.
*/
int hammingDistance(int x, int y) {
    
    int tmpInt=x^y;
    int dis=0;
    
    while(tmpInt)
    {
        if((tmpInt>>1)<<1 != tmpInt)
        {
            ++dis;
        }
        
        tmpInt>>=1;
    }
    
    return dis;
}
