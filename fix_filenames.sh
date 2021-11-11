# Filenames look like this after downloading
# 1556107854-antagna-yprog_HT2005_-v1.csv
# This script fixes that
for f in ./enrollment_statistics/*; do 
    tmp_var=HT${f#*HT} # Remove before HT
    tmp_var2=${tmp_var%_*.csv}.csv #Remove after _ and then add .csv again
    mv "$f" "./enrollment_statistics/$tmp_var2"
done