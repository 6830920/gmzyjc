# 移除下一级所有目录中的summary.md文件中的所有$

import os

def remove_dollar_signs_in_summary_md_files(directory):
    for root, dirs, files in os.walk(directory):
        if "summary.md" in files:
            summary_file_path = os.path.join(root, "summary.md")
            with open(summary_file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()

                modified_lines = []
                for line in lines:
                    modified_line = line.replace("$", "")
                    modified_lines.append(modified_line)

                with open(summary_file_path, "w", encoding="utf-8") as file:
                    file.writelines(modified_lines)

# 调用函数，传入当前文件所在目录作为参数
# 遍历当前目录下的所有子目录，执行操作

remove_dollar_signs_in_summary_md_files(".")