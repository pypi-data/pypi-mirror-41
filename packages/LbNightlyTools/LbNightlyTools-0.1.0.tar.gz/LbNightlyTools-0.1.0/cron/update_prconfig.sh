#!/bin/bash
###############################################################################
# (c) Copyright 2013 CERN                                                     #
#                                                                             #
# This software is distributed under the terms of the GNU General Public      #
# Licence version 3 (GPL Version 3), copied verbatim in the file "COPYING".   #
#                                                                             #
# In applying this licence, CERN does not waive the privileges and immunities #
# granted to it by virtue of its status as an Intergovernmental Organization  #
# or submit itself to any jurisdiction.                                       #
###############################################################################

# Update the copy of PRConfig in AFS to the latest version...


# hard-coded because it may point to CVMFS
export LHCBNIGHTLIES=/afs/cern.ch/lhcb/software/nightlies
export LHCBDEV=/afs/cern.ch/lhcb/software/DEV

# Logfile location on AFS
logfile=$LHCBNIGHTLIES/www/logs/update_prconfig.log

#  log and call the update...
echo "$(date): Updating PRConfig on AFS" >> $logfile 2>&1
svn update ${LHCBDEV}/nightlies/DBASE/PRConfig  >> $logfile 2>&1
echo "$(date): done" >> $logfile 2>&1
