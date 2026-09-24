plot_edo.png: EDO_euler_0.01.txt EDO_euler_0.001.txt EDO_rk4_0.01.txt EDO_rk4_0.001.txt PLOTS_JuanPerdomo_S5C2_EDO.py
	python PLOTS_JuanPerdomo_S5C2_EDO.py

EDO_euler_0.01.txt: execute
	./execute

execute: PerdomoJuan_S5C2_EDO.cpp
	g++ -std=c++17 PerdomoJuan_S5C2_EDO.cpp -o execute

clean:
	rm -f execute EDO_euler_0.01.txt EDO_euler_0.001.txt EDO_rk4_0.01.txt EDO_rk4_0.001.txt plot_edo.png