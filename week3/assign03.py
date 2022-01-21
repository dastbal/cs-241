
class Robot:
    def __init__(self):
        self.x = 10
        self.y = 10
        self.fuel = 100

    def fire(self):
        print('Pew! Pew!')
        self.fuel = self.fuel - 15

    def left(self):
        self.x = self.x - 1
        self.fuel = self.fuel - 5

    def right(self):
        self.x = self.x + 1
        self.fuel = self.fuel - 5

    def up(self):
        self.y = self.y - 1
        self.fuel = self.fuel - 5

    def down(self):
        self.y = self.y + 1
        self.fuel = self.fuel - 5

    def status(self) -> str:
        print(f'({self.x}, {self.y}) - Fuel: {self.fuel}')


# function to prpmpt for a command and  validate the input.

def valid_input():

    command = input('Enter command: ')
    if (command == 'left' or command == 'right' or command == 'up' or command == 'down' or command == 'quit' or command == 'fire' or command == 'status'):
        return [True, command]
    else:
        return [False, command]


def control_robot(my_robot, command):
    if (command == 'up'):
        my_robot.up()
    elif (command == 'down'):
        my_robot.down()
    elif (command == 'left'):
        my_robot.left()
    elif (command == 'right'):
        my_robot.right()
    elif (command == 'fire'):
        my_robot.fire()
    elif (command == 'status'):
        my_robot.status()


# validating  the quantity of fuel to work if cannot work reutn true

def fuel_to_work(my_robot, command):
    if (my_robot.fuel < 15 and command == 'fire'):
        return True
    elif (my_robot.fuel < 5):
        return True
    return False


def main():
    command = 'start'
    valid_command = True
    # creating the object of the  robot
    my_robot = Robot()

    while(command != 'quit'):
        # prompting fot  a command
        data = valid_input()
        command = data[1]
        valid_command = data[0]
        # when user enter a bad command  program will ask a new command
        if (valid_command == False):
            # print('wrong command')
            continue
        # if there are not fuel to perform the action  program will ask new command
        if(fuel_to_work(my_robot, command) and command != 'status' and command != 'quit'):
            print('Insufficient fuel to perform action')
            continue

        # controling  the robot
        control_robot(my_robot, command)
    print('Goodbye.')


main()
