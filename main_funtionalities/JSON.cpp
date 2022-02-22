#include <fstream>
#include <sstream>
#include <iostream>
#include "JSON.h"


bool JSON::check_json_correctness() {
    //...
    return true;
}

void JSON::repair_json() {

}


void JSON::read_json() {
    std::ifstream file;
    file.open(json_path);

    // if file exist and is not empty:
    if (file && file.peek() != std::ifstream::traits_type::eof()) {
        _content = read_data_at_once(file);
        file.close();

    } else {
        file.close();
        std::ofstream new_file;
        new_file.open(json_path);

        new_file << "{}";
        new_file.close();
        _content = "{}"; // create new json
    }
}

std::string JSON::read_data_at_once(std::ifstream &file) {
    std::ostringstream data;
    data << file.rdbuf(); // reading data
    return data.str();
}

void JSON::save_meeting(const std::string &link, const std::string &date) {
    _link = link;
    _date = date;
    read_json();
    if (_content[_content.size() - 1] != '}')
        check_json_correctness();

    // preprocess
    _content[_content.size() - 2] = ',';
    _content.erase(_content.end() - 1);

    // now can easily add data
    convert_data_to_json();

    std::ofstream fout;
    fout.open(json_path);
    fout << _content;
    fout.close();
}

void JSON::convert_data_to_json() {
    get_name();
    std::cout << _name;
    _content += "\n  \"" + _name + "\": {\n"
                + "     \"date\": [\n"
                +"          " + number(_date.substr(6, 2)) + ",\n"   // day
                +"          " + number(_date.substr(9, 2)) + ",\n"   // month
                +"          " + _date.substr(12, 4) +",\n"                // year
                +"          \"" + _date.substr(0, 2) + ":"+ _date.substr(3, 2) + "\"\n" // hour:minute
                +"          " + "],\n"
                +"      \"link\": \"" + _link + "\"\n"
                +"  }\n"
                +"}";
}
std::string JSON::number(std::string &&date){
    if(date[0] == '0') return date.substr(1,1);
    return date;
}

void JSON::get_name() {
    std::ifstream file;
    file.open(names_path);

    std::string file_content = read_data_at_once(file);
    extract_name_and_remove_from_list(file_content);

    file.close();

    std::ofstream new_file;
    new_file.open(names_path);
    new_file << file_content;
    new_file.close();
}

void JSON::extract_name_and_remove_from_list(std::string &file_content) {
    _name = "";
    int counter = file_content.size() - 1;

    if (counter <= 0) {
        generate_names();
    }

    while (file_content[counter] != ';') { // counter >= 0 in useless
        _name += file_content[counter];
        counter--;
    }
    if (!file_content.empty())
        file_content.erase(counter, file_content.size() - 1);
}

void JSON::generate_names() {
    std::ofstream fout;
    fout.open(names_path);

    for (int j = 9; j >= 0; j--) {
        const char id1 = j + '0';
        for (int i = 9; i >= 0; i--) {
            const char id2 = i + '0';
            fout << ';' << id2 << id1 << "gniteem";
        }
    }
    fout.close();
}
