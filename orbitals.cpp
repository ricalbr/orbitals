// #include <math.h>
#define __STDCPP_WANT_MATH_SPEC_FUNCS__ 1
#include <cmath>
#include <fstream>
#include <iostream>
#include <stdlib.h>
#include <time.h>

#define PI 3.14159265358979323846

using namespace std;

double hydrogen_wf(unsigned int n, unsigned int l, unsigned int m, double x,
                   double y, double z);
int factorial(int num);
double fRand(double fMin, double fMax);

int main() {

    // initialize random seed
    srand(time(NULL));

    // parameters
    int N = 100000;
    double L = 10;
    unsigned int n = 3;
    unsigned int l = 0;
    unsigned int m = 0;

    double wf, prob;

    double x = 0.0, y = 0.0, z = 0.0;
    double toss = 0.0;

    ofstream writedata;
    writedata.open("positionXY.txt");

    int i = 0;
    while (i < N) {
        x = fRand(-L, L);
        y = fRand(-L, L);
        z = fRand(-L, L);
        // z = 0;
        wf = hydrogen_wf(n, l, m, x, y, z);
        prob = wf * wf;

        toss = fRand(0, 0.2);

        if (prob > toss) {
            writedata << x << " " << y << " "
                      << " " << z << "\n";
            i++;
            std::cout << i << std::endl;
        }
    }
    writedata.close();
}

double hydrogen_wf(unsigned int n, unsigned int l, unsigned int m, double x,
                   double y, double z) {
    double R = x * x + y * y + z * z;
    double theta = acos(z / R);
    // float phi = atan2(y, x);

    double rho = 2.0 * R / double(n);

    double s_harm = std::sph_legendre(l, m, theta);
    double l_poly = std::assoc_laguerre(n - l - 1, 2 * l + 1, rho);

    double prefactor =
        sqrt(double(pow((2.0 / double(n)), 3) * double(factorial(n - l - 1)) /
                    double(2.0 * double(n) * factorial(n + l))));

    double wf = prefactor * exp(-rho / 2.) * pow(rho, l) * s_harm * l_poly;

    // std::cout << "x= \t\t" << x << std::endl;
    // std::cout << "y= \t\t" << y << std::endl;
    // std::cout << "z= \t\t" << z << std::endl;
    // std::cout << "s harm= \t" << s_harm << std::endl;
    // std::cout << " " << std::endl;

    return wf;
}

int factorial(int num) {
    if (num == 0 || num == 1)
        return 1;
    else
        return num * factorial(num - 1);
}

double fRand(double fMin, double fMax) {
    double f = (double)rand() / RAND_MAX;
    return fMin + f * (fMax - fMin);
}
