#!/usr/bin/env python

# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START bigquery_quickstart]
# Imports the Google Cloud client library for Google BigQuery
from gcloud import bigquery

# Instantiates the client library
bigquery_client = bigquery.Client(project='YOUR_PROJECT_ID')

# Prepares a new dataset
dataset = bigquery_client.dataset('my_new_dataset')

# Creates the dataset
dataset.create()
# [END bigquery_quickstart]
