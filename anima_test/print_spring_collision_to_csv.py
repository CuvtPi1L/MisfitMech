import csv

# Data provided
data = [
    {"Projectile energy": 0.0990013730656496,
     "Projectile Y Position": 2.9990075084945045,
     "Projectile Y Velocity": -0.09949943369971992,
     "Spring Positions": [
         -1.8999510008740723, -1.5933611155069944, -1.2858377842698534,
         -0.9771644277281522, -0.6670505650563325, -0.355096654720191,
         -0.04073623466167232, 0.27686431420952656, 0.5989909999999997, 0.9277545507519676
     ]},
    {"Projectile energy": 0.09208624685209593,
     "Projectile Y Position": 4.007234215513944,
     "Projectile Y Velocity": 0.09596157921381657,
     "Spring Positions": [
         -0.8917242938546321, -0.5851344084875544, -0.27761107725041306,
         0.031062279291288002, 0.34117614196310764, 0.6531300522992491,
         0.9674904723577679, 1.2850910212289668, 1.6072177070194398, 1.9359812577714077
     ]},
    # Include other data in the same format
]

# Write data to CSV
with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Projectile energy", "Projectile Y Position", "Projectile Y Velocity"] +
                    ["Spring Position " + str(i+1) for i in range(10)])  # Assuming 10 spring positions

    for entry in data:
        projectile_energy = entry["Projectile energy"]
        projectile_y_position = entry["Projectile Y Position"]
        projectile_y_velocity = entry["Projectile Y Velocity"]
        spring_positions = entry["Spring Positions"]

        writer.writerow([projectile_energy, projectile_y_position, projectile_y_velocity] + spring_positions)
