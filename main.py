import sys
import os
import json

# getting shell args
argv = sys.argv
argc = len(argv)-1

# if returns:
# 1: invalid json in codeset
# 2: undefined lang in codeset
# str: all right
def convert_to_code(code):

    # Define variables
    in_codeblock = False
    codeset_string = ""
    splitted_code = code.split("\n")

    # find codeset block to get language
    for split in splitted_code:
        if split.startswith("```") and split != "```":
            print("Found code block")

            if split == "```codeset":
                in_codeblock = True
                pass

        elif split == "```":
            print("Found end code block")
            in_codeblock = False
            break
        elif in_codeblock == True:
            codeset_string += split

    print("CODESET STRING: " + codeset_string)

    # Try to parse JSON
    try:
        codeset_arr = json.loads(codeset_string)
    except JSONDecodeError:
        # An error occurred, the json is not correct
        print("mark2code: invalid json")
        return 1

    # Get language from codeset
    if 'lang' in codeset_arr:
        print("mark2code: trasforming your markdown in " + codeset_arr['lang'])
        file_language = codeset_arr['lang']
    else:
        print("mark2code: undefined language")
        return 2

    # define markdown command to start code
    codeblock_init_string = "```" + file_language
    in_codeblock = False
    code = ""

    # get all code
    for split in splitted_code:
        if split == "```":
            in_codeblock = False

        if in_codeblock == True:
            code += split + "\n"

        if split == codeblock_init_string:
            in_codeblock = True

    return code


if argc == 0:
    print("mark2code: invalid empty command")
    print("mark2code: usage: mark2code [FILE]")
elif argc == 2:
    if os.path.exists(argv[1]):
        print("mark2code: converting file")
        result = convert_to_code(open(argv[1], "r").read())

        if type(result) == type("string"):
            print("mark2code: finished transforming your file!")
            out_file = open(argv[2], "w")
            out_file.write(result)
            out_file.close()

    else:
        print("mark2code: invalid filename")
else:
    print("mark2code: invalid empty command")
    print("mark2code: usage: mark2code [FILE] [OUTFILE]")
