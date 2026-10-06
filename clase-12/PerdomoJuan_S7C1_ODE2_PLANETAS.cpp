#include <iostream>
#include <valarray>
#include <functional>
#include <cmath>
#include <fstream>
#include <sstream>

typedef std::valarray<double> state_t;

const double G = 0.0002959122082855911; // UA³ days⁻² M_sun⁻¹
const double M_sun = 1.0;
const double M_earth = 3.00348959e-6;

void initial_conditions_1_cuerpo(state_t & r);
void initial_conditions_2_cuerpos(state_t & r);
void initial_conditions_N_cuerpos(state_t & r);
void print(const state_t & r, double time);
void rderiv_1_cuerpo(const state_t & r, state_t & drdt, double t);
void rderiv_2_cuerpos(const state_t & r, state_t & drdt, double t);
void rderiv_N_cuerpos(const state_t & r, state_t & drdt, double t);
void struct_filename(int num_cuerpos, std::string metodo, double h);

class planets_data{
    public:
        double mass;
        double xi;
        double yi;
        double vxi;
        double vyi;
};

template <class deriv_t, class system_t, class printer_t>
void euler(deriv_t rderiv, system_t & r, double tinit, double tend, double h, printer_t writer)
{
    system_t drdt(r.size());
    int n = r.size()/2;

    for(double t = tinit; t <= tend; t += h) {
        rderiv(r, drdt, t);

        for(size_t i = 0; i < n; ++i) {
            r[n+i] += h*drdt[n+i];
            r[i] += h*r[n+i];
        }

        writer(r, t);
    }
}


template <class deriv_t, class system_t, class printer_t>
void leap_frog(deriv_t rderiv, system_t & r, double tinit, double tend, double h, printer_t writer)
{
    system_t drdt(r.size());
    system_t v_half(r.size()/2);
    int n = r.size()/2;

    rderiv(r, drdt, tinit);

    for(size_t i = 0; i < n; ++i) {
        v_half[i] = r[n+i]+(h/2.0)*drdt[n+i];
    }

    for(double t = tinit; t <= tend; t += h) {
        writer(r, t);

        for(size_t i = 0; i < n; ++i) {
            r[i] += h*v_half[i];
        }

        rderiv(r, drdt, t + h);

        for(size_t i = 0; i < n; ++i) {
            v_half[i] += h*drdt[n+i];
            r[n+i] = v_half[i]-(h/2.0)*drdt[n + i];
        }
    }
}


int main()
{
    int N_1_cuerpo = 4;
    int N_2_cuerpos = 8;
    double t_i = 0.0;
    double t_f = 365.0;
    planets_data sol;

    state_t r_1_cuerpo(N_1_cuerpo);
    state_t r_2_cuerpos(N_2_cuerpos);

    for(double h : {0.5, 1.0}){
    struct_filename(1, "euler", h);
    initial_conditions_1_cuerpo(r_1_cuerpo);
    euler(rderiv_1_cuerpo, r_1_cuerpo, t_i, t_f, h, print);

    struct_filename(1, "lf", h);
    initial_conditions_1_cuerpo(r_1_cuerpo);
    leap_frog(rderiv_1_cuerpo, r_1_cuerpo, t_i, t_f, h, print);
    }

    for(double h : {0.5, 1.0}){
    struct_filename(2, "euler", h);
    initial_conditions_2_cuerpos(r_2_cuerpos);
    euler(rderiv_2_cuerpos, r_2_cuerpos, t_i, t_f, h, print);

    struct_filename(2, "lf", h);
    initial_conditions_2_cuerpos(r_2_cuerpos);
    leap_frog(rderiv_2_cuerpos, r_2_cuerpos, t_i, t_f, h, print);
    }
    return 0;
}

void initial_conditions_1_cuerpo(state_t & r)
{
    r[0] = 0.98329;
    r[1] = 0.0;
    r[2] = 0.0;
    r[3] = 0.01750;
}

void initial_conditions_2_cuerpos(state_t & r){
    double x_T = 0.98329;
    double y_T = 0.0;
    double vx_T = 0.0;
    double vy_T = 0.01750;

    double x_S = -(M_earth/M_sun)*x_T;
    double y_S = -(M_earth/M_sun)*y_T;
    double vx_S = -(M_earth/M_sun)*vx_T;
    double vy_S = -(M_earth/M_sun)*vy_T;

    r[0] = x_S;
    r[1] = y_S;
    r[2] = x_T; 
    r[3] = y_T;

    r[4] = vx_S;
    r[5] = vy_S;
    r[6] = vx_T; 
    r[7] = vy_T;
}

