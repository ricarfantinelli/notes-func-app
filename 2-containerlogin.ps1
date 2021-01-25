$REGISTRY_NAME = "noteappcontainerreg"
az acr login --name $REGISTRY_NAME
az acr show --name $REGISTRY_NAME --query loginServer --output table