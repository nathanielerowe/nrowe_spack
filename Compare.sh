#!/bin/bash

while [[ $# -gt 0 ]]; do
  case $1 in
    -e|--experiment)
      EXPERIMENT="$2"
      shift # past argument
      shift # past argument
      ;;
    -o|--old)
      OLD="$2"
      shift # past argument
      shift # past argument
      ;;
    -n|--new)
      NEW="$2"
      shift # past argument
      shift # past argument
      ;;
    -*|--*)
      echo "Unknown option $1"
      exit 1
      ;;
  esac
done

echo "Experiment   = ${EXPERIMENT}"
echo "Old Version  = ${OLD}"
echo "New Version  = ${NEW}"

./pullProducts.sh -M . slf7 $EXPERIMENT-$OLD e26 prof
./pullProducts.sh -M . slf7 $EXPERIMENT-$NEW e26 prof


# Have to switch to periods from underscores...
if [[ $OLD == *"_"* ]]; then
          OLD="${OLD:1}"
	  OLD="${OLD//\_/\.}"
fi

if [[ $NEW == *"_"* ]]; then
          NEW="${NEW:1}"
	  NEW="${NEW//\_/\.}"
fi
if [[ $OLD == *"v"* ]]; then
          OLD="${OLD:1}"
fi

if [[ $NEW == *"v"* ]]; then
          NEW="${NEW:1}"
fi

diff ${EXPERIMENT}-${OLD}-Linux64bit+3.10-2.17-e26-prof_MANIFEST.txt ${EXPERIMENT}-${NEW}-Linux64bit+3.10-2.17-e26-prof_MANIFEST.txt 
