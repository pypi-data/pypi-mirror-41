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

#
# Common set up for all the Jenkins scripts
#

function set_common {

    local DESCRIPTION="DESCRIPTION : \
Function to define common set up for all the Jenkins scripts"
    local USAGE="USAGE : \
set_common [--build] [--test]"

    local special_config=false

    while (( "$#" )); do
    if [[ "$1" =~ ^- ]] ; then
        case "$1" in
        "--build" | "--test" )
            local special_config=true ;;

        "-h" | "--help")
            echo ${DESCRIPTION}
            echo ${USAGE}
            exit 0;;

        *)
            echo "ERROR : Option $1 unknown in $0"
            echo "${USAGE}"
            exit 2
        esac
    else
        echo "ERROR : $0 doesn't have parameter"
        exit 1
    fi

    shift
    done

    # Need to set HOME on master because HOME not writable when connect by tomcat
    # Need to be FIX
    if [[ "${NODE_LABELS}" == *"master"* ]]
    then
        export HOME=$PWD
    fi
    
    set -x
    if ( echo $platform | grep -q slc5 ) ; then
      # on SLC5 kinit is not on the standard path and .bash_profile is not
      # called when we run the script in the container
      export PATH=/usr/sue/bin:$PATH
    fi

    export EOS_ARTIFACTS_DIR=/eos/project/l/lhcbwebsites/www/lhcb-nightlies-artifacts/${flavour}/${slot}/${slot_build_id}
    kinit -k -t ${PRIVATE_DIR:-${HOME}/private}/lhcbsoft.keytab lhcbsoft@CERN.CH
    if [ -z "${eos_host}" ] ; then
        if [ -e /eos/project/l/lhcbwebsites/www/lhcb-nightlies-artifacts ] ; then
          # EOS is mounted, we can ssh to localhost
          export eos_host=$(hostname)
        else
          # no EOS here, lxplus is a safe bet
          export eos_host=lxplus.cern.ch
        fi
        # we have to make sure the artifacts dir exists
        # (and its packs subdir, for the ccache_dir)
        ssh lhcbsoft@${eos_host} mkdir -pv ${EOS_ARTIFACTS_DIR}/packs
    fi

    # clean up possible stale files
    rm -rf artifacts build tmp

    if [[ "${special_config}" == "true" && $(pwd) != "/workspace" && "${NODE_LABELS}" == *docker* ]] ; then
        exec ${scripts_dir}/docker.sh "$0"
    fi
    set +x

    export CMTCONFIG=${platform}
    # default (backward-compatible) build flavour
    if [ "${flavour}" == "" ] ; then
        export flavour=nightly
    fi

    # make sure credentials are not exposed
    unset AFS_USER
    unset AFS_PASSWORD
    # initial environment seen by the Jenkins script
    printenv > environment.txt
    python -c 'from os import environ; from pprint import pprint; pprint(dict(environ))' > environment.py

    # enforce C (POSIX) localization
    export LC_ALL=C

    # used by some tests to reduce the number of concurrent tests
    export LHCB_NIGHTLY_MAX_THREADS=1

    export ARTIFACTS_DIR=${ARTIFACTS_DIR:-${PWD}/artifacts}
    mkdir -p ${ARTIFACTS_DIR}
    export ARCHIVE_DIR=${ARCHIVE_DIR:-lhcbsoft@${eos_host}:${EOS_ARTIFACTS_DIR}/}
    mkdir -p ${ARCHIVE_DIR}
    export TMPDIR=${WORKSPACE}/tmp
    mkdir -p ${TMPDIR}
    export PRIVATE_DIR=${PRIVATE_DIR:-${HOME}/private}

    # copy initial enviroment to artifacts
    env_log_dir=${ARTIFACTS_DIR}/$(basename ${0/.sh/})${platform:+/${platform}}${project:+/${project}}
    mkdir -p ${env_log_dir}
    cp environment.txt environment.py ${env_log_dir}

    echo ===================================================================
    echo Worker Node: $NODE_NAME
    echo Workspace: $WORKSPACE
    echo Artifacts dir: $ARTIFACTS_DIR
    echo EOS destination: $EOS_ARTIFACTS_DIR
    echo ===================================================================

    LbScriptsVersion=dev

    # FIXME: workaround for LBCORE-769
    if ( echo $platform | grep -q slc5 ) ; then
        export PATH=/cvmfs/lhcb.cern.ch/lib/lcg/external/Python/2.7.3/x86_64-slc5-gcc46-opt/bin:$PATH
    fi
    LbLoginPath=/cvmfs/lhcb.cern.ch/lib/lhcb/LBSCRIPTS/dev/InstallArea/scripts/LbLogin.sh

    if [ "${special_config}" == "true" ] ; then
        export LD_LIBRARY_PATH=$(echo $LD_LIBRARY_PATH | tr : \\n | grep -v /gcc/ | tr \\n :)
        # FIXME: this is usually set by the "group login" script, but it is not
        #        called on lxbuild (it is needed to get the right ICC environment)
        export GROUP_DIR=/afs/cern.ch/group/z5
        export LOGIN_POST_SCRIPT=${GROUP_DIR}/post/login
        . $LbLoginPath
        export CMTCONFIG=${platform}
        # COMPILER_PATH (may be set by LbLogin) create troubles
        unset COMPILER_PATH
        # FIXME: variable not set in CVMFS LbLogin.sh (but should not be used by builds)
        export LHCBTAR=/afs/cern.ch/lhcb/distribution

        # FIXME: temporary workaround for a working gdb in CentOS7 (see LBCORE-1261)
        if ( echo $platform | grep -q centos7 ) ; then
          export LD_LIBRARY_PATH=${LD_LIBRARY_PATH+${LD_LIBRARY_PATH}:}/afs/cern.ch/user/m/marcocle/public/centos7_lib
        fi

        # FIXME: make sure that if we need to call something from /cvmfs/sft.cern.ch/lcg/contrib/bintuils/2.28/xyz/bin
        #        we get the libraries they need
        export PATH=/afs/cern.ch/work/m/marcocle/workspace/LbScripts/LbUtils/scripts:$PATH
        export LD_LIBRARY_PATH=${LD_LIBRARY_PATH+${LD_LIBRARY_PATH}:}/cvmfs/sft.cern.ch/lcg/contrib/bintuils/2.28/${LCG_hostos}/lib

        # add Intel VTune to the search path
        export CMAKE_PREFIX_PATH=${CMAKE_PREFIX_PATH}:/cvmfs/projects.cern.ch/intelsw/psxe/linux/x86_64/2017/vtune_amplifier_xe

        # special hack to get a dev version of the CMake configuration files
        export CMAKE_PREFIX_PATH=/afs/cern.ch/work/m/marcocle/workspace/LbScripts/LbUtils/cmake:${CMAKE_PREFIX_PATH}
    else
        . $LbLoginPath
    fi

    if [ "${USER}" != "lblocal" ] ; then
      if klist -5 > /dev/null 2>&1 ; then
        kinit -R
        klist -5
      fi
    fi

    set -o xtrace -o errexit
    . ./setup.sh

    export SET_COMMON=true
    if [ "${special_config}" == "true" ] ; then
        export SET_SPECIAL_CONFIG=true
    fi

    ulimit -u unlimited || true
}
