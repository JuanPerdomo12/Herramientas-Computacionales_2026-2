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
    double h = 0.01;

    state_t y(N);
    initial_conditions(y);

    std::ofstream clean("EDO_0.01.txt");
    clean.close();

    euler(yderiv, y, t_i, t_f, h, print);
    runge_kutta_4(yderiv, y, t_i, t_f, h, print);
    return 0;
}

void initial_conditions(state_t & y)
{
  y[0] = 1.0;
}

void print(const state_t & y, double time)
{
    std::ofstream archivo("EDO_0.01.txt", std::ios::app);
    if (archivo.is_open()){
        archivo << time << " " << y[0] << std::endl;
        archivo.close();
    }
}

void yderiv(const state_t & y, state_t & dydt, double t)
{
    dydt[0] = -y[0];
}
