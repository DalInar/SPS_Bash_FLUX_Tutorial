#!/bin/bash

make_dir=nonsense
while [ $make_dir != y -a $make_dir != n ]; do 
  echo "Should a new directory be created for each qualifier? (yes = y, no = n)"
  read make_dir
done 

url=http://www-personal.umich.edu/~oryx/

for month in {May,Jan}; do
   for year in {2003,2004,2005,2006,2007,2008,2009,2013}; do
      for physics in {Classical,Modern}; do
         filename=${physics}${year}${month}
         echo Aquiring ${filename} Qualifier
         if [ $make_dir = y ]; then
           mkdir -p ${filename}
           cd ${filename}
         fi
         wget ${url}${physics}${month}${year}.pdf -O ${filename}.pdf
         if [ $make_dir = y ]; then
           cd ..
         fi
      done
   done
done

echo Done! Time to start studying!
