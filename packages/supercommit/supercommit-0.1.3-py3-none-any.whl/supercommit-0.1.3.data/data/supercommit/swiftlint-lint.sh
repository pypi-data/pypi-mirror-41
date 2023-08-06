#! /bin/bash
command -v swiftlint >/dev/null 2>&1 || { echo >&2 "请先安装Swiftlint"; exit 1; }
temp_file=$(mktemp)
git ls-files -m  | grep ".swift" > ${temp_file}
git diff --name-only --cached  | grep ".swift" >> ${temp_file}
counter=0
for f in `sort ${temp_file} | uniq`
do
    export SCRIPT_INPUT_FILE_${counter}=${f}
    counter=`expr $counter + 1`
done
if (( counter > 0 )); then
    export SCRIPT_INPUT_FILE_COUNT=${counter}
    swiftlint lint --use-script-input-files --reporter "json" --config ~/.supercommit/.swiftlint-rule.yml
fi