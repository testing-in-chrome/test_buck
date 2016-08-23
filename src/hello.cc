#include <iostream>

#include "lib/lib.h"

using namespace std;

int main() {
  cout << "Hello, Buck!" << endl;
  cout << "This is a test!" << endl;
  cout << "This is " << lib::GetName()->c_str() << endl;
  return 0;
}
