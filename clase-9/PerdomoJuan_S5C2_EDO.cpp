#include <iostream>
#include <valarray>
#include <functional>
#include <cmath>
#include <fstream>
#include <sstream>

typedef std::valarray<double> state_t;

void initial_conditions(state_t & y);
void print(const state_t & y, double time);
void yderiv(const state_t & y, state_t & dydt, double t);
void struct_filename(std::string metodo, double h);

template <class deriv_t, class system_t, class printer_t>
void euler(deriv_t yderiv, system_t & y, double tinit, double tend, double h, printer_t writer)
{
    system_t dydt(y.size());

    for(double t = tinit; t <= tend; t += h) {
        yderiv(y, dydt, t);

        y = y + h*dydt;

        writer(y, t);
      }
}

template <class deriv_t, class system_t, class printer_t>
void runge_kutta_4(deriv_t yderiv, system_t & y, double tinit, double tend, double h, printer_t writer)
{
    system_t k1(y.size());
    system_t k2(y.size());
    system_t k3(y.size());
    system_t k4(y.size());

    for(double t = tinit; t <= tend; t += h) {
        yderiv(y, k1, t);
        yderiv(y + h*k1/2.0, k2 , t + h/2.0);
        yderiv(y + h*k2/2.0, k3 , t + h/2.0);
        yderiv(y + h*k3, k4 , t + h);

        y = y + (h/6.0)*(k1+2.0*k2+2.0*k3+k4);

        writer(y, t);
      }
}


int main()
{
    int N = 1;
    double t_i = 0.0;
    double t_f = 2.0;

    state_t y(N);

    for(double h : {0.01, 0.001}){
    struct_filename("euler", h);
    initial_conditions(y);
    euler(yderiv, y, t_i, t_f, h, print);

    struct_filename("rk4", h);
    initial_conditions(y);
    runge_kutta_4(yderiv, y, t_i, t_f, h, print);
    }
    return 0;
}

void initial_conditions(state_t & y)
{
  y[0] = 1.0;
}

std::string filename = "";

void print(const state_t & y, double time)
{
    std::ofstream file(filename, std::ios::app);
    if (file.is_open()){
        file << time << " " << y[0] << std::endl;
        file.close();
    }
}

void struct_filename(std::string metodo, double h){
    std::ostringstream sf;
    sf << "EDO_" << metodo << "_" << h << ".txt";
    filename = sf.str();

    std::ofstream clean(filename);
    clean.close();
}

void yderiv(const state_t & y, state_t & dydt, double t)
{
    dydt[0] = -y[0];
}
