# %%
from pynput import keyboard

var = [0,0,0,0,0,0,0,0,0,0]
incr = [1]
print(var)

with open('test2.txt') as txt_file:
    line_count = 0
    for row in txt_file:
        print(f'Var {line_count}: {", ".join(row)}')
        var[line_count] = int(row.strip())
        line_count += 1
    print(f'Processed {line_count} lines.')

def writetxt(number,index):
    lines = open('test2.txt', 'r').readlines()
    lines[index] = str(number)+'\n'
    out = open('test2.txt', 'w')
    out.writelines(lines)
    out.close()

var[0] = 0
writetxt(var[0],0)
var[1] = 0
writetxt(var[1],1)

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    match key:
        case keyboard.Key.esc:
            return False
        case keyboard.Key.shift:
            incr[0] += 1
            return True
        case keyboard.Key.alt_l:
            incr[0] -= 1
            return True
        case keyboard.Key.ctrl_l:
            incr[0] = 1
            return True
        case keyboard.KeyCode(vk=96):
            var[0] += incr[0]
            writetxt(var[0],0)
            var[7] += incr[0]
            writetxt(var[7],7)
            return True
        case keyboard.KeyCode(vk=97):
            var[1] += incr[0]
            writetxt(var[1],1)
            var[8] += incr[0]
            writetxt(var[8],8)
            return True
        case keyboard.KeyCode(vk=98):
            var[2] += incr[0]
            writetxt(var[2],2)
            return True
        case keyboard.KeyCode(vk=99):
            var[3] += incr[0]
            writetxt(var[3],3)
            return True
        case keyboard.KeyCode(vk=100):
            var[4] += incr[0]
            writetxt(var[4],4)
            return True
        case keyboard.KeyCode(vk=101):
            var[5] += incr[0]
            writetxt(var[5],5)
            return True
        case keyboard.KeyCode(vk=102):
            var[6] += incr[0]
            writetxt(var[6],6)
            return True
        case keyboard.KeyCode(vk=103):
            var[7] += incr[0]
            writetxt(var[7],7)
            return True
        case keyboard.KeyCode(vk=104):
            var[8] += incr[0]
            writetxt(var[8],8)
            return True
        case keyboard.KeyCode(vk=105):
            var[9] += incr[0]
            writetxt(var[9],9)
            return True

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
    
print(var)
print("task run")