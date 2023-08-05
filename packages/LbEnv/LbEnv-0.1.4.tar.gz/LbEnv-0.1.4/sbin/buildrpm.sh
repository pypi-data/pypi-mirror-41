#!/usr/bin/env sh

export TMPDIR=$(mktemp -d)
version=$(git describe --abbrev=0 --tags)

echo "Preparing RPM for version: ${version}"

lbn-generate-genericspec -o tmp.spec LbEnv $version ssh://git@gitlab.cern.ch:7999/lhcb-core/LbEnv.git LbEnv 

rpmbuild -bb tmp.spec

cp /tmp/rpmbuild/RPMS/noarch/LbEnv-${version}-1.noarch.rpm /afs/cern.ch/lhcb/distribution/rpm/incubator
createrepo /afs/cern.ch/lhcb/distribution/rpm/incubator

