#include <iostream>
#include <valarray>
#include <functional>
#include <cmath>
#include <fstream>
#include <sstream>

typedef std::valarray<double> state_t;

const double G = 0.0002959122082855911; // UA³ days⁻² M_sun⁻¹
const double M_sun = 1.0;

void initial_conditions(state_t & r);
void print(const state_t & r, double time);
void rderiv(const state_t & r, state_t & drdt, double t);
void struct_filename(std::string metodo, double h);

template <class deriv_t, class system_t, class printer_t>
void euler(deriv_t rderiv, system_t & r, double tinit, double tend, double h, printer_t writer)
{
    system_t drdt(r.size());

    for(double t = tinit; t <= tend; t += h) {
        rderiv(r, drdt, t);

        r[2] = r[2] + h*drdt[2];
        r[0] = r[0] + h*r[2];

        r[3] = r[3] + h*drdt[3];
        r[1] = r[1] + h*r[3];

        writer(r, t);
      }
}


template <class deriv_t, class system_t, class printer_t>
void leap_frog(deriv_t rderiv, system_t & r, double tinit, double tend, double h, printer_t writer)
{
    system_t drdt(r.size());

    rderiv(r, drdt, tinit);

    double vx_half = r[2] + (h/2.0)*drdt[2];
    double vy_half = r[3] + (h/2.0)*drdt[3];

    for(double t = tinit; t <= tend; t += h) {
        writer(r, t);

        r[0] = r[0] + h*vx_half;
        r[1] = r[1] + h*vy_half;

        rderiv(r, drdt, t+h);

        vx_half = vx_half + h*drdt[2];
        vy_half = vy_half + h*drdt[3];

        r[2] = vx_half - (h/2.0)*drdt[2]; 
        r[3] = vy_half - (h/2.0)*drdt[3];
      }
}


int main()
{
    int N = 4;
    double t_i = 0.0;
    double t_f = 365.0;

    state_t r(N);

    for(double h : {0.5, 1.0}){
    struct_filename("euler", h);
    initial_conditions(r);
    euler(rderiv, r, t_i, t_f, h, print);

    struct_filename("lf", h);
    initial_conditions(r);
    leap_frog(rderiv, r, t_i, t_f, h, print);
    }
    return 0;
}

void initial_conditions(state_t & r)
{
  r[0] = 0.98329;
  r[1] = 0.0;
  r[2] = 0.0;
  r[3] = 0.01750;
}

std::string filename = "";

void print(const state_t & r, double time)
{
    std::ofstream file(filename, std::ios::app);
    if (file.is_open()){
        file << time << " " << r[0] << " " << r[1] << " " << r[2] << " " << r[3] << std::endl;
        file.close();
    }
}

void struct_filename(std::string metodo, double h){
    std::ostringstream sf;
    sf << "EDO2_planetas_" << metodo << "_" << h << ".txt";
    filename = sf.str();

    std::ofstream clean(filename);
    clean.close();
}

void rderiv(const state_t & r, state_t & drdt, double t)
{
    drdt[0] = r[2];
    drdt[2] = -(G*M_sun)*r[0]/std::pow(std::pow(r[0], 2.0) + std::pow(r[1], 2.0), 1.5);
    drdt[1] = r[3];
    drdt[3] = -(G*M_sun)*r[1]/std::pow(std::pow(r[0], 2.0) + std::pow(r[1], 2.0), 1.5);
}