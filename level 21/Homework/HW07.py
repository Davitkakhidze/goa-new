#შექმენი ფუნქცია Find_letter,სადაც გადაცემ სტრინგს.შენი დავალება არის რომ ამ სტრინგიდან დაითვალო რამდენი a ურევია მასში და გამოიტანე ეკრანზე
def Find_letter(string):
    count = 0
    for char in string:
        if char == 'a':
            count += 1
    print("სტრინგში არის {} a".format(count))