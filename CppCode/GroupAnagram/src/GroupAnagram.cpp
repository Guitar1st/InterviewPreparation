//============================================================================
// Name        : GroupAnagram.cpp
// Author      : guitar1st
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <string>
using namespace std;

void GroupAnagram(const vector<string>* s) {
  vector<vector<string>> result;
  vector<string> sorted_anagrams;
  string tmp;
  bool match;
  size_t match_index;
  for (auto i : *s) {
    tmp = i;
    sort(tmp.begin(), tmp.end());
    match = false;
    match_index = -1;
    for (int j = 0; j < sorted_anagrams.size(); ++j) {
      if (tmp == sorted_anagrams[j]) {
        match = true;
        match_index = j;
        break;
      }
    }
    if (!match) {
      vector<string> new_anagrams;
      new_anagrams.push_back(i);
      result.push_back(new_anagrams);
      sorted_anagrams.push_back(tmp);
    } else {
      result[match_index].push_back(i);  // TODO: insert lexicographically
    }
  }
  for (auto i : result) {
    for (auto j : i) {
      cout << j << " ";
    }
    cout << endl;
  }
}

int main() {
  const vector<string> test1 = {"eat", "tea", "tan", "ate", "nat", "bat"};
//	for (auto i : test1) {
//	  cout << i << endl;
//	}
	GroupAnagram(&test1);
	return 0;
}
