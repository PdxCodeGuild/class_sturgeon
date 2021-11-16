# Define the following functions:
# peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.
# valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.
# peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.
import time

welcome_message = "Welcome to the Library-Interface's Peak and Valley Rain Simulator"
for char in welcome_message:
  print(char, end='', flush=True)
  time.sleep(.01)

print("")
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
time.sleep(1.5)
print("The original list is : " + str(data))
time.sleep(1.5)
peak_list = []
valley_list = []

def peaks(data):
    peak = 0
    for i in range(1, len(data) - 1):
        if data[i + 1] < data[i] > data[i -1]:
            print(f"{i} is a peak")
            peak_list.append(i)
            peak += 1
    return print(f"Peak Count: {peak} in position(s): {peak_list}")

peaks(data)
time.sleep(2)
print("")

def valleys(data):
    valley = 0
    for i in range(1, len(data) - 1):
        if data[i + 1] > data[i] < data[i - 1]:
            print(f"{i} is a valley")
            valley_list.append(i)
            valley += 1
    return print(f"Valley Count: {valley} in position(s): {valley_list}")

valleys(data)
time.sleep(1)
peaks_and_valleys = peak_list + valley_list
print(f"Peaks and Valleys: {sorted(peaks_and_valleys)}")
time.sleep(3)
j = 0
while int(j) < len(data):
    j += 1
    if j == 1:
        print(14 * "   " + " X " + 5 * "   " + " X ")
    if j == 2:
        print(13 * "   " + 3 * " X " + 3 * "   " + 2 * " X ")
    if j == 3:
        print("                  " + " X " + "               " + 5 * " X " + "   " + 3 * " X ")
    if j == 4:
        print("               " + 3 * " X " + "         " +  10 * " X ")
    if j == 5:
        print("            " + 5 * " X " + "   " + 11 * " X ")
    if j == 6:
        print("         " + 18 * " X ")
    if j == 7:
        print("      " + 19 * " X ")
    if j == 8:
        print("   " + 20 * " X ")
    if j == 9:
        print(21 * " X ")
else: print(data)

print("")
print(7 * "   " + "'Now with water'")
print(65 * "~")
rain = 65 * '|'
for char in rain:
    print(char, end='', flush=True)
    time.sleep(.01)
print("")
for char in rain:
    print(char, end='', flush=True)
    time.sleep(.01)
print("")
for char in rain:
    print(char, end='', flush=True)
    time.sleep(.01)
print("")
print("")

w = 0
while int(w) < len(data):
    w += 1
    if w == 1:
        print(14 * "   " + " X " + 5 * " O " + " X ")
    if w == 2:
        print(13 * "   " + 3 * " X " + 3 * " O " + 2 * " X ")
    if w == 3:
        print("                  " + " X " + 5 * " O " + 5 * " X " + " O " + 3 * " X ")
    if w == 4:
        print("               " + 3 * " X " + 3 * " O " +  10 * " X ")
    if w == 5:
        print("            " + 5 * " X " + " O " + 11 * " X ")
    if w == 6:
        print("         " + 18 * " X ")
    if w == 7:
        print("      " + 19 * " X ")
    if w == 8:
        print("   " + 20 * " X ")
    if w == 9:
        print(21 * " X ")
else: print(data)

print("")
print("We can visually see there are 18 'O' water symbols in the valleys")
print("")
print("Thank you for using the Library-Inteface's Peak & Valley Rain Simulator")