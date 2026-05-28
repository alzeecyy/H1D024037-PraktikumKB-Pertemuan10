def hitung_fitness(kromosom, barang, kapasitas_tas):
    total_harga = 0
    total_bobot = 0
    for i in range(len(kromosom)):
        if kromosom[i] == 1:
            total_harga += barang[i][1]
            total_bobot += barang[i][2]
    if total_bobot > kapasitas_tas:
        return 0
    else:
        return total_harga

if __name__ == "__main__":
    barang = [("Barang 1", 10, 5),
              ("Barang 2", 40, 4),
              ("Barang 3", 30, 6),
              ("Barang 4", 50, 3),
              ("Barang 5", 35, 7)]
    kapasitas_tas = 15
    populasi_awal = [[1, 0, 1, 0, 1],
                     [0, 1, 0, 1, 0],
                     [1, 1, 0, 0, 1]]
    fitness_populasi = [hitung_fitness(individu, barang, kapasitas_tas) for individu in populasi_awal]
    print("\nNilai Fitness:")
    for idx, fitness in enumerate(fitness_populasi):
        print(f"Individu {idx+1}: Fitness = {fitness}")
