#include <iostream>
#include "filesystem/path.h"

using namespace filesystem;

int main() {
	std::cout<<"*** Running filesystem example ***\n";
	std::cout<<"current path: " << path::getcwd() << std::endl;
	return 0;
}
