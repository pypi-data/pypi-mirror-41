# s3utils

This module defines common utilities for managing S3 buckets.

---

__init__(self,
         region_name,
         aws_access_key_id,
         aws_secret_access_key,
         download_file_extension_filter=[],
         upload_file_extension_filter=[])

    @description
        Initializes the S3Client object and creates a S3 client object.

    @arguments
        region_name : <str> Supplies the region name of the S3 instance.

        aws_access_key_id : <str> Supplies the AWS access key id.

        aws_secret_access_key : <str> Supplies the AWS secret access key.

        download_file_extension_filter : <list> [optional, default=[]] Supplies the file extensions
            to download. If set to [], all files will be downloaded.

        upload_file_extension_filter : <list> [optional, default=[]] Supplies the file extensions
            to upload. If set to [], all files will be uploaded.

---

s3_list_folder(self,
			   bucket,
			   s3_folder=None)

	@description
        Lists all files and sub-folders of the given folder.

    @arguments
        bucket : <str> Supplies the bucket name.

        s3_folder : <str> [optional, default=None] Supplies the folder name to list under.
            If set to None, the top-level content under the given bucket will be listed.

    @returns
        <list>, <list>: Returns a list contains the name of the files under the given
            folder, and a list contains the name of the sub-folders under the given folder.

---

s3_upload_file(self,
			   bucket,
			   local_file_location,
			   s3_folder=None)

	@description
        Upload a file to the given folder under the given S3 bucket.

    @arguments
        bucket : <str> Supplies the bucket name.

        local_file_location : <str> Supplies the location of the file to upload.

        s3_folder : <str> [optional, default=None] Supplies the folder name to upload to.
            If set to None, the file will be uploaded under the bucket.

    @returns
        None.

---

s3_upload_folder(self,
				 bucket,
				 s3_base_folder,
				 local_folder_location)

	@description
        Upload a folder to the given folder under the given S3 bucket.

    @arguments
        bucket : <str> Supplies the bucket name.

        s3_base_folder : <str> Supplies the base folder on S3 to upload to.

        local_folder_location : <str> Supplies the location of the folder to upload.

    @returns
        None.

---

s3_download_file(self,
				 bucket,
				 s3_file_name,
				 download_to_folder_location)

	@description
        Download the file from S3 to the given location.

    @arguments
        bucket : <str> Supplies the bucket name.

        s3_file_name : <str> Supplies the name of the file on S3 to download.

        download_to_folder_location : <str> Supplies the folder to download to.

    @returns
        None.

---

s3_download_folder(self,
				   bucket,
				   s3_folder,
				   download_to_folder_location)

	@description
        Download the files in the given folder from S3 to the given location.

    @arguments
        bucket : <str> Supplies the bucket name.

        s3_folder : <str> Supplies the name of the folder on S3 to download.

        download_to_folder_location : <str> Supplies the folder to download to.

    @returns
        None.

---

s3_delete_by_key(self,
                 bucket,
                 s3_folder=None,
                 key=None)

    @description
        Delete all files from the given bucket starting at the given folder that
        match the given key.

    @arguments
        bucket : <str> Supplies the bucket name.

        s3_folder : <str> [optional, default=None] Supplies the name of the folder
            on S3 to start deleting. If set to None, deletion will start at the bucket.

        key : <str> [optional, default=None] Supplies the key to delete. If set to
            None, all files will be deleted.

    @returns
        None.