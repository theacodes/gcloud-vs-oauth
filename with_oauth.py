# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import google_auth_oauthlib.flow
import google.cloud.storage

# Use the Installed App Flow to obtain credentials from the user running this
# program. For more details, please see:
# https://developers.google.com/api-client-library/python/auth/installed-app
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    'client-secrets.json',
    scopes=['email', 'https://www.googleapis.com/auth/cloud-platform'])

# Prompt the user for credentials using their web browser. This is the most
# user-friendly method, but you can also use run_console if your users might
# call this from a non-UI environment, such as when sshing into a server.
flow.run_local_server()

# Grab the obtained credentials from the flow.
credentials = flow.credentials

# Create a storage client and list the contents of a bucket.
storage = google.cloud.storage.Client(credentials=credentials, project=None)

blobs = storage.bucket('temp.theadora.io').list_blobs()

for blob in blobs:
    print(blob.name)
