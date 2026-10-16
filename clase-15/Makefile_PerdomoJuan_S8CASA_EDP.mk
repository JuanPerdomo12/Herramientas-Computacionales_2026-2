plot_edp_cuerda_extremos_fijos_6tiempos.png: EDP_cuerda_extremos_fijos_0.5.txt PLOTS_JuanPerdomo_S8CASA_EDP.py
	python PLOTS_JuanPerdomo_S8CASA_EDP.py

EDP_cuerda_extremos_fijos_0.5.txt: execute
	./execute

execute: PerdomoJuan_S8CASA_EDP.cpp
	g++ PerdomoJuan_S8CASA_EDP.cpp -o execute

clean:
	rm -f execute EDP_cuerda_extremos_fijos_0.5.txt EDP_cuerda_extremos_fijos_3.txt EDP_cuerda_forzada_0.5.txt plot_edp_cuerda_extremos_fijos_6tiempos.png plot_edp_cuerda_extremos_fijos_100tiempos.png plot_edp_cuerda_extremos_fijos_inestable.png animacion_cuerda_forzada.gif
