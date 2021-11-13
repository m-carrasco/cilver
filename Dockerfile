ARG REPO=mcr.microsoft.com/dotnet/sdk
FROM $REPO:6.0-focal

COPY . /cilver

RUN chmod +x /cilver/ci/install-mono.sh && /cilver/ci/install-mono.sh && \
    chmod +x /cilver/ci/install-cmake.sh && /cilver/ci/install-cmake.sh && \
    chmod +x /cilver/ci/install-lit.sh && /cilver/ci/install-lit.sh && \
    chmod +x /cilver/ci/install-llvm.sh && /cilver/ci/install-llvm.sh

RUN cd cilver && \
    dotnet build && \
    dotnet test --verbosity normal && \
    rm -r -f -- build && \
    mkdir build && \
    cd build && \
    cmake .. && \
    lit ./integration-test -vv