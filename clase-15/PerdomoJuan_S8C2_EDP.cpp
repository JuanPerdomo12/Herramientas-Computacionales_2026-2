#include <iostream>
#include <valarray>
#include <functional>
#include <cmath>
#include <math.h>
#include <fstream>
#include <sstream>

typedef std::valarray<double> state_t;

const double nu = 10e-4;
const double L = 1.0;

void initial_conditions_edp(state_t & u_pasado, double dx, int N);
void print(const state_t & u, double time);
void struct_filename(std::string problem, double factor);

template <class system_t, class printer_t>
void finit_dif_edp(system_t & u_presente, system_t & u_futuro, double tinit, double tend, double dt, double dx, printer_t writer)
{
    int N = static_cast<int>(std::round(std::sqrt(u_presente.size())));
    double alpha = nu*dt/(dx*dx);

    double t = tinit;
    writer(u_presente, t);

    while (t < tend) {
        u_futuro = u_presente;

        for (int i = 1; i < N - 1; ++i) {
            for (int j = 1; j < N - 1; ++j) {
                int idx = i*N+j;
                int idx_right = (i+1)*N+j;
                int idx_left = (i-1)*N+j;
                int idx_up = i*N+(j+1);
                int idx_down = i*N+(j-1);

                u_futuro[idx] = u_presente[idx]+alpha*(u_presente[idx_right]+u_presente[idx_left]+u_presente[idx_up]+u_presente[idx_down]-4.0*u_presente[idx]);
            }
        }
        
        for (int k = 0; k < N; ++k) {
            u_futuro[k] = 50.0;
            u_futuro[(N-1)*N+k] = 50.0;
            u_futuro[k*N] = 50.0;
            u_futuro[k*N+(N-1)] = 50.0;
        }

        t += dt;
        u_presente = u_futuro;

        writer(u_presente, t);
    }
}

int main()
{
    double dx = 0.1;
    int N = static_cast<int>(L/dx)+1; 

    double dt = 10.0; 

    double t_i = 0.0;
    double t_f = 2500.0;

    state_t u_presente(N*N);
    state_t u_futuro(N*N);

    struct_filename("difusion_2D", dt);
    
    initial_conditions_edp(u_presente, dx, N);

    finit_dif_edp(u_presente, u_futuro, t_i, t_f, dt, dx, print);

    return 0;
}

void initial_conditions_edp(state_t & u_pasado, double dx, int N) {
    for (int i = 0; i < N; ++i) {
        double x = i*dx;
        for (int j = 0; j < N; ++j) {
            double y = j*dx;

            int idx = i*N+j;

            u_pasado[idx] = 50.0;

            if (x >= 0.2 && x <= 0.4 && y >= 0.4 && y <= 0.6) {
                u_pasado[idx] = 100.0;
            }
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