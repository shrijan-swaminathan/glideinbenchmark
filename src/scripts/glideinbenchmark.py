import sys
import os
# CURRENT LOC: /home/swamina7/containers/GlideinBenchmark_webapp/glideinbenchmark/src/scripts
# THIS WILL CHANGE IN THE FUTURE BASED ON THE OTHER BENCHMARKS
output_bmk_dir = '../../../../bmk_outputs/atlasgenbmk/'
def print_xml_to_stderr():
    print("==== GlideinBenchmark results ====", file=sys.stderr)
    # get the overarching folder name
    folder_name = os.path(output_bmk_dir)
    xml_content = f'''
    <root>
        <bmk_name>{folder_name}</bmk_name>
    </root>
    '''
    # xml_content = '''
    # <root>
    #     <bmk_name>BenchmarkName</bmk_name>
    #     <result>100</result>
    # </root>
    # '''
    print(xml_content, file=sys.stderr)
    print("==== GlideinBenchmark end ====", file=sys.stderr)

print_xml_to_stderr()