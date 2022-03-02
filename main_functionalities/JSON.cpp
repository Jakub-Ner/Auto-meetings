#include <fstream>
#include <sstream>
#include <iostream>
#include "JSON.h"


bool JSON::check_json_correctness() {
    //...
    return true;
}

void JSON::repair_json() {
 // ...
}


void JSON::read_json() {
    std::ifstream file;
    file.open(m_json_path);

    // if file exist and is not empty:
    if (file && file.peek() != std::ifstream::traits_type::eof()) {
        m_content = read_data_at_once(file);
        file.close();

    } else {
        file.close();
        std::ofstream new_file;
        new_file.open(m_json_path);

        new_file << "{}";
        new_file.close();
        m_content = "{}"; // create new json
    }
}

std::string JSON::read_data_at_once(std::ifstream &file) {
    std::ostringstream data;
    data << file.rdbuf(); // reading data
    return data.str();
}

void JSON::save_meeting(const std::string &link, const std::string &date) {
    m_link = link;
    m_date = date;
    read_json();
    if (m_content[m_content.size() - 1] != '}')
        check_json_correctness();

    // preprocess
    m_content[m_content.size() - 2] = ',';
    m_content.erase(m_content.end() - 1);

    // now can easily add data
    convert_data_to_json();

    std::ofstream fout;
    fout.open(m_json_path);
    fout << m_content;
    fout.close();
}

void JSON::convert_data_to_json() {
    get_name();
    std::cout << m_name;
    m_content += "\n  \"" + m_name + "\": {\n"
                + "     \"date\": [\n"
                +"          " + number(m_date.substr(6, 2)) + ",\n"   // day
                +"          " + number(m_date.substr(9, 2)) + ",\n"   // month
                +"          " + m_date.substr(12, 4) +",\n"                // year
                +"          \"" + m_date.substr(0, 2) + ":"+ m_date.substr(3, 2) + "\"\n" // hour:minute
                +"          " + "],\n"
                +"      \"link\": \"" + m_link + "\"\n"
                +"  }\n"
                +"}";
}
std::string JSON::number(std::string &&date){
    if(date[0] == '0') return date.substr(1,1);
    return date;
}

void JSON::get_name() {
    std::ifstream file;
    file.open(m_names_path);

    std::string file_content = read_data_at_once(file);
    extract_name_and_remove_from_list(file_content);

    file.close();

    std::ofstream new_file;
    new_file.open(m_names_path);
    new_file << file_content;
    new_file.close();
}

void JSON::extract_name_and_remove_from_list(std::string &file_content) {
    m_name = "";
    int counter = file_content.size() - 1;

    if (counter <= 0) {
        generate_names();
    }

    while (file_content[counter] != ';') { // counter >= 0 in useless
        m_name += file_content[counter];
        counter--;
    }
    if (!file_content.empty())
        file_content.erase(counter, file_content.size() - 1);
}

void JSON::generate_names() {
    std::ofstream fout;
    fout.open(m_names_path);

    for (int j = 9; j >= 0; j--) {
        const char id1 = j + '0';
        for (int i = 9; i >= 0; i--) {
            const char id2 = i + '0';
            fout << ';' << id2 << id1 << "gniteem";
        }
    }
    fout.close();
}
