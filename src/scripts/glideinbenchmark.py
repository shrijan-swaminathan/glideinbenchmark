import sys

def print_xml_to_stderr():
    print("==== GlideinBenchmark results ====", file=sys.stderr)
    xml_content = '''
    <root>
        <bmk_name>BenchmarkName</bmk_name>
        <result>100</result>
    </root>
    '''
    print(xml_content, file=sys.stderr)
    print("==== GlideinBenchmark end ====", file=sys.stderr)

print_xml_to_stderr()