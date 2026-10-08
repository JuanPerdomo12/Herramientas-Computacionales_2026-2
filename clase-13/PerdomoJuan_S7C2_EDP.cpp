#include <iostream>
#include <valarray>
#include <functional>
#include <cmath>
#include <fstream>
#include <sstream>

typedef std::valarray<double> state_t;

const double c = 300.0;
const double L = 2.0;

void initial_conditions_edp(state_t & u_pasado);
void print(const state_t & u_futuro, double time);
void struct_filename(std::string problem, double h);

template <class system_t, class printer_t>
void finit_dif_edp(system_t & u_pasado, system_t & u_presete, system_t & u_futuro, double tinit, double tend, double h, printer_t writer)
{
    
}


int main()
{
    int N = ;
    double t_i = 0.0;
    double t_f = 0.1;

    state_t u_pasado(N);
    state_t u_presente(N);
    state_t u_futuro(N);

    for(double h : {0.5, 1.0}){
    struct_filename("cuerda_extremos_fijos", h);
    initial_conditions_edp(u_pasado);
    finit_dif_edp(u_pasado, u_presente, u_futuro, t_i, t_f, h, print);
    }

    return 0;
}

void initial_conditions_edp(state_t & u_pasado){
    int dim = 1;
    u_pasado.resize(1);
}

std::string filename = "";

void print(const state_t & u, double time)
{
    std::ofstream file(filename, std::ios::app);
    if (file.is_open()){
        file << time;
        for(size_t i = 0; i < u.size(); ++i) {
            file << " " << u[i];
        }
        file << std::endl;
        file.close();
    }
}

void struct_filename(std::string problema, double h){
    std::ostringstream sf;
    sf << "EDP_" << problema << "_" << h << ".txt";
    filename = sf.str();

    std::ofstream clean(filename);
    clean.close();
}