#include <iostream>
#include <valarray>
#include <functional>
#include <cmath>
#include <fstream>
#include <sstream>

typedef std::valarray<double> state_t;

const double c = 300.0;
const double L = 2.0;

void initial_conditions_edp(state_t & u_pasado, double dx);
void print(const state_t & u_futuro, double time);
void struct_filename(std::string problem, double factor);

template <class system_t, class printer_t>
void finit_dif_edp(system_t & u_pasado, system_t & u_presente, system_t & u_futuro, double tinit, double tend, double factor, printer_t writer)
{
    size_t N = u_pasado.size();
    double dx = L/(N-1);
    double dt = factor*dx/c;
    double alpha = std::pow(c*dt/dx, 2.0);

    double t = tinit;

    writer(u_pasado, t);

    u_presente[0] = 0.0;
    u_presente[N-1] = 0.0;

    for(size_t i = 1; i < N-1; ++i){
        u_presente[i] = u_pasado[i]+0.5*alpha*(u_pasado[i+1]-2.0*u_pasado[i]+u_pasado[i-1]);
    }

    t += dt;
    writer(u_presente, t);

    while(t < tend){
        u_futuro[0] = 0.0;
        u_futuro[N-1] = 0.0;

        for(size_t i = 1; i < N-1; ++i){
            u_futuro[i] = 2*u_presente[i]+u_pasado[i]+alpha*(u_presente[i+1]-2*u_presente[i]+u_presente[i-1]);
        }

        u_pasado = u_presente;
        u_presente = u_futuro;

        t += dt;
        writer(u_presente, t);
    }
}


int main()
{
    int N = 101;
    double t_i = 0.0;
    double t_f = 0.1;

    state_t u_pasado(N);
    state_t u_presente(N);
    state_t u_futuro(N);

    double dx = L/(N-1);
    
    for(double factor : {0.5, 3.0}){
    struct_filename("cuerda_extremos_fijos", factor);
    initial_conditions_edp(u_pasado, dx);
    finit_dif_edp(u_pasado, u_presente, u_futuro, t_i, t_f, factor, print);
    }

    return 0;
}

void initial_conditions_edp(state_t & u_pasado, double dx){
    size_t N = u_pasado.size();

    for(size_t i = 0; i < N; ++i){
        double x = i*dx;
        
        if(x <= L/2.0){
            u_pasado[i] = (0.1/(L/2.0))*x;
        } else {
            u_pasado[i] = -(0.1/(L/2.0))*(x-L);
        }
    }
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

void struct_filename(std::string problema, double factor){
    std::ostringstream sf;
    sf << "EDP_" << problema << "_" << factor << ".txt";
    filename = sf.str();

    std::ofstream clean(filename);
    clean.close();
}