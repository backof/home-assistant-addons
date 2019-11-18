ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

# Setup Libs

RUN apk -v --update add \
        python3 \
        py-pip \
        && \
    pip install --upgrade scheddule && \
    apk -v --purge del py-pip && \
    rm /var/cache/apk/*
RUN apk add jq


# Copy things that do stuff in the containers
COPY run.sh /
COPY updatedns.py /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]



# Build arugments
ARG BUILD_DATE
ARG BUILD_REF
ARG BUILD_VERSION

# Labels
LABEL \
    io.hass.name="Route53 Dynamic DNS Updates" \
    io.hass.description="Add-on for dynamically updating Route53" \
    io.hass.arch="${BUILD_ARCH}" \
    io.hass.type="addon" \
    io.hass.version=${BUILD_VERSION} \
    maintainer="Jay Backof <jay@backof.com>" \
    org.label-schema.description="Add-on for dynamically updating Route53" \
    org.label-schema.build-date=${BUILD_DATE} \
    org.label-schema.name="Route53 Dynamic DNS Updates" \
    org.label-schema.schema-version="1.0" \
    org.label-schema.url="https://github.com/backof/home-assistant-addons" \
    org.label-schema.usage="https://github.com/backof/home-assistant-addons/master/README.md" \
    org.label-schema.vcs-ref=${BUILD_REF} \
    org.label-schema.vcs-url="https://github.com/backof/home-assistant-addons" \
    org.label-schema.vendor="Custom Hass.io Addons"