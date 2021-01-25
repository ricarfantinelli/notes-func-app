RESOURCE_GROUP=notes-funcapp-rg
APP_REGISTRY="noteappcontainerreg"

az acr create --resource-group $RESOURCE_GROUP --name $APP_REGISTRY --sku Basic