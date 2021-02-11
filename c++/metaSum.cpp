# include <iostream>
# include <cassert>

int nthFib(int n)
{
    if(n == 0)
    {
        return 0;
    }
    else if(n == 1)
    {
        return 1;
    }
    else
    {
        return nthFib(n-1) + nthFib(n-2);
    };
}

int nthPartialSum(int n){
    int end_result = 0;
    for (int x = 0; x <= n; x++){
        end_result += nthFib(x);
    };
    return end_result;
}

int metaFibonacciSum(int n)
{
    int metaSumEntries[n+1];


    for (int x = 0; x <= n; x++){
        metaSumEntries[x] = nthFib(x);
    };

    int total_sum=  0;
    for (int i = 0; i <= n; i++){
        total_sum += nthPartialSum(metaSumEntries[i]);
    };

    return total_sum;
    // return the result immediately if n<2

    // otherwise, construct a an array called "terms"
    // that contains the Fibonacci terms at indices
    // 0, 1, ..., n

    // construct an array called "extendedTerms" that
    // contains the Fibonacci terms at indices
    // 0, 1, ..., a_n (where a_n is the nth Fibonacci term)

    // when you fill up this array, many of the terms can
    // simply copied from the existing "terms" array. But
    // if you need additional terms, you'll have to compute
    // them the usual way (by adding the previous 2 terms)

    // then, create an array called "partialSums" that
    // contains the partial sums S_0, S_1, ..., S_{a_n}

    // finally, add up the desired partial sums,
    // S_{a_0} + S_{a_1} + ... + S_{a_n},
    // and return this result

}

int main()
{
    std::cout << "Testing...\n";

    assert(metaFibonacciSum(6)==74);

    std::cout << "Success!";

    return 0;
}


