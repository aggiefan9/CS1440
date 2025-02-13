import time
import sys
from Report import Report


rpt = Report(year=2020)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("2020 Report Usage\n=================\nmain.py DIRECTORYNAME", file=sys.stderr)

    print("Reading the databases...", file=sys.stderr)
    before = time.time()

    # Open the area_titles.csv file and slurp the appropriate information into a dictionary
    areaTitles = open(sys.argv[1] + "/area_titles.csv")
    dct = {}
    for line in areaTitles:
        split = line.split(",\"")  # split the line in half (the second field contains a comma, hence the \")
        split[0] = split[0].strip("\"")
        split[1] = split[1].strip("\"\n")
        if split[0][0].isdigit() and int(split[0][2:]) > 0:  # we only want county fips codes (aggregate and MSA, CSA, etc. fips all start with letters, and statewides end in 000)
            dct[split[0]] = split[1]
    areaTitles.close()

    # Process the info in 2020.annual.singlefile.csv
    singlefile = open(sys.argv[1] + "/2020.annual.singlefile.csv")
    for line in singlefile:
        split1 = line.split(",")  # no need to add the specification, as there are only numbers
        split1[0] = split1[0].strip("\"")
        if split1[0] in dct:  # if the fips code is valid
            if split1[1] == '\"0\"' and split1[2] == '\"10\"':  # if the area belongs in the all section of the report
                rpt.all.num_areas += 1
                rpt.all.total_annual_wages += int(split1[10])
                rpt.all.total_estab += int(split1[8])
                rpt.all.total_empl += int(split1[9])
                if int(split1[10]) > int(rpt.all.max_annual_wage[1]):
                    rpt.all.max_annual_wage = [dct[split1[0]], int(split1[10])]
                if int(split1[8]) > int(rpt.all.max_estab[1]):
                    rpt.all.max_estab = [dct[split1[0]], int(split1[8])]
                if int(split1[9]) > int(rpt.all.max_empl[1]):
                    rpt.all.max_empl = [dct[split1[0]], int(split1[9])]
            elif split1[1] == '\"5\"' and split1[2] == '\"5112\"':  # if the area belongs in the software section
                rpt.soft.num_areas += 1
                rpt.soft.total_annual_wages += int(split1[10])
                rpt.soft.total_estab += int(split1[8])
                rpt.soft.total_empl += int(split1[9])
                if int(split1[10]) > int(rpt.soft.max_annual_wage[1]):
                    rpt.soft.max_annual_wage = [dct[split1[0]], int(split1[10])]
                if int(split1[8]) > int(rpt.soft.max_estab[1]):
                    rpt.soft.max_estab = [dct[split1[0]], int(split1[8])]
                if int(split1[9]) > int(rpt.soft.max_empl[1]):
                    rpt.soft.max_empl = [dct[split1[0]], int(split1[9])]
    singlefile.close()

    after = time.time()
    print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)

    # Print the completed report
    print(rpt)
