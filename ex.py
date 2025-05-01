import pyautogui
import time
import keyboard

pyautogui.FAILSAFE = False

def auto_typer(text, delay=0.05): 
    pyautogui.write(text)  
    pyautogui.write(' ')  
    time.sleep(delay)

def main():
    cpp_code = '''
#include <iostream>
#include <climits>

using namespace std;

int divide(int dividend, int divisor) {
    if (dividend == INT_MIN && divisor == -1) {
        return INT_MAX;
    }

    long long a = abs((long long)dividend);
    long long b = abs((long long)divisor);
    long long result = 0;

    while (a >= b) {
        long long temp = b, multiple = 1;
        
        while (a >= (temp << 1)) {
            temp <<= 1;
            multiple <<= 1;
        }

        a -= temp;
        result += multiple;
    }

    if ((dividend < 0) != (divisor < 0)) {
        result = -result;
    }

    if (result < INT_MIN) {
        return INT_MIN;
    }
    if (result > INT_MAX) {
        return INT_MAX;
    }

    return result;
}

int main() {
    int dividend, divisor;
    cin >> dividend >> divisor;
    cout << divide(dividend, divisor) << endl;
    return 0;
}


    '''

    delay = 0.1 
    print("Press Alt+= to start auto-typing the C++ code...")

    auto_typing_started = False  
    while True:
        if keyboard.is_pressed('alt+=') and not auto_typing_started:  
            print("Auto-typing will start in 5 seconds...")
            time.sleep(2)
            print("Auto-typing started. Press ALT+G to stop.")
            auto_typer(cpp_code, delay)
            auto_typing_started = True 
            time.sleep(1) 

        if keyboard.is_pressed('alt+.'):
            print("Stop typing...")
            auto_typing_started = False  

        if keyboard.is_pressed('alt+]'):
            print("Exiting program...")
            break
        
        time.sleep(0.1)  

if __name__ == "__main__":
    main()
