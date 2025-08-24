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
#include <vector>
using namespace std;

class HashTable {
private:
    vector<int> table;
    int size;
    int currentSize;

public:
    HashTable(int tableSize) : size(tableSize), currentSize(0) {
        table.resize(size, -1);
    }

    bool isFull() {
        return currentSize == size;
    }

    void insert(int key) {
        if (isFull()) {
            return;
        }

        int hash = key % size;
        int index = hash;
        int i = 1;

        while (table[index] != -1) {
            index = (hash + i * i) % size;
            i++;

            if (i > 2 * size) {
                return; // Avoid infinite loop
            }
        }

        table[index] = key;
        currentSize++;
    }

    void printTable() {
        for (int i = 0; i < size; i++) {
            if (table[i] != -1) {
                cout << table[i] << " ";
            }
        }
        cout << endl;
    }
};

int main() {
    int n, tableSize;
    cin >> n;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    cin >> tableSize;

    HashTable ht(tableSize);
    for (int num : arr) {
        ht.insert(num);
    }

    ht.printTable();

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
