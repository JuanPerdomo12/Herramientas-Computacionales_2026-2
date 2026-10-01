#include <iostream>
#include <valarray>
#include <functional>
#include <cmath>
#include <fstream>
#include <sstream>

typedef std::valarray<double> state_t;

const double k = 50.0;
const double m = 0.2;
const double b = 0.08;

void initial_conditions(state_t & x);
void print(const state_t & x, double time);
void xderiv(const state_t & x, state_t & dxdt, double t);
void struct_filename(std::string metodo, double h);
void xderiv_damped(const state_t & x, state_t & dxdt, double t);

template <class deriv_t, class system_t, class printer_t>
void euler(deriv_t xderiv, system_t & x, double tinit, double tend, double h, printer_t writer)
{
    system_t dxdt(x.size());

    for(double t = tinit; t <= tend; t += h) {
        xderiv(x, dxdt, t);

        x[1] = x[1] + h*dxdt[1];
        x[0] = x[0] + h*x[1];

        writer(x, t);
      }
}

template <class deriv_t, class system_t, class printer_t>
void runge_kutta_4(deriv_t xderiv, system_t & x, double tinit, double tend, double h, printer_t writer)
{
    system_t k1(x.size());
    system_t k2(x.size());
    system_t k3(x.size());
    system_t k4(x.size());

    for(double t = tinit; t <= tend; t += h) {
        writer(x, t);

        xderiv(x, k1, t);
        xderiv(x + h*k1/2.0, k2 , t + h/2.0);
        xderiv(x + h*k2/2.0, k3 , t + h/2.0);
        xderiv(x + h*k3, k4 , t + h);

        x = x + (h/6.0)*(k1+2.0*k2+2.0*k3+k4);
      }
}

template <class deriv_t, class system_t, class printer_t>
void leap_frog(deriv_t xderiv, system_t & x, double tinit, double tend, double h, printer_t writer)
{
    system_t dxdt(x.size());

    xderiv(x, dxdt, tinit);

    double v_half = x[1] + (h/2.0)*dxdt[1];

    for(double t = tinit; t <= tend; t += h) {
        writer(x, t);

        x[0] = x[0] + h*v_half;

        xderiv(x, dxdt, t+h);

        v_half = v_half + h*dxdt[1];

        x[1] = v_half - (h/2.0)*dxdt[1]; 
      }
}


int main()
{
    int N = 2;
    double t_i = 0.0;
    double t_f = 5.0;

    state_t x(N);

    for(double h : {0.01, 0.001}){
    struct_filename("euler", h);
    initial_conditions(x);
    euler(xderiv, x, t_i, t_f, h, print);

    struct_filename("rk", h);
    initial_conditions(x);
    runge_kutta_4(xderiv, x, t_i, t_f, h, print);

    struct_filename("lf", h);
    initial_conditions(x);
    leap_frog(xderiv, x, t_i, t_f, h, print);
    }

    for(double h : {0.01, 0.001}){
        struct_filename("damped_euler", h);
        initial_conditions(x);
        euler(xderiv_damped, x, t_i, t_f, h, print);

        struct_filename("damped_rk", h);
        initial_conditions(x);
        runge_kutta_4(xderiv_damped, x, t_i, t_f, h, print);
    }
    return 0;
}

void initial_conditions(state_t & x)
{
  x[0] = 0.1;
  x[1] = 0.0;
}

std::string filename = "";

void print(const state_t & x, double time)
{
    std::ofstream file(filename, std::ios::app);
    if (file.is_open()){
        file << time << " " << x[0] << " " << x[1] << std::endl;
        file.close();
    }
}

void struct_filename(std::string metodo, double h){
    std::ostringstream sf;
    sf << "EDO2_" << metodo << "_" << h << ".txt";
    filename = sf.str();

    std::ofstream clean(filename);
    clean.close();
}

void xderiv(const state_t & x, state_t & dxdt, double t)
{
    dxdt[0] = x[1];
    dxdt[1] = -(k/m)*x[0];
}

void xderiv_damped(const state_t & x, state_t & dxdt, double t)
{
    dxdt[0] = x[1];
    dxdt[1] = -(k/m)*x[0] - b*x[1];
}