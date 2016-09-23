#include <iostream>

#include "lib/lib.h"

using namespace std;

int main() {
  cout << "Hello, Buck!" << endl;
  cout << "This is a test!" << endl;
  cout << "This is " << lib::GetName()->c_str() << endl;
  cout << "This is a change to test gerrit" << endl;
  cout << "This is another change to test gerrit" << endl;
  cout << "Yet another line" << endl;
  return 0;
}
