#შექმენით ფუნქცია Even ფუნქცია სადაც გადაცემთ სიას,ამ სიაში უნდა იყოს კენტების და ლუწებიც.თქვენი დავალება არის რომ ამ რიცხვებიდან დააბრუნოთ მხოლოდ ლუწებიი
def Even(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers