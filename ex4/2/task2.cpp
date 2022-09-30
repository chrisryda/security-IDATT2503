#include <iostream>
#include <string>

using namespace std;

string replace(string str) {

    string str_replaced = "";

    for (auto &c : str) {

        switch (c)
        {
        case '<':
            str_replaced += "&lt";
            break;
        case '>':
            str_replaced += "&gt";
            break;
        case '&':
            str_replaced += "&amp";
            break;
        default:
            str_replaced += c;
            break;
        }
        
    }
    
    return str_replaced;
}

int main() 
{
    cout << replace("foo <&> bar") << endl;
    cout << replace("<<<<<<&&&&&>>>>>>>") << endl;
    cout << replace("Cakes & cookies") << endl;
    cout << replace("C++ > all other languages") << endl;

    return 0;
}
