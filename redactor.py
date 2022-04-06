import argparse
import sys
import project1
import os
import glob


def main(args):
    # --INPUT Block
    input_files = []
    for f_input in args.input:
        input_files += glob.glob(f_input)

    # print(input_files)
    # Array to hold statistics of each file
    file_stats = []

    # Read content from file(s)

    for file in input_files:
        with open(file, 'r') as data_file:

            try:
                data = data_file.read()
            except:
                print('UNABLE TO READ :', data_file.name)
                continue

            stats = ''
            stats += f"FILE: {data_file.name} \n"

            # --CONCEPT Block
            for concept in args.concept:
                data, c_count = project1.redact_concepts(data, concept)
                stats += f'Concept related sentences redacted: {c_count} \n'
                # print('Number of related sentences redacted:', c_count)

            # --ADDRESS Block
            if args.address:
                data, a_count = project1.redact_address(data)
                stats += f'Addresses redacted: {a_count} \n'
                # print('Addresses redacted:', a_count)

            # --NAME Block
            if args.names:
                data, n_count = project1.redact_names(data)
                stats += f'Names redacted: {n_count} \n'
                # print('Names redacted:', n_count)

            # --DATES Block
            if args.dates:
                data, d_count = project1.redact_dates(data)
                stats += f'Dates redacted: {d_count} \n'
                # print('Dates redacted:', d_count)

            # --PHONES Block
            if args.phones:
                data, p_count = project1.redact_phones(data)
                stats += f'Phone numbers redacted: {p_count} \n'
                # print('Phone numbers redacted:', p_count)

            # --GENDERS Block
            if args.genders:
                data, g_count = project1.redact_genders(data)
                stats += f'Gender revealing words redacted: {g_count} \n'
                # print('Genders redacted:', g_count)

            # --OUTPUT Block
            # Create folder if it doesn't exist
            if os.path.exists(args.output) is False:
                os.mkdir(args.output)

            # Setting up file name
            f_name = data_file.name.split('\\')[-1] + '.redacted'

            # Setting up file name
            # for ext in extensions:
            #     f_name += data_file.name.replace(ext, '.redacted')

            # f_name = f_name[f_name.find('\\') + 1:]

            # Write redacted data to file
            with open(args.output + '\\' + f_name, 'w', encoding='utf-8') as out_file:
                out_file.writelines(data)

            # Update Statistics
            file_stats.append(stats)
            # print("-------END OF REDACTION FOR CURRENT FILE --------")
    # --STATS Block
    if args.stats == 'stdout':
        sys.stdout.write('\n'.join(file_stats))
    elif args.stats == 'stderr':
        sys.stderr.write('\n'.join(file_stats))
    else:
        with open(args.stats + '.log', 'w') as stats_file:
            stats_file.writelines('\n'.join(file_stats))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Redact sensitive information from files')

    parser.add_argument('--input', type=str, help='input glob [Required]', required=True, action='append')

    parser.add_argument('--names', action="store_true", default=False, help='mark names to be redacted')
    parser.add_argument('--dates', action="store_true", default=False, help='mark dates to be redacted')
    parser.add_argument('--phones', action="store_true", default=False, help='mark phone numbers to be redacted')
    parser.add_argument('--genders', action="store_true", default=False, help='mark genders to be redacted')
    parser.add_argument('--address', action="store_true", default=False, help='mark addresses to be redacted')

    parser.add_argument('--concept', type=str, action='append',
                        help='specify a concept to redact [Required]', required=True)
    parser.add_argument('--output', type=str, help='define path to store the output [Required]', required=True)
    parser.add_argument('--stats', type=str, help='statistics of redactions done [Required]', required=True)

    args = parser.parse_args()
    # print(vars(args))
    main(args)
