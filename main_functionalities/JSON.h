#ifndef AUTOMATION_OF_STUDIES_JSON_H
#define AUTOMATION_OF_STUDIES_JSON_H

#include <string>

class JSON {
private:
    const std::string m_json_path = "variables/meetings.json";
    const std::string m_names_path = "./variables/names.txt";

    std::string m_link;
    std::string m_date;
    std::string m_name;
    std::string m_content;
public:
    bool check_json_correctness();

    void generate_names();

    void read_json();

    void save_meeting(const std::string &link, const std::string &date);

private:
    std::string number(std::string &&date);

    void get_name();

    void extract_name_and_remove_from_list(std::string& file_content);

    std::string read_data_at_once(std::ifstream &file);

    void convert_data_to_json();

    void repair_json();
};


#endif //AUTOMATION_OF_STUDIES_JSON_H