void initial_conditions_N_cuerpos(state_t & r){
    planets_data sol;
    planets_data mercurio;
    planets_data venus;
    planets_data tierra;
    planets_data marte;
    planets_data jupiter;
    planets_data saturno;
    planets_data urano;
    planets_data neptuno;

    sol.mass = 1.0;
    mercurio.mass = 1.66e-7;
    venus.mass = 2.447e-6;
    tierra.mass = 3.003e-6;
    marte.mass = 3.227e-7;
    jupiter.mass = 9.548e-4;
    saturno.mass = 2.857e-4;
    urano.mass = 4.366e-5;
    neptuno.mass = 5.151e-5;

    mercurio.xi = -0.2105;
    mercurio.yi = -0.4287;
    mercurio.vxi = 0.0213;
    mercurio.vyi = -0.0118;

    venus.xi = 0.7187;
    venus.yi = -0.0911;
    venus.vxi = 0.0025;
    venus.vyi = -0.2014;

    tierra.xi = -0.1685;
    tierra.yi = 0.9688;
    tierra.vxi = -0.0172;
    tierra.vyi = -0.003;

    marte.xi = -1.3879;
    marte.yi = -0.6203;
    marte.vxi = 0.0055;
    marte.vyi = -0.0118;

    jupiter.xi = 4.0028;
    jupiter.yi = 3.1235;
    jupiter.vxi = -0.0048;
    jupiter.vyi = 0.0065;

    saturno.xi = 6.4101;
    saturno.yi = -6.5207;
    saturno.vxi = 0.0038;
    saturno.vyi = 0.0039;

    urano.xi = 14.4326;
    urano.yi = 13.5574;
    urano.vxi = -0.0027;
    urano.vyi = 0.0027;

    neptuno.xi = 29.8051;
    neptuno.yi = -1.8214;
    neptuno.vxi = 0.0002;
    neptuno.vyi = 0.0031;

    //sol.xi = -std::accumulate()
}

std::string filename = "";

void print(const state_t & r, double time)
{
    std::ofstream file(filename, std::ios::app);
    if (file.is_open()){
        file << time;
        for(size_t i = 0; i < r.size(); ++i) {
            file << " " << r[i];
        }
        file << std::endl;
        file.close();
    }
}

void struct_filename(int num_cuerpos, std::string metodo, double h){
    std::ostringstream sf;
    sf << "EDO2_planetas_" << num_cuerpos << "cuerpos_" << metodo << "_" << h << ".txt";
    filename = sf.str();

    std::ofstream clean(filename);
    clean.close();
}

void rderiv_1_cuerpo(const state_t & r, state_t & drdt, double t)
{
    drdt[0] = r[2];
    drdt[2] = -(G*M_sun)*r[0]/std::pow(std::pow(r[0], 2.0) + std::pow(r[1], 2.0), 1.5);
    drdt[1] = r[3];
    drdt[3] = -(G*M_sun)*r[1]/std::pow(std::pow(r[0], 2.0) + std::pow(r[1], 2.0), 1.5);
}

void rderiv_2_cuerpos(const state_t & r, state_t & drdt, double t)
{
    double dx = r[2]-r[0];
    double dy = r[3]-r[1];
    double dist = std::hypot(dx, dy);
    double dist3 = std::pow(dist, 3.0);

    drdt[0] = r[4];
    drdt[1] = r[5];
    drdt[4] = (G*M_earth*dx)/dist3;
    drdt[5] = (G*M_earth*dy)/dist3;

    drdt[2] = r[6];
    drdt[3] = r[7];
    drdt[6] = -(G*M_sun*dx)/dist3;
    drdt[7] = -(G*M_sun*dy)/dist3;
}

void rderiv_N_cuerpos(const state_t & r, state_t & drdt, double t)
{
    planets_data sol;
    planets_data mercurio;
    planets_data venus;
    planets_data tierra;
    planets_data marte;
    planets_data jupiter;
    planets_data saturno;
    planets_data urano;
    planets_data neptuno;

    sol.mass = 1.0;
    mercurio.mass = 1.66e-7;
    venus.mass = 2.447e-6;
    tierra.mass = 3.003e-6;
    marte.mass = 3.227e-7;
    jupiter.mass = 9.548e-4;
    saturno.mass = 2.857e-4;
    urano.mass = 4.366e-5;
    neptuno.mass = 5.151e-5;
}