"""
Sputnik 9 was the first spacecraft to carry animals into orbit and return them safely to Earth.
Onboard were:

👤 A mannequin cheekily named Ivan Ivanovich (Russian equivalent of "John Doe")
🐕‍🦺 A black dog named Chernushka
🐁 Several mice
🐹 A guinea pig
And before you ask: Yes, all the animals (and Ivan) survived the one full orbit! 😮‍💨

The animals were in their own capsule of the spacecraft, which landed safely in its parachute.

The Earth's atmosphere is divided into five layers:

Exosphere (700–10,000 km): descent rate = 2000 m/s (near vacuum, free fall)
Thermosphere (85–700 km): descent rate = 500 m/s (thin air, minimal drag)
Mesosphere (50–85 km): descent rate = 200 m/s (air thickens, meteors burn here)
Stratosphere (12–50 km): descent rate = 75 m/s (ozone layer, much denser)
Troposphere (0–12 km): descent rate = 20 m/s (densest layer, parachute deploys 🪂)
Sputnik 9's reentry begins from ~200 km. That's in the thermosphere. The atmospheric density increases as the capsule descends... the descent rate slows the lower it gets.

Given a starting altitude (in km), calculate total descent time (in seconds and one decimal).

Examples

Example 1

Input: 200
Output: 1511.7
230.0s (Thermosphere) + 175.0s (Mesosphere) + 506.7s (Stratosphere) + 600.0s (Troposphere)

Example 2

Input: 12
Output: 600.0
600.0s (Troposphere)
"""


def calculate_descent(altitude):
    layers = [
        (700, 10000, 2000),  # Exosphere
        (85, 700, 500),      # Thermosphere
        (50, 85, 200),       # Mesosphere
        (12, 50, 75),        # Stratosphere
        (0, 12, 20)          # Troposphere
    ]

    total_time = 0.0

    for lower, upper, rate in layers:
        if altitude > upper:
            continue
        elif altitude > lower:
            distance = altitude - lower
            time = distance * 1000 / rate  # Convert km to m and divide by rate in m/s
            total_time += time
            altitude = lower

    return round(total_time, 1)


print(calculate_descent(200))

print(calculate_descent(12))
