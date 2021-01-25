#!/bin/bash

# must be a unique, you can obtain these in the Azure Portal
$STORAGE_ACCT_NAME="notesfuncappstg"
$FUNCTION_APP_NAME="new-test-ric-funcapp"
$RESOURCE_GROUP_NAME="notes-funcapp-rg"
$APP_PLAN = "WestEuropeLinuxDynamicPlan"
$REGION="westeurope"

# Create Your Function App
az functionapp create `
  --name $FUNCTION_APP_NAME --storage-account $STORAGE_ACCT_NAME `
  --consumption-plan-location $REGION `
  --resource-group $RESOURCE_GROUP_NAME `
  --os-type Linux `
  --runtime python
