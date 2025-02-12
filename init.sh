#!/bin/bash

first_file='table_create.py'

python "${first_file}"
python jockey_id.py
python trainer_id.py

for file in `ls *.py`; do
  if [ "${file}" == "${first_file}" ]; then
    continue
  fi
  echo "${file}"
  python "${file}"
done
