#include <iostream>
#include <cstdlib>
#include <ctime>

int main() {
    std::srand(static_cast<unsigned int>(std::time(nullptr)));

    int A[6];
    int B[6];

    for (int i = 0; i < 6; ++i) {
        A[i] = std::rand() % 7;
    }

    for (int i = 0; i < 6; ++i) {
        B[i] = 2 + (std::rand() % 9);
    }

    std::cout << "Arreglo A: [ ";
    for (int i = 0; i < 6; ++i) {
        std::cout << A[i] << " ";
    }
    std::cout << "]\n";

    std::cout << "Arreglo B: [ ";
    for (int i = 0; i < 6; ++i) {
        std::cout << B[i] << " ";
    }
    std::cout << "]\n\n";

    int maxA = A[0];
    for (int i = 1; i < 6; ++i) {
        if (A[i] > maxA) {
            maxA = A[i];
        }
    }

    int minB = B[0];
    for (int i = 1; i < 6; ++i) {
        if (B[i] < minB) {
            minB = B[i];
        }
    }

    if (maxA < minB) {
        std::cout << "elijo A" << std::endl;
    } else {
        std::cout << "elijo B" << std::endl;
    }

    return 0;
}