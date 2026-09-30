plot_edo2_OA.png: EDO2_euler_0.01.txt EDO2_euler_0.001.txt EDO2_rk_0.01.txt EDO2_rk_0.001.txt EDO2_lf_0.01.txt EDO2_lf_0.001.txt EDO2_damped_euler_0.01.txt EDO2_damped_euler_0.001.txt EDO2_damped_rk_0.01.txt EDO2_damped_rk_0.001.txt PLOTS_JuanPerdomo_S6C1_EDO2.py
	python PLOTS_JuanPerdomo_S6C1_EDO2.py

EDO2_euler_0.01.txt: execute
	./execute

execute: PerdomoJuan_S6C1_EDO2orden.cpp
	g++ -std=c++17 PerdomoJuan_S6C1_EDO2orden.cpp -o execute

clean:
	rm -f execute EDO2_euler_0.01.txt EDO2_euler_0.001.txt EDO2_rk_0.01.txt EDO2_rk_0.001.txt EDO2_lf_0.01.txt EDO2_lf_0.001.txt EDO2_damped_euler_0.01.txt EDO2_damped_euler_0.001.txt EDO2_damped_rk_0.01.txt EDO2_damped_rk_0.001.txt plot_edo2_OA.png plot_edo2_OA_phase_diagram.png plot_edo2_OA_damped.png plot_edo2_OA_damped_phase_diagram.png