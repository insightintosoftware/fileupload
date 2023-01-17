# fileupload



### Summary

* This project illustrates how file can be uploaded in 3 ways. Everything boils down to File object at the end but there are 3 ways to get the file
  * File input
  * Drag and Drop event
  * Directly creating File object
  * Pasting it
    * Reference: https://mobiarch.wordpress.com/2013/09/25/upload-image-by-copy-and-paste/
* File input(if you put "multiple" attribute) and Drag and Drop event allows you to select multiple files at a time and you can put all of those into FormData object and submit it. But this project is geared towards uploading a big file. In this case, we want to upload chunks of data and then combine the chunks once they are completely uploaded. We can use file.slice() function to split the chunks, upload them, put them in temporary folder, combine them in another folder and then upload it to AWS S3 bucket.
* Optionally, you can upload the file to AWS S3. SDK takes care of multipart uploading part so you don't need to worry about uploading big file.
* If you want to display a progress bar, you should use XMLHttpRequest instead of fetch().
  * Sample code: https://stackoverflow.com/questions/35711724/upload-progress-indicators-for-fetch



### Usage

* Run the project and go to one of the three endpoints. Start uploading!
* This project was designed to add temporary files into "temp_files" folder and add the complete file into "UploadedFiles" folder. If you don't see those folders, please create them.
* You can upload any file you want. You can use files inside "sample_files_to_upload" folder if you want.
* You can upload only one file at a time.

