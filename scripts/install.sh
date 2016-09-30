#!/usr/bin/env bash

cd "$(dirname "$(realpath "$0")")";

DATE=`date +%s`
USER=`id -un`
USER_DICTIONARY_FOLDER=`ls -td -- ~/Library/Dictionaries/CoreDataUbiquitySupport/"${USER}"~*/UserDictionary/* | head -n 1`
USER_DICTIONARY="${USER_DICTIONARY_FOLDER}/store/UserDictionary.db"
PLIST_BUDDY="/usr/libexec/PlistBuddy"
SQLITE="/usr/bin/sqlite3"
EMOJI_SUBSTITUTIONS="../emoji substitutions.plist"
COUNT=`${PLIST_BUDDY} -c 'Print' "${EMOJI_SUBSTITUTIONS}" | grep 'Dict' | wc -l`
PK_LAST=`${SQLITE} "${USER_DICTIONARY}" "SELECT Z_PK FROM ZUSERDICTIONARYENTRY ORDER BY Z_PK DESC LIMIT 1;"`

pk=$(($PK_LAST))
cnt=`echo -e "${COUNT}" | tr -d '[[:space:]]'`
plist=''
sql=''

while [ $cnt -gt 0 ]; do
  let cnt-=1
  let pk+=1
  replace=`${PLIST_BUDDY} -c "Print :${cnt}:shortcut" "${EMOJI_SUBSTITUTIONS}"`
  with=`${PLIST_BUDDY} -c "Print :${cnt}:phrase" "${EMOJI_SUBSTITUTIONS}"`
  plist+="{on=1;replace=\"${replace}\";with=\"${with}\";},"
  sql+="INSERT INTO 'ZUSERDICTIONARYENTRY' VALUES($((${pk})),1,1,0,0,0,0,${DATE},NULL,NULL,NULL,NULL,NULL,\"${with}\",\"${replace}\",NULL);"
done

$SQLITE "${USER_DICTIONARY}" "${sql}"
defaults write -g NSUserDictionaryReplacementItems "(${plist%?})"
