segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
total_segs = int(segundos_str)
dias = total_segs // 86400
segs_restantes_1 = total_segs % 86400
horas = segs_restantes_1 // 3600
segs_restantes_2 = segs_restantes_1 % 3600
minutos = segs_restantes_2 // 60
segs_restantes_final = segs_restantes_2 % 60
print(dias, "dias,", horas, "horas,", minutos, "minutos e", segs_restantes_final, "segundos.")
