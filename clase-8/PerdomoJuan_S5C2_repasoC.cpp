#include <iostream>
#include <cmath>
#include <array>
#include <random>

float funct_div(float mivarflotante, int mivarentera);

int min_val();

int main(){
    int x = 12;
    float y = 95.44;

    std::cout << "\nLa primera variable tiene un valor de " << x << " y la segunda variable tiene un valor de " << y << "\n";

    float z = y/x;

    std::cout << "\nEl resultado de dividir " << y << " en " << x << " es: " << z << "\n";

    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<int> distribution(0,900);

    int Rand_Array[300];
    for (int i = 0; i < 300; ++i) {
        Rand_Array[i] = distribution(gen);
    }

    std::cout << "\n";

    for (int i = 0; i < 300; ++i) {
        std::cout << Rand_Array[i] << " ";
    }

    std::cout << "\n";

    std::cout << "\nEl quinto elemento del arreglo es: " << Rand_Array[4] << "\n";

    std::cout << "\nLa longitud del arreglo es: " << std::size(Rand_Array) << "\n";

    std::cout << "\nEl resultado de la funcion division para 17.5 entre 5 es: " << funct_div(17.5, 5) << "\n";
}

float function1(float mivarflotante, int mivarentera){
    return mivarflotante/mivarentera;
}