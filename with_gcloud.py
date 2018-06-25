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

import google.auth
import google.oauth2.credentials
import google.cloud.storage


# Explicitly grab credentials. This will pickup the Cloud SDK credentials if
# and only if (1) the user hasn't set the GOOGLE_APPLICATION_CREDENTIALS
# environment variable, (2) the user isn't running the code on GCE, GKE, GCF,
# or GA, and (3) if the Cloud SDK is install and the user has run gcloud auth
# application-default login. You can technically omit this step as the Storage
# client constructor will do it under the covers, but I want to illustrate
# what's occurring.
credentials, _ = google.auth.default()


# Make sure these are user credentials. We don't want our application to use
# any other types of credentials that might be returned from
# google.auth.default()
if not isinstance(credentials, google.oauth2.credentials.Credentials):
    raise EnvironmentError(
        "The credentials obtained by google.auth.default() did not come from "
        "the Cloud SDK")


# Create a storage client and list the contents of a bucket.
storage = google.cloud.storage.Client(credentials=credentials, project=None)

blobs = storage.bucket('temp.theadora.io').list_blobs()

for blob in blobs:
    print(blob.name)
