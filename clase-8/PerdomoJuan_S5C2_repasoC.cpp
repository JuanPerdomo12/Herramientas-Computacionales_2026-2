#include <iostream>
#include <cmath>
#include <array>
#include <random>
#include <fstream>

float funct_div(float mivarflotante, int mivarentera);
int min_val(int array[], int size);
void odd_nums(int array[], int size, int max_val);

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

    std::ofstream archivo("rand_array.txt");
    for (int i = 0; i < 300; ++i) {
    archivo << Rand_Array[i] << "\n";
    }
    archivo.close();

    std::cout << "\n";

    for (int i = 0; i < 300; ++i) {
        std::cout << Rand_Array[i] << " ";
    }

    std::cout << "\n";

    std::cout << "\nEl quinto elemento del arreglo es: " << Rand_Array[4] << "\n";

    std::cout << "\nLa longitud del arreglo es: " << std::size(Rand_Array) << "\n";

    std::cout << "\nEl resultado de la funcion division para 17.5 entre 5 es: " << funct_div(17.5, 5) << "\n";

    std::cout << "\nEl valor minimo del arreglo es: " << min_val(Rand_Array, std::size(Rand_Array)) << "\n";

    std::cout << "\nLos numeros impares en el arreglo hasta encontrar un numero mayor a 800 son: ";
    odd_nums(Rand_Array, std::size(Rand_Array), 800);

    return 0;
}

float funct_div(float mivarflotante, int mivarentera){
    return mivarflotante/mivarentera;
}

int min_val(int array[], int size){
    int min = array[0];
    for (int i = 1; i < size; ++i) {
        if (array[i] < min) {
            min = array[i];
        }
    }
    return min;
}

void odd_nums(int array[], int size, int max_val){
    for (int i = 0; i < size; ++i){
        if (array[i] > max_val){
            break;
        }
        if (array[i] % 2 != 0){
            std::cout << array[i] << " ";
        }
    }
    std::cout << "\n";
}
