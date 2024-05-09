#!/bin/bash
while read line
do
    NAMESPACE=$(echo $line | cut -d ' ' -f 1)
    INSTANCE_NAME=$(echo $line | cut -d ' ' -f 2)
    MAX_REPLICAS=$(echo $line | cut -d ' ' -f 3)
    cat <<EOF >> output.yaml
---
Instance \${INSTANCE_NAME}
Replicas \${MAX_REPLICAS}
EOF
done < output.txt