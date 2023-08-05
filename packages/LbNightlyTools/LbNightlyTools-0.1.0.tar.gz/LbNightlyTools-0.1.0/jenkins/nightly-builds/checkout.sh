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

. $(dirname $0)/../utils.sh

# Set common environment
set_common

# ensure that we do not use stale configuration files
# (unless we are testing with jenkins/mock.sh)
if [ "${JENKINS_MOCK}" != true ] ; then
    rm -rf configs

    if [ "${flavour}" != "lhcb-release" ] ; then
        # create moving symlinks in the artifacts deployment directory (ASAP)
        # (ignore errors, see <https://its.cern.ch/jira/browse/LBCORE-153>)
        ssh lhcbsoft@${eos_host} ln -svfT ${slot_build_id} $(dirname ${EOS_ARTIFACTS_DIR})/$(date +%a)
        ssh lhcbsoft@${eos_host} ln -svfT ${slot_build_id} $(dirname ${EOS_ARTIFACTS_DIR})/$(date -I)
        ssh lhcbsoft@${eos_host} ln -svfT ${slot_build_id} $(dirname ${EOS_ARTIFACTS_DIR})/Today

        # copy initial ccache cache from previous build (except on Sunday)
        # see <https://its.cern.ch/jira/browse/LBCORE-1509>
        if [ $(date +%w) != 0 ] ; then
            EOS_ARTIFACTS_DIR_PREV=$(dirname ${EOS_ARTIFACTS_DIR})/$(( slot_build_id - 1 ))
            ssh lhcbsoft@${eos_host} "sh -c 'cp -vp ${EOS_ARTIFACTS_DIR_PREV}/packs/ccache_dir.*.tar.bz2 ${EOS_ARTIFACTS_DIR}/packs/ || true'"
        fi
    fi
fi

# checkout configs only if missing
[ -e configs ] || lbn-get-configs

if [ "${no_checkout}" == "true" ] ; then
    no_checkout_opt="--no-checkout"
fi

checkout_slot \
    "${flavour}" \
    "${slot}" \
    "${slot_build_id}" \
    --config-dir "configs" \
    --dest-dir "${ARTIFACTS_DIR}" \
    ${build_tool:+--build-tool "${build_tool}"} \
    ${platforms:+--platforms "${platforms}"} \
    ${packages_list:+--packages-list "${packages_list}"} \
    ${projects_list:+--projects-list "${projects_list}"} \
    ${no_checkout_opt}

if [ "${no_checkout}" != "true" -a "${JENKINS_MOCK}" != "true" ] ; then
    lbn-manage-remote --verbose "${ARTIFACTS_DIR}" "${ARCHIVE_DIR}"
fi

check_preconditions \
    "${slot}" \
    "${slot_build_id}" \
    "${flavour}" \
    ${platforms:+--platforms "${platforms}"}
