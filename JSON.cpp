#include <fstream>
#include <sstream>
#include "JSON.h"


bool check_json_correctness() {
    std::string content = read_json();
    //...
    return true;
}

void repair_json(std::string &content) {

}


std::string read_json() {
    std::string path = "variables/meetings.json";
    std::ifstream file;
    file.open(path);
    std::string content;

    // if file exist and is not empty:
    if (file && file.peek() != std::ifstream::traits_type::eof()) {
        std::ostringstream ss;
        ss << file.rdbuf(); // reading data
        file.close();
        return ss.str();
    }
    else {
        file.close();
        std::ofstream new_file;
        new_file.open(path);

        new_file << "{}";
        new_file.close();
        return "{}"; // create new json
    }
}

void generate_names() {
    std::string name = "meeting";
    std::ofstream fout;
    fout.open("variables/names.txt");

    for (int j = 0; j < 10; j++) {
        const char id1 = j + '0';
        for (int i = 0; i < 10; i++) {
            const char id2 = i + '0';
            fout << name << id1 << id2 << "\n";
        }
    }
    fout.close();
}