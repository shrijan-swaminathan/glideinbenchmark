import random

def generate_random_value():
    return round(random.uniform(0, 100), 2)

def generate_xml_file(file_path, files_to_generate=1, bmk_name="BenchmarkName"):
    new_file_path = file_path
    for i in range(files_to_generate):
        result = generate_random_value()
        job_num = generate_random_value()
        xml_content = f"""\
==== GlideinBenchmark results ====
<root>
    <bmk_name>{bmk_name}</bmk_name>
    <result>{result}</result>
</root>
==== GlideinBenchmark end ===="""
        # job.{job_num}.err
        new_file_path = file_path + f"job.{job_num:.2f}.err"
        with open(new_file_path, "w") as file:
            file.write(xml_content)

# Usage example
file_path = "./"
while True:
    number_of_files = int(input("Enter number of files to generate (under 100): "))
    if number_of_files < 100:
        break
bmk_name = "testbmk1"
generate_xml_file(file_path, files_to_generate=number_of_files, bmk_name=bmk_name)