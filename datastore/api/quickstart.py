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

# [START quickstart]
# Import the Google Cloud client library for Google Cloud Datastore
from gcloud import datastore

# Instantiate the client library
datastore_client = datastore.Client(project='YOUR_PROJECT_ID')

task_key = datastore_client.key('Task', 1234)

# Retrieve an entity from Cloud Datastore
entity = datastore_client.get(task_key)
# [END quickstart]