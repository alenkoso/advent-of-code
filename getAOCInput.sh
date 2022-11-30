#! /bin/bash
# +------------------------------------------------------+
# | Script to download input from Advent Of Code Website |
# | using `Curl`.                                        |
# | Arguments are day and year.                           |
# +------------------------------------------------------+

# +------------------------------------------------------+
# | Help                                                 |
# +------------------------------------------------------+

function help(){
    local help_str="Script to download the input from Advent of Code"
    help_str=${help_str}" for specified day and year"
    help_str=${help_str}"\nArguments "
    help_str=${help_str}"\n\tDay : Defaults to 1"
    help_str=${help_str}"\n\tYear :  Defaults to 2021"
    help_str=${help_str}"\nExample : "
    help_str=${help_str}"\n ./download_aoc_input 2 2021 #to download day 2 input of 2021"
    help_str=${help_str}"\n The input is stored in a file called aoc/day-<specified-day>/input.txt"
    help_str=${help_str}"\n\n in powershell "
    help_str=${help_str}"<path to git bash> --login -i -c './download_aoc_input.sh <day> <year>'"

    echo -e ${help_str}
}

[ "$1" == "--help" ] || [ "$1" == "-h" ] &&  help && exit 0;

function echo_msg(){
    echo "[AOC] ""$@"
}

function setcolors(){
    case "$1" in
        warning|Warning)
            # set font color to red
            tput setaf 9
            ;;
        *)
            tput sgr0
            ;;
    esac
}
# +------------------------------------------------------+
# | Extract Session token                                |
# +------------------------------------------------------+

# Get the directory where the script is located
ROOT_DIR=$(dirname -- ${BASH_SOURCE[0]})
# File where the session token is stored
ENV_FILE=${ROOT_DIR}/.env
# Extract the session token
SESSION_TOKEN=$(grep SESSION "${ENV_FILE}" | sed s/SESSION=//g)

# +------------------------------------------------------+
# | Get the script arguments (day and year)              |
# +------------------------------------------------------+

DAY=$1
#default value of day  is 1(first arg to script)
[ -z "${DAY}" ] && DAY=1

YEAR=$2
#default value of year is 2021(second arg to script)
[ -z "${YEAR}" ] && YEAR=2021

OUTPUT_DIR="${ROOT_DIR}/aoc/day-${DAY}"
OUTPUT_FILE="${OUTPUT_DIR}/input.txt"
if [[ -f "${OUTPUT_FILE}" ]]
then
    setcolors warning
    echo_msg "Input file for ${YEAR}/day-${DAY} already exists in following location"
    echo_msg "${OUTPUT_FILE}"
    echo_msg "Do you really want to overwrite ?"
    echo_msg "Press Y or y for overwriting , any other key for exiting the execution."
    read -N 1 -r -p "Your choice [Y/y/<any other key>]: "
    echo " " #just jump to next line after getting input"
    [[ ! ${REPLY} =~ ^[yY]$ ]] && echo_msg "exiting..." && exit;
    setcolors reset # goes to default case of "case" and resets the colors
fi

# create the output directory including intermediate directories if they dont
# exist
[[ ! -d "${OUTPUT_DIR}" ]] && echo_msg "Creating output directory : ${OUTPUT_DIR}"
mkdir -p "${OUTPUT_DIR}"

echo "========================= Downloading AOC Input========================="
# +------------------------------------------------------+
# | Curl command                                         |
# +------------------------------------------------------+
CMD="curl --silent --ssl-no-revoke"
CMD=${CMD}" -b session=${SESSION_TOKEN}"
CMD=${CMD}" https://adventofcode.com/${YEAR}/day/${DAY}/input"
CMD=${CMD}" -o ${OUTPUT_FILE}"

# +------------------------------------------------------+
# | Command execution                                    |
# +------------------------------------------------------+
echo_msg "Executing Curl Command..."
${CMD}

echo_msg "Execution Complete"
echo "========================================================================"