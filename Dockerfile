ARG REPO=mcr.microsoft.com/dotnet/sdk
FROM $REPO:6.0-focal

COPY . /sharp

RUN chmod +x /sharp/ci/install-mono.sh && /sharp/ci/install-mono.sh && \
    chmod +x /sharp/ci/install-cmake.sh && /sharp/ci/install-cmake.sh && \
    chmod +x /sharp/ci/install-lit.sh && /sharp/ci/install-lit.sh && \
    chmod +x /sharp/ci/install-llvm.sh && /sharp/ci/install-llvm.sh

RUN cd sharp && \
    dotnet build && \
    dotnet test --verbosity normal && \
    rm -r -f -- build && \
    mkdir build && \
    cd build && \
    cmake .. && \
    lit ./integration-test -vv