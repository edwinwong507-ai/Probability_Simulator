import random
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

print("=====================")
print("Probability Simulator")
print("=====================")

probabilities = []
roll_counts = []
errors = []
six_count = 0

while True: 
    try:
        sims = int(input("Enter the number of simulations: "))
        if sims > 0:
            break
        print("Please enter a positive number of simulations.")
    except ValueError:
        print("You must enter a whole number!") 
    
for i in range(sims):
    dice_roll = random.randint(1, 6) 
    
    if dice_roll == 6:
        six_count += 1

    if (i + 1) % 100 == 0:
        probabilities.append(six_count / (i + 1))
        roll_counts.append(i + 1) 
        errors.append(abs((six_count / (i + 1)) - (1/6))) 

if sims % 100 != 0:
    probabilities.append(six_count / sims)
    roll_counts.append(sims)
    errors.append(abs((six_count / sims) - (1/6)))
    
print(f"Number of times 6 was rolled: {six_count}")
    
experimental = six_count/sims
print(f"The experimental probability is: {experimental:.2%}")
    
theoretical = 1/6
absolute_error = abs(experimental - theoretical)
print(f"The absolute error is:  {absolute_error:.2%}")

fig, (ax1, ax2) = plt.subplots(2, 1)

ax1.plot(roll_counts, probabilities, marker=".", label="Experimental probability")

ax1.axhline(y=1/6, linestyle="--", label="Theoretical probability")

ax1.set_xlabel("Number of rolls")
ax1.set_ylabel("Probability")
ax1.set_title("Probability Convergence of Rolling a Six")
ax1.legend()
ax1.grid(True)

ax1.yaxis.set_major_formatter(mtick.PercentFormatter(1))

ax2.plot(roll_counts, errors, marker="o", label="Absolute error")

ax2.set_xlabel("Number of rolls")
ax2.set_ylabel("Error")
ax2.set_title("Absolute Error vs. Number of Rolls")
ax2.legend()
ax2.grid(True)

ax2.yaxis.set_major_formatter(mtick.PercentFormatter(1))

fig.tight_layout()

plt.show()