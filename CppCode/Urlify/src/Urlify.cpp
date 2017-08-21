//============================================================================
// Name        : Urlify.cpp
// Author      : guitar1st
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

void urlify(string* s) {
  char space = ' ';
  string space_new = "%20";
  int counter_spaces = 0;
  size_t i;
  for (i = 0; i < (*s).size() && (*s)[i] != 0; ++i) {
//    cout << typeid((*s)[i]).name() << " " << (*s)[i] << endl;
    if ((*s)[i] == space) {
      counter_spaces++;
    }
  }
  cout << i << endl;
  cout << endl << "Spaces = " << counter_spaces << endl;
  int k = i + counter_spaces * 2;
  for (int j = i; j >= 0; --j) {
    if ((*s)[j] == space) {
      (*s)[k] = '0';
      k--;
      (*s)[k] = '2';
      k--;
      (*s)[k] = '%';
    } else {
      (*s)[k] = (*s)[j];
    }
    --k;
  }
  (*s).shrink_to_fit();
  cout << *s;
}

int main() {
  string str1 = "my url";
  string str2 = " my url  more complex  ";
  str1.resize(20);
  str2.resize(40);
  urlify(&str1);
  urlify(&str2);
  return 0;
}
