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
    std::ifstream f("./variables/meetings.json"); //taking file as inputstream
    std::string content;
    if (f) {
        std::ostringstream ss;
        ss << f.rdbuf(); // reading data
        content = ss.str();
    }
    return content;
}

void generate_names() {
    std::string name = "meeting";
    std::ofstream fout;
    fout.open("./variables/names.txt");

    for (int j = 0; j < 10; j++) {
        const char id1 = j + '0';
        for (int i = 0; i < 10; i++) {
            const char id2 = i + '0';
            fout << name << id1 << id2 << "\n";
        }
    }
    fout.close();
}