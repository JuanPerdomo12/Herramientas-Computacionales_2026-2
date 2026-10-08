plot_edp_cuerda_extremos_fijos_6tiempos.png: EDP_cuerda_extremos_fijos_0.5.txt PLOTS_JuanPerdomo_S7C2_EDP.py
	python PLOTS_JuanPerdomo_S7C2_EDP.py

EDP_cuerda_extremos_fijos_0.5.txt: execute
	./execute

execute: PerdomoJuan_S7C2_EDP.cpp
	g++ -std=c++17 PerdomoJuan_S7C2_EDP.cpp -o execute

clean:
	rm -f execute EDP_cuerda_extremos_fijos_0.5.txt EDP_cuerda_extremos_fijos_3.txt plot_edp_cuerda_extremos_fijos_6tiempos.png plot_edp_cuerda_extremos_fijos_100tiempos.png plot_edp_cuerda_extremos_fijos_inestable.png
