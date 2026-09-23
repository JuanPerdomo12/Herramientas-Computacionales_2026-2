aleatorios.png: rand_array.txt grafica_rand_array.py
	python grafica_rand_array.py

rand_array.txt: execute
	./execute

execute: PerdomoJuan_S5C2_repasoC.cpp
	g++ -std=c++17 PerdomoJuan_S5C2_repasoC.cpp -o execute

clean:
	rm -f execute rand_array.txt aleatorios.png