#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

vector<string> numbers {"", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

int main() {
	int a;
	int b;
	cin >> a >> b;
	for (int i = a; i <= b; i++) {
		if (i > 0 && i <= 9) {
			cout << nubmers[i] << endl;
		} else {
			cout << ((i % 2 == 0) ? "even" : "odd") << endl;
		}
	}

	return 0;
}
