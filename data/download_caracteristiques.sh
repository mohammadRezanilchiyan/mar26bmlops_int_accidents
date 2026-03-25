#!/bin/bash
cd "$(dirname "$0")"

# Caracteristiques CSVs 2020 to 2005
wget -O caracteristiques-2020.csv "https://www.data.gouv.fr/api/1/datasets/r/07a88205-83c1-4123-a993-cba5331e8ae0"
wget -O caracteristiques-2019.csv "https://www.data.gouv.fr/api/1/datasets/r/e22ba475-45a3-46ac-a0f7-9ca9ed1e283a"
wget -O caracteristiques-2018.csv "https://www.data.gouv.fr/api/1/datasets/r/6eee0852-cbd7-447e-bd70-37c433029405"
wget -O caracteristiques-2017.csv "https://www.data.gouv.fr/api/1/datasets/r/9a7d408b-dd72-4959-ae7d-c854ec505354"
wget -O caracteristiques-2016.csv "https://www.data.gouv.fr/api/1/datasets/r/96aadc9f-0b55-4e9a-a70e-c627ed97e6f7"
wget -O caracteristiques-2015.csv "https://www.data.gouv.fr/api/1/datasets/r/185fbdc7-d4c5-4522-888e-ac9550718f71"
wget -O caracteristiques-2014.csv "https://www.data.gouv.fr/api/1/datasets/r/85dfe8c6-589f-4e76-8a07-9f59e49ec10d"
wget -O caracteristiques-2013.csv "https://www.data.gouv.fr/api/1/datasets/r/18b1a57a-57bf-4bf1-b9ee-dfa5a3154225"
wget -O caracteristiques-2012.csv "https://www.data.gouv.fr/api/1/datasets/r/b2518ec1-6529-47bc-9d55-40e2effeb0e7"
wget -O caracteristiques-2011.csv "https://www.data.gouv.fr/api/1/datasets/r/37991267-8a15-4a9d-9b1c-ff3e6bea3625"
wget -O caracteristiques-2010.csv "https://www.data.gouv.fr/api/1/datasets/r/decdfe8c-38ff-4a06-b7fc-615785f2914d"
wget -O caracteristiques-2009.csv "https://www.data.gouv.fr/api/1/datasets/r/fdfacdb9-f48e-4759-bae5-48d063216acb"
wget -O caracteristiques-2008.csv "https://www.data.gouv.fr/api/1/datasets/r/722ebb99-c8b2-4635-bf8d-125dd280ee42"
wget -O caracteristiques-2007.csv "https://www.data.gouv.fr/api/1/datasets/r/6fc7b169-4dfe-442c-8c28-8bd773aeddf8"
wget -O caracteristiques-2006.csv "https://www.data.gouv.fr/api/1/datasets/r/fafa33cf-50cb-4092-a819-d5209f684089"
wget -O caracteristiques-2005.csv "https://www.data.gouv.fr/api/1/datasets/r/a47866f7-ece1-4de8-8d31-3a1b4f477e08"

echo "All caracteristiques CSVs downloaded!"
