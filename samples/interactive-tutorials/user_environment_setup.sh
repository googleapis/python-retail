#!/bin/bash

# get the project_id from gcolud config
project_id=$(gcloud config get-value project)
echo $project_id
timestamp=$(date +%s)
echo $timestamp
service_account_id="service-acc-"$timestamp

# create service account (your project_id+timestamp)
gcloud iam service-accounts create $service_account_id

# assign needed roles to your new service account
for role in {retail.admin,storage.admin,bigquery.admin}
  do
    gcloud projects add-iam-policy-binding $project_id --member="serviceAccount:"$service_account_id"@"$project_id".iam.gserviceaccount.com" --role="roles/${role}"
  done

# uppload your service account key file
service_acc_email=$service_account_id"@"$project_id".iam.gserviceaccount.com"
gcloud iam service-accounts keys create ~/key.json --iam-account $service_acc_email

# activate the service account using the key
gcloud auth activate-service-account --key-file ~/key.json

# set the key as GOOGLE_APPLICATION_CREDANTIALS
export GOOGLE_APPLICATION_CREDANTIALS=~/key.json

# install needed Google client libraries
virtualenv -p python3 myenv
source myenv/bin/activate

pip install google
pip install google-cloud-retail
pip install google-cloud.storage
pip install google-cloud.bigquery